from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Caracteristica
from .forms import ProductForm, CaracteristicaForm

# Listar los productos
def list_products(request):
    productos = Producto.objects.all()
    for producto in productos:
        # Permite mostrar hasta 5 características por producto en la página principal
        producto.caracteristicas = Caracteristica.objects.filter(producto=producto)[:5] 
    return render(request, 'productos_app/lista.html', {'productos': productos})

# Agregar productos
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Guarda el nuevo producto en la base de datos
            form.save()
            return redirect('list_products')
    else:
        # Si no es una solicitud POST, se crea un formulario vacío
        form = ProductForm()
    return render(request, 'productos_app/agregar.html', {'form': form})

# Eliminar productos
def delete_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('list_products')

# Características del producto (Adicional)
def detail_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    caracteristicas = Caracteristica.objects.filter(producto=producto)
    context = {
        'producto': producto,
        'caracteristicas': caracteristicas
    }
    return render(request, 'productos_app/detalle.html', context)

# Agregar nuevas características al producto
def add_caracteristica(request, producto_id):
    # Busca el producto por su ID o devuelve un error 404 si no existe
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = CaracteristicaForm(request.POST)
        if form.is_valid():
            # Asocia la característica al producto antes de guardarla
            caracteristica = form.save(commit=False)
            caracteristica.producto = producto
            caracteristica.save()
            return redirect('detail_product', id=producto.id)
    else:
        # Si no es una solicitud POST, se crea un formulario vacío
        form = CaracteristicaForm()
    return render(request, 'productos_app/add_caracteristica.html', {'form': form, 'producto': producto})

# Editar las características del producto
def edit_caracteristica(request, caracteristica_id):
    caracteristica = get_object_or_404(Caracteristica, id=caracteristica_id)
    if request.method == 'POST':
        form = CaracteristicaForm(request.POST, instance=caracteristica)
        if form.is_valid():
            # Guarda los cambios realizados en la característica
            form.save()
            return redirect('detail_product', id=caracteristica.producto.id)
    else:
        # Si no es una solicitud POST, se crea un formulario con los datos de la característica existente
        form = CaracteristicaForm(instance=caracteristica)
    return render(request, 'productos_app/edit_caracteristica.html', {'form': form, 'caracteristica': caracteristica})

# Eliminar características del producto
def delete_caracteristica(request, id):
    caracteristica = get_object_or_404(Caracteristica, id=id)
    caracteristica.delete()
    return redirect('detail_product', id=caracteristica.producto.id)