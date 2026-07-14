class Menuitem:

    def __init__(self,name, cost,water,milk,coffee):
        self.name=name
        self.cost=cost
        self.ingredents={"Water":water,
                         "Milk":milk,
                         "Coffee":coffee}

class MENU:

    def __init__(self):
        self.menu=["espresso","latte","cappuccino"]

    
    def get_item(self):
        for i in self.menu:
            print(i,",",end=" ")
    
    def find_drink(self, order_drink):

        if order_drink == "espresso":
            return Menuitem("Espresso", 1.50, 50, 0, 18)

        elif order_drink == "latte":
            return Menuitem("Latte", 2.50, 200, 150, 24)

        elif order_drink == "cappuccino":
            return Menuitem("Cappuccino", 3.00, 250, 100, 24)

        else:
            print("Drink not available.")
            return None

        

            
class Coffee_maker:
    def __init__(self,water,milk,coffee):
        self.resourse={"Water":water,
                       "Milk":milk,
                       "Coffee":coffee}
    

    def report(self):
        print(self.resourse)
        return True
    

    def is_resourse_sufficient(self,drink):
        
        for item in drink.ingredents:
            if self.resourse[item]<drink.ingredents[item]:
                return False
        return True
    

    def make_coffee(self,order):
        for item in order.ingredents:
            self.resourse[item]-=order.ingredents[item]
        

        
class MoneyMachine:

    def __init__(self):
        self.profit=0
    
    def report(self):
        return self.profit
    

    def make_payment(self,Cost):
        penny=0.01
        dime=0.10
        nickel=0.05
        quarter=0.25
        print("Insert the coins:")
        print("-"*100)
        print("The Price of the Latte : 2.50")
        print("Give the Money sir !!")
        print("-"*100)
        Penny=float(input("Insert the Penny : "))
        print("-"*100)
        print(f"Penny = {Penny}")
        print("-"*100)
        Dime=float(input("Insert the Dime: "))
        print("-"*100)
        print(f"Dime = {Dime}")
        print("-"*100)
        Nickel=float(input("Insert the Nickel : "))
        print("-"*100)
        print(f"Nickel = {Nickel}")
        print("-"*100)
        Quarter=float(input("Insert the Quarter : "))
        print("-"*100)
        print(f"Quartar = {Quarter}")
        print("-"*100)
        money=0
        money+=penny*Penny+dime*Dime+nickel*Nickel+quarter*Quarter
        print("-"*100)
        if money>=Cost.cost:
            print("Thanks for your order sir")
            if money==Cost.cost:
                self.profit+=Cost.cost
                return True
            elif money>Cost.cost:
                money-=Cost.cost
                self.profit+=Cost.cost
                print("Here's your change sir !",money)

                return True
        
        else:

            print("Sorry sir! you haven't given the enough money!!!")
            return False

    

            

        