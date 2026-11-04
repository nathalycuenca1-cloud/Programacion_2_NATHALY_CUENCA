>>> p = Project(name="Tarea 1", description="Descripcion de la tarea")
>>> p.save()
>>> from tasks.models import ReservaVuelos
Traceback (most recent call last):
  File "/usr/lib/python3.12/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<console>", line 1, in <module>
ImportError: cannot import name 'ReservaVuelos' from 'tasks.models' (/home/alumnos/Documents/Programacion_II_Nathaly_Cuenca/django/taskflow_api/tasks/models.py). Did you mean: 'Reserva_vuelos'?
>>> from tasks.models import Reserva_vuelos
>>> Reserva_vuelos.objects.create(nombre="Vuelo Quito-Guayaquil", clase_vuelo="Ejecutiva", datos_pasajero="Nathaly Cuenca", horarios="10:00 AM - 11:00 AM")
<Reserva_vuelos: Vuelo Quito-Guayaquil>
>>> 
KeyboardInterrupt
>>> 