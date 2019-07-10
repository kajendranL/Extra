# ATM Process
password = 4321
chance = 3
balance = 5000.00
Contact = 9790857244
Transaction = []

while chance > 0:
    pin = int(input("Enter your passcode: "))
    if pin == password:
        print("Press 1 to display your balance: ")
        print("Press 2 to withdraw the amount: ")
        print("Press 3 to change your password: ")
        print("Press 4 to know your last 5 transactions: ")

        option = int(input("Enter your option: "))

        if option == 1:
            print("Your bank balance is:", balance)
            break

        elif option == 2:
            withdraw = int(input("Enter the amount: "))
            if withdraw > balance:
                print("You do not have suffecient funds")
                break
            balance = balance - withdraw
            Transaction = Transaction.append(balance)
            print("Amount withdrawn: ", withdraw)
            print("Your current balance is: ", balance)
            break

        elif option == 3:
            password = int(input("Please Enter your password: "))
            if password == pin:
                print("Your new password cannot be the recent one, please input the right password")
            print("Your password has been changed")
            break


            # how to find the last transactions?
        elif option == 4:
            print("Your last transactions are: ", Transaction)
            break
    else:
        chance = - 1
        print("Enter password again")

        if chance == 0:
            print("Your account is locked, please Contact your bank or wait for 30 minutes")
            break










