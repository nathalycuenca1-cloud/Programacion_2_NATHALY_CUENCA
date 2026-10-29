from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Por hacer"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        DONE = "DONE", "Completada"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Reserva_vuelos(models.Model):
    nombre = models.CharField(max_length=100)
    clase_vuelo = models.TextField(blank=True)
    datos_pasajero = models.TextField(blank=True)
    horarios = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Mision(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Alumno(models.Model):
    sensei = models.ForeignKey(
        Sensei, on_delete=models.CASCADE, related_name="alumnos"
    )
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField(Mision, related_name="alumnos")

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="perfiles/")

    def __str__(self):
        return f"Perfil de {self.alumno.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(
        Estudiante, through="Participacion", related_name="actividades"
    )

    def __str__(self):
        return self.titulo


class Participacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.actividad.titulo} ({self.rol})"
