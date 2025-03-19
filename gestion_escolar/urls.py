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
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('api/', include(router.urls)),  # Incluye las rutas generadas por el router de la API
]

# Incluir las URLs de la API generadas por el router (ya se ha hecho con include)
