## FUNCIONES 
def activar_sistema():
    print("-- sistema de naboo --")
    print("sistema de control activado")

activar_sistema()

# Funciones con parametros 

def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe : {nombre}")


saludar_jedi("Qui-Gon Jim")    
saludar_jedi("Obi-Wan Kenobi")  

def mostrar_nave(nombre, combustible):
    print(f"nave: {nombre}")
    print(f"cantidad combustible: {combustible}")

mostrar_nave("Caza N-1", 80)

# Funciones que devuelven datos o informacion 
# Return 


def calcular_combustible(inicial, consumo):
    restante = inicial - consumo 
    return restante 


def calcular_combustible2(inicial, consumo):
    return inicial - consumo

resultado = calcular_combustible(100,25)
print(f"combustible:{resultado}")

resultado = calcular_combustible2(100, 35)
print(f"combustible: {resultado}")


print(f"combustible:{calcular_combustible2(100,15)}")