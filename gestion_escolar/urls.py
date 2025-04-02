from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views
from .views import AlumnoViewSet, CalificacionViewSet, DocenteViewSet, AsistenciaViewSet

# Crear el router de la API para los viewsets
router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet)
router.register(r'docentes', DocenteViewSet)
router.register(r'calificaciones', CalificacionViewSet)
router.register(r'asistencias', AsistenciaViewSet)

# Rutas de la UI (interfaz de usuario)
urlpatterns = [
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),

    # Redirección de roles
    path('calificaciones/', views.lista_calificaciones, name='lista_calificaciones'),
    path('docente/', views.panel_docente, name='panel_docente'),
    path('admin_panel/', views.panel_administrativo, name='panel_administrativo'),
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('redireccionar/', views.redireccionar_usuario, name='redireccionar_usuario'),

    # Funciones de usuario específicas
    path('docentes/', views.panel_docente, name='vista_docentes'),
    path('administrativos/', views.panel_administrativo, name='vista_administrativos'),
    path('alumno/dashboard/', views.dashboard_alumno, name='dashboard_alumno'),

    # Rutas de gestión de datos y operaciones
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('materias/', views.lista_materias, name='lista_materias'),

    # Rutas de administración
    path('administrativo/asignar-materia-docente/', views.asignar_materia_docente, name='asignar_materia_docente'),
    path('administrativo/asignar-materia-alumno/', views.asignar_materia_alumno, name='asignar_materia_alumno'),

    # API 
    path('api/', include(router.urls)),  # Incluye las rutas generadas por el router de la API
]
