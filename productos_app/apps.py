from django.apps import AppConfig

class ProductosAppConfig(AppConfig):
    name = 'productos_app'
    
    def ready(self):
        import productos_app.permissions
