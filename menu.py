import orderNode
from pizzaList import pizzaList
from orderList import orderList
import threading
import time
import datetime
import logging 

class menu:

    def __init__(self):
        self.order=orderList()
        self.killer=0

    def principal(self):
        option=0
        while option !=4:
        
            print("\nPizzas Manolo \n1. Ingresar nuevo pedido"
            +"\n2. Mostrar pedidos\n3. Cancelar pedido\n4. Salir")
            
            option=int(input("Seleccione una opción\n"))

            if option<1:
                print("\nSeleccione un digito mayor o igual a 1\n")
            elif option>4:
                print("\nSeleccione un digito menor o igual a 4\n")
            elif option==1:
                self.option1()
            elif option==2:
                t2= threading.Thread(name="Hilo 411", target=self.option2,args=())
                t2.start()  
                t2.join()
            elif option==3:
                print("Opción 3")
        
        print("Feliz día")
    
    def option1(self):
        costumer=input("\nPor favor ingrese el nombre del cliente\n")
        print()
        ingredient=0
        option=0
        pizza=pizzaList()

        while option!=2:
        
            ingredient=int(input("Ingrese el ingrediente de la pizza: \n1. Pepperoni \n2. Salchicha\n3. Carne"
            +"\n4. Queso \n5. Piña\n6. Descartar nueva pizza\n"))

            if ingredient<1:
                print("\nSeleccione un digito mayor o igual a 1\n")
            elif ingredient>6:
                print("\nSeleccione un digito menor o igual a 4\n")
            elif ingredient>=1 and ingredient<=4:
                quantity=int(input("Ingrese una cantidad\n"))
                if quantity>0:
                    pizza.insert(ingredient, quantity)
            elif ingredient==5:
                print("Opcion 5")
            elif ingredient==6:
                print("Opcion 6")

            option=int(input("\n¿Desea agregar una pizza con otro ingrediente?\n1. Agregar otra pizza\n2. Guardar pedido\n3.Descartar pedido\n"))

            if option ==2:
                self.order.insert(costumer, pizza)
                if self.killer==0:
                    self.order.startTrip()
                    self.killer+=1
                print("Se ha guardado exitosamente la orden")


            if option ==3:
                option=2
    
    def option2(self):
        option=0
        for i in range(10):
            self.order.getTimer()
            time.sleep(2)

    
        


        


    