""" 
    A mock Atm Project that performs the basic operations in a bank
 """

#import methods to be used 
import datetime
import random

#sample data
database = {1111000001: ['Gbotemi', 'Bolarinwa', 'gbotemi@gmail.com', 'gbotemiPassword']}

#timestamp for login
def displayTime():
    #display time and date
    today = datetime.datetime.now()
    print (today.strftime("%B %d, %Y %H:%M:%S"))

# to begin operations in the bank
def start():
    print("Welcome to Bank Dot")
    displayTime()
    
    isOptionCorrect = False

    while (isOptionCorrect == False):

        welcome = int(input("Do you have an account with us? 1 (Yes) 2 (No) \n"))
        if welcome == 2:
            signUp()
            isOptionCorrect = True

        elif welcome == 1:
            login()
            isOptionCorrect = True

        else:
            print("Invalid option")

#generating Account number for new Users
def generateAccountNumber():
    return random.randrange(1111111111 - 999999999)

#operation to sign up
def signUp():
    firstName = input("Enter Firstname \n")
    surName = input("Enter Surname \n")
    newEmail = input("Enter new email \n")
    newPassword = input("Enter new password \n")
    accountNumber = generateAccountNumber()
    
    database[accountNumber] = [ firstName, surName, newEmail, newPassword]

    
    print("you have successfully signed up")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("************* WELCOME **************")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your Account number is %d" % accountNumber)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   
    
    return login()

    
#login function for users
def login():
    
    

    #for accountNumber, userDetails in database.keys():
    accountTrial = 2
    while accountTrial >= 0:
        userAccountNumber = int(input("Enter your Account Number \n"))
        if (userAccountNumber in list(database.keys())):
            
            trial = 3
            while trial >= 0:
                password = input("Enter password here: \n")

                if (password == database.get(userAccountNumber)[3]):
                    print ("Login Successful \nWelcome %s" % database.get(userAccountNumber)[0])
                    bankOperation()
                elif (trial != 0):
                    print ("wrong password, try again. you have %d more trials" % trial)
                    trial -= 1
                else:
                    print("You have exceeded the number of tries. Select the following options 1 (Forgot Password) 2 (Exit)")
                    select = int(input(""))
                    if (select == 1):
                        forgotPassword()
                    elif (select == 2):
                        exitBank()
                    else:
                        print("Invalid option")
        elif (accountTrial != 0):
            accountTrial -= 1
            print("Check if Account number is correct")
            

        else:
            print("You have exceeded the number of tries to attempt account number. \n Please kindly reach out to us on 080112331231")
            exit()


#bank operations to be performed
def bankOperation():
    select = int(input("What would you like to do? \n 1: Withdrawal \n 2: Deposit \n 3: Complaint \n 4: Logout \n 5: Exit \n"))
                
    #result of choosing option 1 or 2 or 3
    if select == 1:
        withdrawal()
    elif select == 2:
        deposit()
    elif select == 3:
        complaint()
    elif select == 4:
        logOut()
    elif select == 5:
        exitBank()
    else:
        print("Please choose from the listed options")


#complaints function for complaints
def complaint():
    isSue = input("What issue will you like to report? \n")
    print ("Thank you for contacting us")
    bankOperation()


#functions for depositing into the bank
def deposit():
    acctBalance = int(input("How much would you like to deposit? "))
    print ("Your current balance is", acctBalance)
    bankOperation()


#withdrawal functions for users
def withdrawal():
    acctBalance = int(input("How much will you like to withdraw: \n")) 
    print ("Take your cash")
    bankOperation()


#log out functions to log out of the bank app
def logOut():
    print("You have successfully been logged out \n******************************\nEnter you details to Login\n******************************\n ")
    exit()


#exit functions to exit the app
def exitBank():
    print("Goodbye, thank you for banking with us.")
    exit()


#TODO handle error with strings


start()
