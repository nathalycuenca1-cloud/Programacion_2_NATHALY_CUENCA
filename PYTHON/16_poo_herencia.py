class Guerrero:
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre
    def presentarse(self):
        print("mi poderoso nombre es:", self.nombre)

class saiyajin(Guerrero):
    def __init__(self, nombre:str):
        super().__init__(nombre)
    def transformarse(self):
        print(self.nombre,"se transforma en super saiyajin" )

goku=saiyajin("goku")
goku.presentarse()
goku.transformarse()

class androide:
    nombre: str
    energia:int
    
    def __init__(self, nombre: str, energia: int):
        self.nombre = nombre
        self.energia = energia
        
    def mostar_energia(self):
        print("androide:", self.nombre)
        print("energia:", self.energia)

class adroiderecargable(androide):
    def __init__(self, nombre: str, energia: int):
        super().__init__(nombre, energia)
        
    def recargar(self, cantidad: int):
        if cantidad >0:
            self.energia += cantidad

androide1 = adroiderecargable("numero 17", 600)
print("*******androide de recarga******")
androide1.mostar_energia()
androide1.recargar(100)
print("******despues de recargar*******")
androide1.mostar_energia()