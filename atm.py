class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balance_check(self):
        print("Your balance is 50,000")
    
    def withdraw(self,amount):
        new_amount = 50000 - amount
        print("You have Withdrawn "+str(amount)+" Your remaining amount is"+str(new_amount))

def main():
    card_number = input("Insert card number ")
    pin_number = input("Enter your pin number")

    new_user = Atm(card_number,pin_number)

    print("Choose the options")
    print("1. BALANCE ENQUIRY    2. WITHDRAWL")

    options= int(input("enter the option number "))

    if (options == 1):
        new_user.balance_check()

    elif(options == 2):
        amount = int(input("enter the amount "))
        new_user.withdraw(amount)

    else:
        print("Please enter the valid number")

if __name__=="__main__":
    main()