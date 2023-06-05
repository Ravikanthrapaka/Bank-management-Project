#Bank management project
#AccountHolders,amount
#Account,withdraw,Deposit,Atm pin


AccountHolders = ['Ravikanth','James','Boss','balu','Rock']
AtmPins=['9898','2112','6776','1992','1111']
Balances=[30000, 20000, 50000, 1000, 5000]
Withdraw = 0
Deposit = 0
Balance = 0
counter_1=1
counter_2=5
i=0

while True:
    print("--------------------------------------")
    print("*****Welcome to All Indian Bank****")
    print("--------------------------------------")
    print("---> 1.) Open New Bank Account")
    print("---> 2.) Withdraw")
    print("---> 3.) Deposit")
    print("---> 4.) Check Your Balance")
    print("---> 5.) Exit")
    print("--------------------------------------")

    ChoiceNo = input("Enter above option you required:")
    if ChoiceNo =="1":
        print("You Selected: 1")
        no_of_customers = eval(input("No. of Accounts : "))
        i=i+no_of_customers

        if i>3:
            print("\n")
            print("You reached limit to take a account again")
            i = i - no_of_customers
        else:
            while counter_1 <=i:
                name=input("Enter Your name:")
                AccountHolders.append(name)
                Pin=str(input("Set your own PIN:"))
                AtmPins.append(Pin)
                Balance=0
                Deposit = eval(input("Enter amount to Deposit:"))
                Balance=Balance+Deposit
                Balances.append(Balance)
                print("\nName=", end=" ")
                print(AccountHolders[counter_2])
                print("Pin=", end=" ")
                print(AtmPins[counter_2])
                print("Balance", end=" ")
                print(Balances[counter_2],  end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour name is sucessfully Created")
                print("Your pin was generated")
                print("Your balance Will be Updated")
                print("***You New Account Sucessfully Opened*** ")
                print("\n")
                print("Please remember Your Name and Pin")
                print("========================================")
                # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("press Enter for back or menu")
    elif ChoiceNo == "2":
        j = 0
        print("you selected option 2")
        
        while j < 1:
            k = -1
            name = input("Enter Your Name : ")
            pin = input("Enter Your Pin : ")

            # AccountHolders list.
            while k < len(AccountHolders) - 1:
                k = k + 1
                # this checks pin and names
                if name == AccountHolders[k]:
                    if pin == AtmPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(Balances[k], end=" ")
                        print("-/Rs\n")
                        balance = (Balances[k])
                        withdrawal = eval(input("Enter Withdrawn Amount : "))
                        
                        if withdrawal > balance:
                            # This is deposit from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher amount because your Balance mentioned above is not enough : "))
                            # To update balnce
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n") # 1000-500=500
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            Balance[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            # Else condition above is towithdraw if balance is greater than the withdrw amt
                            balance = balance - withdrawal
                            #update balance
                            print("\n")
                            print("----Withdraw Successfull!----")
                            Balances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                # value is incorrect it use
                print("Your name or pin does not match please Check\n")
                break
            
        mainMenu = input("Press enter key for menu or back")
    elif ChoiceNo == "3":
        print("You Selected option:3")
        n = 0
        #name and pin incorrect
        while n < 1:
            k = -1
            name = input("Please Enter Your name : ")
            pin = input("Please Enter Your Pin : ")
            # To find correct user
            while k < len(AccountHolders) - 1:
                k = k + 1
                # To Find both the pin and the name is valid
                if name == AccountHolders[k]:
                    if pin == AtmPins[k]:
                        n = n + 1
                        # updatebalance
                        # the deposit is done
                        print("Your Current Balance: ", end=" ")
                        print(Balances[k], end=" ")
                        print("-/Rs")
                        balance = (Balances[k])
                        # deposit from the customer.
                        deposition = eval(input("Enter the amount to deposit : "))
                        balance = balance + deposition # 2+2=4
                        Balances[k] = balance
                        print("\n")
                        print("----Deposit is done sucessfully----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name or pin does not match!\n")
                break
            # help for go back or menu
        mainMenu = input("Press Enter for Exit or menu ")
    elif ChoiceNo == "4":
        print("You Selected Option:4")
        k = 0
        print("Customers and Account balance : ")
        print("\n")
        # keep running until all details are shown
        while k <= len(AccountHolders) - 1:
            print("->.Customer =", AccountHolders[k])
            print("->.Balance =", Balances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Press Enter to go back or exit ")
    elif ChoiceNo == "5":
        print("You Selected Option:5")
        print("\n")
        print("Thank you for using All Indian Bank")
        print("---------------------------------------")
        print("\n")
        
        break
    else:
        print("\n")
        print("Invalid option you selected")
        print("Try again!")
        mainMenu = input("Press Enter to go back or exit")

        

