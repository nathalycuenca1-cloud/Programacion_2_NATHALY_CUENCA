#string xadenas de carateres 
jedi="Qui-Gon Jinn"
aprendiz="Obi-Wan Kenobi"
droide="R2-D2"
planeta="Naboo"
codigo="327"

print("Jedi es: " + jedi)
print("El jedi", type(jedi))
print("Aprendiz es: " + aprendiz)
print("El aprendiz", type(aprendiz))
print("Droide es: " + droide)
print("El droide", type(droide))
print("Planeta es: " + planeta)
print("El planeta", type(planeta))
print("Codigo es: " + codigo)
print("El codigo", type(codigo))

longitud_jedi=len(jedi)
print("La longitud del nombre del jedi es:" + str(longitud_jedi))
longitud_aprendiz=len(aprendiz)
print("La longitud del nombre del aprendiz es:" + str(longitud_aprendiz))

mensaje= "La federación de comercio ha establecido un bloque en  Naboo."
print("Mensaje es:", mensaje)
mensaje_mayusculas=mensaje.upper()
print("Mensaje en mayusculas es:" +  mensaje_mayusculas)
mensaje_minusculas=mensaje.lower()
print("Mensaje en minusculas es:" +  mensaje_minusculas)


comunicado= "Los jedi son enviados a Naboo."
print("Comunicado es:" + comunicado)
nuevo_comunicado=comunicado.replace("Naboo", "Tatooine")
print("Nuevo comunicado es:" + nuevo_comunicado)

planetas= "Naboo, tatooine, coruscant, alderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es:" + str(planetas_lista))
print("El primer planeta de la lista es:" + planetas_lista[0])

droide="R2-D2"
print("El droide es:" + droide)
print("El primer caracter del droide es:" + droide[0])
print("El segundo caracter del droide es:" + droide[1])
print("El tercer caracter del droide es:" + droide[2])
print("El cuarto caracter del droide es:" + droide[3])
print("El quinto caracter del droide es:" + droide[4])
print("El sexto caracter del droide es:" + droide[-1])