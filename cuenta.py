class Cuenta:
   

    titular=input("Ingrese su nombre y apellido: ")
    cantidad = float(input("Ingrese monto de su cuenta: "))

    def __init__(self, titular=titular, cantidad=cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad: $", self.cantidad)
        
    def ingresar(self):
        deposito=float(input("Que cantidad deseas depositar?"))
        self.cantidad += deposito
        print("Se ingresaron $", deposito, "en total tenés $",self.cantidad, "pesos")
        
    def retirar(self):
        retiro=float(input("Que cantidad deseas retirar?"))
        self.cantidad -= retiro
        print("Se retiraron $", retiro, "el saldo total es $",self.cantidad, "pesos")
cuenta1=Cuenta()
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirar() 
