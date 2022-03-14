from itertools import count
from pizzaNode import pizzaNode
import threading
import time
import datetime
import logging 

class pizzaList:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0

    def insert(self, ingredient, quantity):

        newPizza=pizzaNode(ingredient, quantity)
        self.size+=1

        if self.head is None:
            self.head =newPizza
            self.bottom= newPizza
        else:
            self.bottom.setNext(newPizza)
            self.bottom= newPizza

    def getText(self):
        printer =self.head
        text=""

        for i in range(self.size):
            text+="\nPizza de {}, cantidad de pizzas ordenadas: {}".format(printer.getIngredient(), printer.getQuantity())
            printer=printer.getNext()
        
        return text
    
    def getTime(self):
        printer=self.head
        total=0

        for i in range(self.size):
            total+=int(printer.getTime())
            printer=printer.getNext()
        return total

    def backTime(self):
        self.head.setTime()


        
        


        

    
