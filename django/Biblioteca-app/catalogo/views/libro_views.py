from django.db.models import Q
from django.shortcuts import render, redirect
from catalogo.forms.libro_form import LibroForm
from catalogo.models import Libro
from django.contrib.auth.decorators import login_required, permission_required

from catalogo.models.categoria import Categoria

@login_required
@permission_required('catalogo.view_libro', raise_exception=True)
def libro_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria', '').strip()
    libros = Libro.objects.select_related('categoria_id').all()
    if pista:
        libros = libros.filter(
            Q(titulo__icontains=pista) |
            Q(autor__icontains=pista) |
            Q(categoria_nombre__icontains=pista)
        )
    if categoria_id:
        libros = libros.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()

    contexto = {
        'libros': libros,
        'categorias': categorias.objects.all(),
        'pista': pista,
        'categoria_id': categoria_id,
    }
    return render(request, 'libros/libro_list.html', 
                  {'libros': libros},
                   contexto
                  )

@login_required
@permission_required('catalogo.add_libro', raise_exception=True)
def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()

    return render(request, 'libros/formulario.html', {'form': form})

@login_required
@permission_required('catalogo.change_libro', raise_exception=True)
def update_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libros/formulario.html', {'form': form})

@login_required
@permission_required('catalogo.delete_libro', raise_exception=True)
def delete_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libros/confirm_delete.html', {'libro': libro})