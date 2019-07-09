data = {'alpha': {'password': [1234],
                  'balance': [2000]
                  },
        'beta': {'password': [4321],
                 'balance': [2000]
                 }
        }
chance = 3



while chance > 0 :
    name = input("Enter user name:")
    for i in data:
        if i == name:
            while chance > 0:
                code = int(input("Enter password: "))
                if code == data[i]['password'][-1]:
                    print("press 1 for checking the balance")
                    print("Press 2 for whithdrawing")
                    print("Press 3 to change the password")
                    print("press 4 to know last 5 Transactions")

                    option = int(input("Enter the option:"))
                    if option == 1:
                        print('Your current balance is:', data[i]['balance'][-1])
                        break
                    elif option == 2:
                        withdraw = int(input("Enter the withdrwal amount:"))
                        balance = data[i]['balance'][-1] - withdraw
                        if withdraw >= balance:
                            print("You have insufficient funds")
                            break
                        print("Amount withdrawn:", withdraw)
                        print("Your current balance is:", balance)
                        print("Thank you for banking with us")
                        break
                    elif option == 3:
                        password = int(input("Enter new password"))
                        if password == data[i]['password'][-1]:
                            print("Your new password can not be similar to recently used passwords")
                            break
                        print("Your password has been changed")
                        break

                    elif option == 4: #yet to work on
                        print ("your last 5 transactions are:",)
                else:
                    chance -= 1
                    print("Enter the password again:")
                    if chance == 0:
                        print("Account Blocked, please contact your bank, or try again after 30 min")
                    break
                if i != name:
                    print("Enter user name")
                    break






