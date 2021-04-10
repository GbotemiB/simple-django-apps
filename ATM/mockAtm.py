#mock atm project
import datetime
import random

#sample data
database = {1111000001: ['Gbotemi', 'Bolarinwa', 'gbotemi@gmail.com', 'gbotemiPassword']}

def displayTime():
    #display time and date
    today = datetime.datetime.now()
    print (today.strftime("%B %d, %Y %H:%M:%S"))

def start():
    print("Welcome to Bank Dot")

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


def generateAccountNumber():
    return random.randrange(1111111111 - 999999999)


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

    

def login():
    
    userAccountNumber = int(input("Enter your Account Number \n"))

    #for accountNumber, userDetails in database.keys():
    if (userAccountNumber in list(database.keys())):
        
        trial = 3
        while trial >= 0:
            password = input("Enter password here: \n")

            if (password == database.get(userAccountNumber)[3]):
                print ("Login Successful \nWelcome %s" % database.get(userAccountNumber)[0])
                select = int(input("What would you like to do? \n 1: Withdrawal \n 2: Deposit \n 3: Complaint \n 4: Logout \n 5: Exit \n"))
                bankOperation(select)
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
                
    else:
        print("Check if Account number is correct")
        login()


def bankOperation(option):
    #result of choosing option 1 or 2 or 3
    if option == 1:
        acctBalance = int(input("How much will you like to withdraw: "))
        print ("Take your cash")
    elif option == 2:
        acctBalance = int(input("How much would you like to deposit? "))
        print ("Your current balance is", acctBalance)
    elif option == 3:
        isSue = input("What issue will you like to report? \n")
        print ("Thank you for contacting us")
    elif option == 4:
        logOut()
    elif option == 5:
        exitBank()
    else:
        print("Please choose from the listed options")

def complaint():
    pass


def deposit():
    pass

def withdrawal():
    acctBalance = int(input("How much will you like to withdraw: \n")) 
    database['']
    print ("Take your cash")

def logOut():
    print("You have successfully been logged out \n******************************\nEnter you details to Login\n******************************\n ")
    login()

def exitBank():
    print("Goodbye, thank you for banking with us.")
    exit()


#TODO handle error with strings


start()
