
database = {"food":2000}

class Budget:

    def __init__(self, category):
        #initialise cash to 0
        cash = 0

        self.category = category
        self.cash = cash 
    
    def withdraw(self, amount):
        self.cash -= amount
        return (f"Amount withdrawn from {self.category} budget is {self.cash}")

    
    def deposit(self, categoryName, amount):
        amountInStock = database[categoryName]
        amountInStock += amount
        #return (f"Amount deposited into {self.category} budget is {self.cash}")


    def categoryBalances(self):
        return (f"Amount left in {self.category} budget is {self.cash}")
        

    def transferBalance(self, database, category1, amount, category2):
        withdrawn = database[category1]
        sent = database[category2]

        database[category1] = withdrawn - amount
        database[category2] = sent + amount
        return database

    def newCategory(createCategory):
        createBudgetAmount = int(input("Please Deposit any amount into your Category \n"))
        database[createCategory] = createBudgetAmount
        print (database)
    

    
def start():
    print ("Welcome to the Budget App")
    print ("=============================")
   
    todo = int(input("What will you like to do \n(1) Create a new budget category \n(2) Deposit funds into a Budget \n(3) Withdraw funds from a budget \n(4) See budget balances \n(5) Transfer balance between budget \n"))
    if (todo == 1):
        createBudget()
        start()
    elif todo == 2:
        depositFunds()
        start()
    elif todo == 3:
        Budget.withdraw()
    elif todo == 4:
        Budget.categoryBalances()
    elif todo == 5:
        Budget.transferBalance()
    else:
        print ("Invalid option, please try again")
        start()

def createBudget():
    name = input("please enter category name\n")
    if name not in database.keys():
        Budget.newCategory(name)
    else:
        print("Category already exists, try again.")
        createBudget()

def depositFunds():
    category = input("what is the name of the category you want to deposit funds into? \n")
    if category in database.keys():
        amount = int(input("How much will you like to deposit? \n"))
        Budget.deposit(category, amount)




start()
