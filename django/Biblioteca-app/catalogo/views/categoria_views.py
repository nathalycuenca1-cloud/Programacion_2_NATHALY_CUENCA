from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.form.categoria_form import CategoriaForm
from catalogo.models import Categoria

def categoria_list(request):
    categorias = Categoria.objects.all()
    # Corrige esta línea quitando 'template/' del inicio:
    return render(request, 'catalogo/categorias/categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    
    # Cambia 'catalogo/categoria_form.html' por la ruta de tu archivo actual:
    return render(request, 'catalogo/categorias/formulario.html', {'form': form})