from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib.auth.models import Group
from .forms import RegistroForm, AlumnoForm
from .models import Alumno, Docente, Calificacion, Asistencia, Materia
from .serializers import AlumnoSerializer, CalificacionSerializer, DocenteSerializer, AsistenciaSerializer
from rest_framework import viewsets

# Función para asignar usuario a un grupo
def asignar_grupo(usuario, grupo_nombre):
    grupo, _ = Group.objects.get_or_create(name=grupo_nombre)
    usuario.groups.add(grupo)
    usuario.save()

# Vista de registro con asignación de grupo y redirección
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            asignar_grupo(user, form.cleaned_data['rol'])  # Asignar grupo
            login(request, user)  # Iniciar sesión automáticamente
            # Redirigir según el grupo
            if user.groups.filter(name='Alumno').exists():
                return redirect('dashboard_alumno')  # Redirige al dashboard de Alumno
            elif user.groups.filter(name='Docentes').exists():
                return redirect('panel_docente')  # Redirige al panel de Docente
            elif user.groups.filter(name='Administrativos').exists():
                return redirect('panel_administrativo')  # Redirige al panel Administrativo
            else:
                return redirect('pagina_inicio')  # Redirigir a la página de inicio si no hay grupo asignado
    else:
        form = RegistroForm()
    return render(request, 'auth/registro.html', {'form': form})

# Vista de login con redirección según el grupo
# Vista de login con redirección según el grupo
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Determinar a dónde redirigir según el rol del usuario
            if user.groups.filter(name='Alumno').exists():
                redirect_url = '/alumnos/dashboard/'
            elif user.groups.filter(name='Docentes').exists():
                redirect_url = '/docente/docente/'
            elif user.groups.filter(name='Administrativos').exists():
                redirect_url = '/administrativo/admin_panel/'
            else:
                redirect_url = '/'

            # Si la solicitud es AJAX, responder con JSON
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({'success': True, 'redirect_url': redirect_url})
            else:
                return redirect(redirect_url)

        # Si las credenciales son incorrectas
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({'success': False, 'error': 'Usuario o contraseña incorrectos'})

    else:
        form = AuthenticationForm()

    # Obtener el token CSRF
    csrf_token = get_token(request)
    
    return render(request, 'auth/login.html', {'form': form, 'csrf_token': csrf_token})

# Restricción de acceso por grupos
def es_docente(user):
    return user.groups.filter(name='Docentes').exists()

def es_administrativo(user):
    return user.groups.filter(name='Administrativos').exists()

def es_alumno(user):
    return user.groups.filter(name='Alumno').exists()

# Redireccionar según el grupo del usuario
@login_required
def redireccionar_usuario(request):
    user = request.user

    if hasattr(user, 'alumno'):
        return redirect('dashboard_alumno')  # Redirige a la vista correcta
    elif hasattr(user, 'docente'):
        return redirect('panel_docente')  # Asegúrate de que esta vista existe
    elif hasattr(user, 'administrativo'):
        return redirect('panel_administrativo')  # Asegúrate de que esta vista existe
    else:
        return redirect('pagina_inicio')  # O alguna otra vista por defecto
# Vistas protegidas según el grupo
@login_required
@user_passes_test(es_docente)
def panel_docente(request):
    return render(request, 'docente/panel_docente.html')

@login_required
@user_passes_test(es_administrativo)
def panel_administrativo(request):
    return render(request, 'administrativo/panel_administrativo.html')

@login_required
@user_passes_test(es_alumno)
def dashboard_alumno(request):
    return render(request, 'alumnos/dashboard.html')

# Listar y crear alumnos
@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestion/lista_alumnos.html', {'alumnos': alumnos})

@login_required
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'gestion/form_alumno.html', {'form': form})

# API con DRF
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

# Listar materias
@login_required
def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, 'materias/lista_materias.html', {'materias': materias})

# Asignaciones
@login_required
def asignar_materia_docente(request):
    return HttpResponse("Vista para asignar materia a docente.")

@login_required
def asignar_materia_alumno(request):
    return HttpResponse("Vista para asignar materia a alumno.")

@login_required
def asignar_calificacion(request, alumno_id):
    return HttpResponse(f"Vista para asignar calificación al alumno con ID {alumno_id}")

@login_required
def registrar_asistencia(request, alumno_id):
    return HttpResponse(f"Vista para registrar asistencia del alumno con ID {alumno_id}")

# Lista de calificaciones
@login_required
def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'gestion/lista_calificaciones.html', {'calificaciones': calificaciones})

# Página de inicio
def pagina_inicio(request):
    return render(request, 'inicio.html')

def redireccionar(request):
    # Aquí define la lógica para redirigir según el rol del usuario
    return redirect('pagina_inicio')  # Cambia esto según la redirección deseada