from types import NoneType
from orderNode import orderNode
import threading
import time
import datetime
import logging 

class orderList:
    def __init__(self):
        self.head= None
        self.bottom= None
        self.size=0
    

    def insert(self, costumer, pizzaList):

        newOrder=orderNode(costumer, pizzaList)
        self.size+=1

        if self.head is None:
            self.head =newOrder
            self.bottom= newOrder
        else:
            self.bottom.setNext(newOrder)
            self.bottom= newOrder
    
    def poll(self):
        if self.head.getNext()!=NoneType:
            self.head=self.head.getNext()
            self.size-=1
    
    def getTimer(self):
        if self.head!=None:
            print("\nLa orden de: "+self.head.getCostumer())
            print("Que contiene: "+self.head.getPizzaList().getText())
            print("Estara lista en: "+str(self.head.getPizzaList().getTime()))
            if self.head.getNext()!=None:
                printer=self.head.getNext()
                for i in range(self.size-1):
                    print("Proximas ordenes: ")
                    print("\nLa orden de: "+printer.getCostumer())
                    print("Que contiene: "+printer.getPizzaList().getText())
                    print("Tiempo que tardará una vez iniciada: "+str(printer.getPizzaList().getTime()))

        else:
            print("\nSe completo las ordenes")

    def startCount(self):
        counter=self.head
        timer=0
        for i in range(100000):
            if counter!=None:
                counter.getPizzaList().backTime()
                time.sleep(1)
                if counter.getPizzaList().getTime()<=0:
                    if self.head.getNext()!=NoneType:
                        counter=self.head.getNext()
                        self.poll()
                        time.sleep(1)
                        continue
                    else:
                        self.poll()
                        time.sleep(1)
                        continue
                else:
                    continue
            else:
                time.sleep(1)
                continue
            


    def startTrip(self):
        t1= threading.Thread(name="Hilo 2", target=self.startCount,args=())
        t1.start()


        

