import rules

# Predicados predefinidos
is_authenticated = rules.is_authenticated
is_staff = rules.is_staff
is_superuser = rules.is_superuser
is_group_member = rules.is_group_member

# Permisos para productos
rules.add_perm('productos_app.view_producto', is_authenticated)  # Todos los usuarios autenticados pueden ver productos
rules.add_perm('productos_app.add_producto', is_staff)  # Solo el personal puede agregar productos
rules.add_perm('productos_app.change_producto', is_staff)  # Solo el personal puede cambiar productos
rules.add_perm('productos_app.delete_producto', is_superuser)  # Solo superusuarios pueden eliminar productos

# Permisos para características
rules.add_perm('productos_app.view_caracteristica', is_authenticated)  # Todos los usuarios autenticados pueden ver características
rules.add_perm('productos_app.add_caracteristica', is_authenticated)  # Todos los usuarios autenticados pueden agregar características
rules.add_perm('productos_app.change_caracteristica', is_authenticated)  # Todos los usuarios autenticados pueden cambiar características
rules.add_perm('productos_app.delete_caracteristica', is_staff)  # Solo el personal puede eliminar características

# Ejemplo de un grupo específico para editores
rules.add_perm('productos_app.editor', is_group_member('editors'))  # Solo los miembros del grupo "editors" pueden tener este permiso
