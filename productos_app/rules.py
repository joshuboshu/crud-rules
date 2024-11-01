import rules

def add_perm_if_not_exists(name, pred):
    # Verifica si la regla ya existe en el registro de permisos antes de agregarla
    if name not in rules.permissions.permissions:
        rules.add_perm(name, pred)

# Define permisos asegurándote de que no se dupliquen
add_perm_if_not_exists('productos_app.add_producto', rules.is_staff)
add_perm_if_not_exists('productos_app.view_producto', rules.is_authenticated)
add_perm_if_not_exists('productos_app.change_producto', rules.is_staff)
add_perm_if_not_exists('productos_app.delete_producto', rules.is_staff)
