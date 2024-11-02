from django import forms
from django.contrib.auth.models import User
from .models import Role, UserRole

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['user', 'role']
    
    def __init__(self, *args, **kwargs):
        super(UserRoleForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
        self.fields['role'].queryset = Role.objects.all()
