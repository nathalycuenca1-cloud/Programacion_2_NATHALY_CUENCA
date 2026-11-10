from django.shortcuts import render, redirect
from catalogo.forms.libro_form import LibroForm
from catalogo.models import Libro


def libro_list(request):
    libros = Libro.objects.all().order_by('titulo')
    return render(request, 'libros/libro_list.html', {'libros': libros})


def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()

    return render(request, 'libros/formulario.html', {'form': form})


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


def delete_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'libros/confirm_delete.html', {'libro': libro})