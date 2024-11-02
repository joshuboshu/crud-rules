from django.contrib.auth.models import User
from user_rules.models import UserRole, Role

def assign_default_roles():
    for user in User.objects.all():
        if not hasattr(user, 'userrole'):
            role = Role.objects.first()  # Puedes elegir el rol que desees asignar inicialmente
            UserRole.objects.create(user=user, role=role)
