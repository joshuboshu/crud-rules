import rules

# Define reglas individuales
is_staff = rules.is_staff
is_authenticated = rules.is_authenticated

# Define permisos específicos para Producto
rules.add_perm('productos_app.add_producto', is_staff)
rules.add_perm('productos_app.view_producto', is_authenticated)
rules.add_perm('productos_app.change_producto', is_staff)
rules.add_perm('productos_app.delete_producto', is_staff)

@rules.predicate
def permission_rules(user):
    return user.is_authenticated and 'christophe' in user.username

rules.add_perm('is_jean', permission_rules)