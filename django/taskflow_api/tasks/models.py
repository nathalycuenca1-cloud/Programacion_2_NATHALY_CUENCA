from django.db import models
from ssl import create_default_context


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):          
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):#tambien llamado enum riene opciones las cuales  vamos a encerrar
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    # ForeignKey: cada Task pertenece a UN Project.
    # Un Project puede tener MUCHAS Task — relación muchos a uno.
    project = models.ForeignKey(#aqui vemos una relacion
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)#aqui vemos una clase dentro de otra clase
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)#uno con hora otra con fecha
    created_at = models.DateTimeField(auto_now_add=True) 

class Reserva_vuelos(models.Model):
    nombre = models.CharField(max_length=100)
    clase_vuelo = models.TextField(blank=True)
    datos_pasajero = models.TextField(blank=True)
    horarios = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):          
        return self.nombre

class Sensei(models.Model):
     nombre= models.CharField(max_length=100)
     edad = models.TextField(blank=True)
     create_at = models.DateTimeField(auto_now_add=True)   



class Alumno(models.Model):
    sensei= models.ForeignKey(Sensei, on_delete=models.CASCADE, related_name='alumnos')
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True) #como manera de auditoria de cuando se creo
    misiones = models.ManyToManyField('Mision',related_name='alumnos' )

    def _str_(self):
            return self.nombre 


class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/')
   



class Mision(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    def _str_(self):
            return self.nombre 


class Actividad(models.Model):
     titulo=models.CharField(max_length=100)
     objetivo=models.CharField(max_length=100)

     estudiantes = models.ManyToManyField(
          Estudiante, 
          through='Participacion')

class Participacion(models.Model):
    estudiante = models.ForeignKey(
         Estudiante,
         on_delete=models.CASCADE)
    actividad = models.ForeignKey(
         Actividad, 
         on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)  #estudiante_id


