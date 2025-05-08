#Mini Banking Application Using Procedural Programming  
   
#Menu-Driven Interface################################################################################################################################## 
import random
def login():
        while True:
            print("______Mini Banking Application______")

            choice = input("Choose an option Admin or User: ")
            if choice == "1":
                Admin()   
                return  
            elif choice == "2":
                User()    
                return
            else:
                print("Invalid choice")  
    
def User():
    
# Login Bank System with Username and Password###########################################################################################################
    username="James"
    password="1357"
           
    input_user = input("Enter your username: ") 
    input_password = input("Enter your password: ")

    with open ("User.txt", "a") as file:
        file.write(f"{ input_user},{input_password}")

    if input_user == username and input_password == password:
        print("Login successful") 
        
        while True: 
            print("______Welcome to User Menu______")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Go back")
        
            choice = input("Choose an option: ")

            if choice == "1":
                create_account()

            elif choice == "2":
                deposit_money()

            elif choice == "3":
                withdraw_money()

            elif choice == "4":
                check_balance()

            elif choice == "5":
                view_transaction_history()

            elif choice == "6":
                print("Go back")
                login() 
                break 
                                    
            else:
                print("Invalid choice")  

    else: 
        print("Login failed") 
            

def Admin():
 
# Login Bank System with Admin Username and Password##################################################################################################### 
    Admin_username="Jack"
    Admin_password="12345"
    
    
    input_Admin = input("Enter your Admin_username: ") 
    input_password = input("Enter your password: ")

    with open ("Admin.txt", "a") as file:
            file.write(f"{ input_Admin},{input_password}")

    if input_Admin == Admin_username and input_password == Admin_password:
        print("Login successful")

        while True:   
              print("______Welcome to Admin Menu______")
              print("1. View all accounts")
              print("2. Delete an accounts")
              print("3. all accounts total balance")
              print("4. Exit")

              choice = input("Choose an option: ")

              if choice == "1":
                 View_all_accounts()

              elif choice == "2":
                   Delete_an_accounts()

              elif choice == "3":
                   all_accounts_total_balance()

              elif choice == "4":
                   print("Exit")
                   break   

              else:
                   print("Invalid choice")  

    else: 
        print("Login failed")

#########################################################################################################################################################      

        



 
# Dictionary to store accounts###########################################################################################################################
accounts={}
global amount

#Generate a unique account number
def generate_account_number():
    return random.randint(100,106) 

#Create a new bank account.
def create_account():
    account_number = generate_account_number()
    
    name = input("Enter account holder name: ")
    current_balance = float(input("Enter current_balance: "))
    
    if  current_balance < 0:
        print(" current_balance cannot be negative.")
        return
    
    accounts[account_number] = {"name":name, "balance":current_balance, "transactions":[]}
    accounts[account_number]["transactions"].append(f"account holder name: {name}")
    print(f"Account created successfully! Your account number is: {account_number} ")


#Deposit money
def deposit_money():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter deposit amount: "))
    
    if amount <= 0:
        print("Deposit amount must be positive.")
        return
    
    accounts[account_number]["balance"] += amount
    accounts[account_number]["transactions"].append(f"Deposited: {amount}")
   
    print(f"deposited successfully!")


#Withdraw money 
def withdraw_money():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter withdrawal amount: "))
    
    if amount <= 0 or amount > accounts[account_number]["balance"]:
        print("Invalid withdrawal amount.")
        return
    
    accounts[account_number]["balance"] -= amount
    accounts[account_number]["transactions"].append(f"Withdraw: {amount}")

    print(f"withdrawl successfully!")


#Check account balance.
def check_balance():
    account_number = int(input("Enter account number: "))
    print(f"Current balance: {accounts[account_number]['balance']}")


#View transaction history
def view_transaction_history():
    account_number = int(input("Enter account number: "))

    print("Transaction History:")
    
    for transaction in accounts[account_number]["transactions"]:
        print(transaction)


#View all accounts
def View_all_accounts():
    for account_number, name in accounts.items():

        print(f" Your account number is: {account_number} ")
        print(f"account holder name: {name}")
        print(f"Current balance: {accounts[account_number]['balance']}")

    
#All accounts total balance
def all_accounts_total_balance():
    balance =sum(account_number["balance"] for account_number in accounts.values())
    print(f"All accounts total balance: {balance}")  
    

# Delete an accounts
def Delete_an_accounts():
    account_number = int(input("Enter account number: "))

    del accounts[account_number]
    print(f"accounts  {account_number} Delete successfull!")


login()


    


    
    


