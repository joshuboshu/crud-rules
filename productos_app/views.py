from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Caracteristica
from .forms import ProductForm, CaracteristicaForm
from django.contrib.auth.decorators import login_required
from rules.contrib.views import permission_required as rules_permission_required


@login_required
@rules_permission_required('productos_app.view_producto')
def list_products(request):
    productos = Producto.objects.all()
    for producto in productos:
        producto.caracteristicas = Caracteristica.objects.filter(producto=producto)[:5]
    return render(request, 'productos_app/lista.html', {'productos': productos})

@login_required
@rules_permission_required('productos_app.add_producto')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado exitosamente.")
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'productos_app/agregar.html', {'form': form})

@login_required
@rules_permission_required('productos_app.change_producto', raise_exception=True)
def edit_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('list_products')
    else:
        form = ProductForm(instance=producto)
    return render(request, 'productos_app/agregar.html', {'form': form})

@login_required
@rules_permission_required('productos_app.delete_producto', raise_exception=True)
def delete_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    messages.success(request, "Producto eliminado exitosamente.")
    return redirect('list_products')

@login_required
@rules_permission_required('productos_app.view_caracteristica')
def detail_product(request, id):
    producto = get_object_or_404(Producto, id=id)
    caracteristicas = Caracteristica.objects.filter(producto=producto)
    return render(request, 'productos_app/detalle.html', {'producto': producto, 'caracteristicas': caracteristicas})

@login_required
@rules_permission_required('productos_app.add_caracteristica')
def add_caracteristica(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = CaracteristicaForm(request.POST)
        if form.is_valid():
            caracteristica = form.save(commit=False)
            caracteristica.producto = producto
            caracteristica.save()
            messages.success(request, "Característica agregada exitosamente.")
            return redirect('detail_product', id=producto.id)
    else:
        form = CaracteristicaForm()
    return render(request, 'productos_app/add_caracteristica.html', {'form': form, 'producto': producto})

@login_required
@rules_permission_required('productos_app.change_caracteristica', raise_exception=True)
def edit_caracteristica(request, caracteristica_id):
    caracteristica = get_object_or_404(Caracteristica, id=caracteristica_id)
    if request.method == 'POST':
        form = CaracteristicaForm(request.POST, instance=caracteristica)
        if form.is_valid():
            form.save()
            messages.success(request, "Característica actualizada exitosamente.")
            return redirect('detail_product', id=caracteristica.producto.id)
    else:
        form = CaracteristicaForm(instance=caracteristica)
    return render(request, 'productos_app/edit_caracteristica.html', {'form': form, 'caracteristica': caracteristica})

@login_required
@rules_permission_required('productos_app.delete_caracteristica', raise_exception=True)
def delete_caracteristica(request, id):
    caracteristica = get_object_or_404(Caracteristica, id=id)
    caracteristica.delete()
    messages.success(request, "Característica eliminada exitosamente.")
    return redirect('detail_product', id=caracteristica.producto.id)
