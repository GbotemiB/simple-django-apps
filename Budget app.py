


class Budget:
    

    def __init__(self, category):

        cash = 0

        self.category = category
        self.cash = cash 
    
    def withdraw(self, amount):
        self.cash -= amount
        return (f"Amount withdrawn from {self.category} budget is {self.cash}")

    
    def deposit(self, amount):
        self.cash += amount
        return (f"Amount deposited into {self.category} budget is {self.cash}")


    def categoryBalances(self):
        return (f"Amount left in {self.category} budget is {self.cash}")
        

    def transferBalance():
        pass


categoryOne = Budget('Food')
categoryTwo = Budget('Clothing')
print(categoryOne.deposit(3000))
print(categoryOne.withdraw(2000))
print(categoryOne.categoryBalances())

print(categoryTwo.deposit(10000))
print(categoryTwo.withdraw(1500))
print(categoryTwo.categoryBalances())


