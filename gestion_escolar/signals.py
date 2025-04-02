from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def crear_grupos(sender, **kwargs):
    grupos = ["Alumno", "Docente", "Administrativo"]
    for grupo in grupos:
        Group.objects.get_or_create(name=grupo)
