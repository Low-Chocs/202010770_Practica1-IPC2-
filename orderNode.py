class orderNode:
    def __init__(self, costumer, pizzaList):
        self.costumer=costumer
        self.pizzaList= pizzaList
        self.next=None

    def getCostumer(self):
        return self.costumer
    
    def getPizzaList(self):
        return self.pizzaList
    
    def getNext(self):
        return self.next

    def setCostumer(self, costumer):
        self.costumer= costumer

    def setPizzaList(self, pizzaList):
        self.pizzaList= pizzaList

    def setNext(self, next):
        self.next = next