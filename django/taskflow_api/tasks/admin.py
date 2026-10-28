from django.contrib import admin
from .models import Project, Task, Reserva_vuelos, Sensei, Alumno, Perfil, Estudiante, Actividad, Participacion

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date')
    search_fields = ('title', 'project__name')
    list_filter = ('status', 'project')

@admin.register(Reserva_vuelos)
class ReservaVuelosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'clase_vuelo', 'datos_pasajero', 'horarios', 'created_at')
    search_fields = ('nombre', 'datos_pasajero', 'clase_vuelo')
    list_filter = ('clase_vuelo', 'created_at')