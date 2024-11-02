from django.urls import path
from .views import assign_role, get_roles

urlpatterns = [
    path('assign-role/', assign_role, name='assign_role'),
    path('api/roles/', get_roles, name='get_roles'),
]

