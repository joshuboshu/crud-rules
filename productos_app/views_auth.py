from django.contrib.auth import get_user_model, login
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('list_products')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})