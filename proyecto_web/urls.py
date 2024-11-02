from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos_app.urls')),
    path('user_rules/', include('user_rules.urls')),
]