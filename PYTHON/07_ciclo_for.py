 # ciclo for

naves=[
    "caza N-1",
    "Nave real de Naboo",
    "transporte"

]
for nave in naves:
    print("Inspeccionando ",nave)

print("Inspección realizada")

droides = range (1,17,3)
print("Tipo de droides :", type(droides))
for droide in droides:
    print(f"Reparar : droide B1-{droide}")
    print(f"Tipo de dato droide:  {type(droide)}")


planetas=[
    "Naboo",
    "Tatooine",
    "Coruscant",
]

recorrido = enumerate(planetas, start=5)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipos de dato {type(posicion)}: {type(planeta)}")

paises = [
    "Ecuador",
    "venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos",

]
for pais in paises:
    if pais =="Chile":
        continue
    if pais == "Brasil":
        break
    print(f"Pais visitado: {pais}")

jedi = {}
jedi_activo = {
    "nombre": "obiwan",
    "fuerza": "120",
    "estilo_pelea": "Samurai",
    "misiones": ["guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"

    }
}
print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad=8, turbo_laser=2)
print(nave)