#Mini Banking Application Using Procedural Programming  
   
#Menu-Driven Interface 
import random
choice = input("Choose an option: ")
if choice == "1":
   Admin()     
elif choice == "2":
  User()    
else:
    print("Invalid choice")  
    
          

def Admin():
    while True:
        # Login Bank System with Admin Username and Password 
        Admin_username="Jack"
        Admin_password="12345"
        input_user = input("Enter your Admin_username: ") 
        input_password = input("Enter your password: ")
        if input_user == Admin_username and input_password == Admin_password:
            print("Login successful") 
            Admin() 
        else: 
            print("Login failed")
            
        print("______Mini Banking Application______")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

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
            print("Exit")
            break
        else:
            print("Invalid choice")  

def User():
    while True:
        # Login Bank System with Username and Password
        username="kamal"
        password="1357"
        input_user = input("Enter your username: ") 
        input_password = input("Enter your password: ")
        if input_user == username and input_password == password:
            print("Login successful") 
            User() 
        else: 
            print("Login failed")
            print("______Mini Banking Application______")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Exit")

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
                print("Exit")
                break
            else:
                print("Invalid choice")  


 
# Dictionary to store accounts
accounts={}

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



          

        


# Login Bank System with Admin Username and Password
    

    
    

main()
