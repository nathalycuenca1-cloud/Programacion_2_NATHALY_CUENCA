from django.shortcuts import redirect, render
from django.http import HttpResponse

from tasks.forms import TaskForm, ProjectForm
from tasks.models import Project


def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)     

def register(request):
    """Registro de usuarios"""
    return HttpResponse("Registro de usuarios")

def sobre_nosotros(request):
    """Desarrollador"""
    return HttpResponse("Estas ante un <h1>gran desarrollador<h1>")

def greeting(request, nombre):
    """Registro de usuarios"""
    return HttpResponse(f"Hola, {nombre}, bienvenido")

def destination(request, titulo, nombre, cargo):
    """Registro de usuarios"""
    return HttpResponse(
        f"Bienvenido:{titulo} {nombre}, su cargo es {cargo}")

def area(request, base, altura):
    """Triangulo"""
    return HttpResponse(
        f"El area del triangiulo:{base*altura/2}")


def home(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/home.html", contexto)

# tasks/views.py
from django.shortcuts import render


def leads_like(request):
    contexto = {
        "Titulo": "Estudiante",
        "Nombre": "Nathaly",
        "Apellido": "Cuenca"
    }
    return render(request, "leads/leads-like.html")


def lista(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
        "projects": Project.objects.order_by("-created_at"),
    }
    return render(request, "projects/projects.html", contexto)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "modo": "crear"})

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect("tasks:task-lista")
    else:
        form = ProjectForm()
    
    return render(request, "projects/project_form.html", {"form": form, "modo": "crear"})