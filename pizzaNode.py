class pizzaNode:
    def __init__(self, ingredient, quantity):
        self.ingredient=ingredient
        self.quantity=quantity
        self.next=None

        if self.ingredient==1:
            self.ingredientName="Pepperoni"
            self.time=3*int(self.quantity)
        elif self.ingredient==2:
            self.ingredientName="Salchicha"
            self.time=4*int(self.quantity)
        elif self.ingredient==3:
            self.ingredientName="Carne"
            self.time=10*int(self.quantity)
        elif self.ingredient==4:
            self.ingredientName="Queso"
            self.time=5*int(self.quantity)
        elif self.ingredient==5:
            self.ingredientName="Piña"
            self.time=2*int(self.quantity)

    def getTime(self):
        if self.time!=None:
            return self.time
        else:
            return " "

    def setTime(self):
        self.time-=1

    def getIngredientNumber(self):
        return self.ingredient
    
    def getIngredient(self):
        return self.ingredientName

    def getQuantity(self):
        return self.quantity
    
    def getNext(self):
        return self.next

    def setIngredient(self, ingredient):
        self.ingredient= ingredient

    def setQuantity(self, quantity):
        self.quantity= quantity
    
    def setNext(self, next):
        self.next = next