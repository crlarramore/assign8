import cgitb; cgitb.enable()
class BankAccount:
    def __init__(self, num, bal):
        self.accountNumber = num
        self.balance = float(bal)
        print("An account has been created")
        print("The account number is " + str(self.accountNumber))
        print("The account has a balance of $" + str(self.balance))

    def deposit(self):
        userDeposit = input("How much would you like to deposit? ")
        self.balance = self.balance + float(userDeposit)
        self.getBalance()

    def getBalance(self):
        print("The account balance is: $" + str(self.balance))

class CheckingAccount(BankAccount):
    def __init__(self, num, bal, fee, minBal):
        BankAccount.__init__(self, num, bal)
        self.accountFees = 5
        self.minimumBalance = 50
        print("This is a checking account")
        print("The account fee is $" + str(self.accountFees))
        print("The account minimum balance is $" + str(self.minimumBalance))

    def deductFees(self):
        print("Deducting fee of $5")
        print("Balance after fee is $" + (str(self.balance)-5))

    def checkMinimumBalance(self):
        print("Checking if account balance meets minimum balance. . .")
        print("")

        if float(self.balance) < self.minimumBalance:
            print("Account balance is below minimum allowed")
            print("You must deposit $" + str(self.minimumBalance - self.balance) + "to meet the minimum account balance")
            self.deposit()
            self.checkMinimumBalance()
        else:
            print("Account balance meets minimum requirements")

class SavingsAccount(BankAccount):
    def __init__(self, num, bal, interest_rate):
        BankAccount.__init__(self, num, bal)
        self.interest = .2
        print("This is a savings account")
        print("The interest rate is" + str(self.interest))

    def interestRate(self):
        print("Interest rate is 20%")
        print("Balance after accrued interest is $" + str(self.balance) * 1.2)
              
        
print("Welcome to Online Banking!")

try:
    flag1 = 0
    while flag1 == 0:
        print("")
        print("--Main Menu--")
        print("To open an pre-paid account, press 1")
        print("To exit the program, press 2")
        loop1 = input("")

        if loop1 == '1':
            flag2 = 0
            while flag2 == 0:
                flag2 = 1
                print("")
                print("--Account Creation--")
                print("To open a Pre-Paid Account, press 1")
                loop2 = input("")

                if loop2 == '1':
                    print("")
                    print("--Open an Pre-Paid account--")
                    print("Minimum Balance is $50.00")
                    print("Account Fees are $5.00")
                    checkingAccountNumber = input("Enter an Account Number: ")
                    checkingAccountBalance = input("Enter Account Balance: $")
                    print("Please wait while account is created. . .")
                    print("")
                    my_checkingAccount = CheckingAccount(checkingAccountNumber, checkingAccountBalance, 50.0, 5.0)
                    my_checkingAccount.checkMinimumBalance()
                    flag3 = 0
                    while flag3 == 0:
                        print("")
                        print("--My Pre-Paid Account--")
                        print("What would you like to do?")
                        print("To make a deposit, press 1")
                        print("To check your balance, press 2")
                        print("To go to the Main Menu, press 3")
                        loop3 = input("")

                        if loop3 =='1':
                            my_checkingAccount.deposit()

                        elif loop3 == '2':
                            my_checkingAccount.getBalance()
                        elif loop3 == '3':
                            print("Going to the Main Menu. . .")
                            flag3 = 1
                        else:
                            print("Invalid Entry")

                else:
                    print("Invalid Entry")
                    flag2 = 0

        elif loop1 == '2':
            print("Exiting program. . .")
            flag1 = 1
        else:
            print("Invalid Entry")
except:
    print("Command not recognized!")

    
                    

