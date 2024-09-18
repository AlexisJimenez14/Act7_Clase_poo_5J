print("Programacion POO")
# definiendo clase
class Perro:
#funciones dentro de la clase
    def morder(self):
        print("el perro me mordio")
    def Datos_perro(self,nombre, edad):
        print(f"nombre: {nombre} edad : {edad}")


#zona de creacionde objeto
pitbull=Perro()

#zona de uso de objetos
pitbull.Datos_perro("boby","4")
pitbull.morder()
