data = {'alpha': {'password': [1234],
                  'balance': [2000]
                  },
        'beta': {'password': [4321],
                 'balance': [2000]
                 },
        'gamma': {'password': [9876],
                  'balance': [5000]
                  },
        }

chance = 3
Transactions = []


while chance > 0:
    for i in data:
        Pin = int(input("Enter your ATM PIN: "))
        if Pin == data[i]['password'][-1]:
            # def option_menu():
            print("Welcome to the Bank")
            print()
            print("Your Transactions options are: ")
            print()
            print("To deposit amount, press 1 ")
            print("To withdraw the amount, press 2 ")
            print("To check your bank balance, press 3")
            print("To change your ATM Pin, press 4")
            print("To update your contact number, press 5 ")
            print("To quit, press 6 ")
            # return input("Chose your option")

            option = int(input("Enter yout option: "))


            if option == 2:
                withdraw = int(input("Enter the withdrwal amount:"))
                balance = data[i]['balance'][-1] - withdraw
                if withdraw >= balance:
                    print("You have insufficient funds")
                    break
                print("Amount withdrawn:", withdraw)
                print("Your current balance is:", balance)
                print("Thank you for banking with us")
                break

            if option == 3:
                print('Your current balance is:', data[i]['balance'][-1])
                break


            if option == 4:
                password = int(input("Enter new password"))
                if password == data[i]['password'][-1]:
                    print("Your new password can not be similar to recently used passwords")
                    break
                print("Your password has been changed")
                break

            if option == 5:  # yet to work on
                Transactions = data[i]['balance'][-1]
                print("your last 5 transactions are:", Transactions)
                break

        else:
            chance -= 1
            print("Enter the password again:")
            if chance == 0:
                print("Account Blocked, please contact your bank, or try again after 30 min")
            break









