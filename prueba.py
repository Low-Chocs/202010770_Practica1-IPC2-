import threading
import time
import datetime
import logging 

def consultar(id):
    time.sleep(2)
    print("xd")
    return

def guardar(contador):
    number=30
    for i in range(10):
        time.sleep(1)
        number-=1
        print(number)

#t1= threading.Thread(name="Hilo 1", target=consultar,args=(1,))
t2= threading.Thread(name="Hilo 2", target=guardar,args=(100,))

#t1.start()
t2.start()
#t1.join()
t2.join()