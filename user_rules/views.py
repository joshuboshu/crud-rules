from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from user_rules.utils import assign_default_roles
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_rules.models import UserRole, Role
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@user_passes_test(lambda u: u.is_superuser)
@require_POST
def set_user_role(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = json.loads(request.body)
        role_name = data.get("role")
        role = Role.objects.get(name=role_name)

        user_role, created = UserRole.objects.get_or_create(user=user)
        user_role.role = role
        user_role.save()

        return JsonResponse({"success": True, "role_name": role.name})
    except (User.DoesNotExist, Role.DoesNotExist, KeyError):
        return JsonResponse({"success": False})


@api_view(['GET'])
def get_roles(request):
    roles = Role.objects.all().values('id', 'name')
    return Response(list(roles))


@user_passes_test(lambda u: u.is_superuser)
@require_POST
def assign_role(request):
    try:
        data = json.loads(request.body)  # Obtiene los datos del cuerpo de la solicitud
        user_id = data.get('user_id')
        role_name = data.get('role')

        # Busca el rol por su nombre
        role = Role.objects.filter(name=role_name).first()
        if not role:
            return JsonResponse({'error': 'Rol no encontrado'}, status=400)

        # Obtiene o crea el UserRole
        user_role, created = UserRole.objects.get_or_create(user_id=user_id)
        user_role.role = role
        user_role.save()

        return JsonResponse({'success': 'Rol asignado correctamente'})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)