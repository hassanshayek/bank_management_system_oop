class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.transaction_history = []


class Bank:
    def __init__(self):
        self.all_accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.is_loan_enabled = True

    def create_account(self, username, password):
        new_user = Account(username, password)
        self.all_accounts.append(new_user)
        print("Account created successfully.")

    def show_accounts(self):
        for account in self.all_accounts:
            print('Username:', account.username, 'Balance:', account.balance)

    def deposit(self, username, amount):
        account = self.find_account(username)
        if account:
            account.balance += amount
            self.total_balance += amount
            account.transaction_history.append(f"Deposited {amount} taka")
            print(f"Deposited {amount} taka successfully.")
        else:
            print("Account not found.")

    def withdraw(self, username, amount):
        account = self.find_account(username)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                self.total_balance -= amount
                account.transaction_history.append(f"Withdraw {amount} taka")
                print(f"Withdraw {amount} taka successfully.")
            else:
                print("Not enough money!")
        else:
            print("Account not found.")

    def transfer(self, sender_name, receiver_name, amount):
        sender_account = self.find_account(sender_name)
        receiver_account = self.find_account(receiver_name)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                sender_account.transaction_history.append(
                    f"Transferred {amount} taka to {receiver_account.username}")
                receiver_account.transaction_history.append(
                    f"Received {amount} taka from {sender_account.username}")
                print(f"Transferred {amount} taka successfully.")
            else:
                print("Not enough money!")
        else:
            print("Accounts not found.")

    def check_balance(self, username):
        account = self.find_account(username)
        if account:
            return account.balance
        else:
            print("Account not found.")

    def check_transaction_history(self, username):
        account = self.find_account(username)
        if account:
            for transaction in account.transaction_history:
                print(transaction)
        else:
            print("Account not found.")

    def take_loan(self, username):
        if self.is_loan_enabled:
            account = self.find_account(username)
            if account:
                loan_amount = account.balance * 2
                account.balance += loan_amount
                self.total_loan_amount += loan_amount
                account.transaction_history.append(
                    f"Received a loan of {loan_amount} taka")
                print(f"Received a loan of {loan_amount} taka.")
            else:
                print("Account not found.")
        else:
            print("Loan feature is currently disabled.")

    def check_total_balance(self):
        return self.total_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.is_loan_enabled = True
        print("Loan feature is enabled.")

    def disable_loan_feature(self):
        self.is_loan_enabled = False
        print("Loan feature is disabled.")

    def find_account(self, username):
        for account in self.all_accounts:
            if account.username == username:
                return account
        return None


janata = Bank()
admin_name = "admin"
admin_password = "123"

while True:
    print("1. Admin Login")
    print("2. User Registration")
    print("3. User Login")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter admin name: ")
        password = input("Enter admin password: ")
        if name == admin_name and password == admin_password:
            while True:
                print("\nAdmin Menu")
                print("1. Create Account")
                print("2. Check Total Balance")
                print("3. Check Total Loan Amount")
                print("4. Enable Loan Feature")
                print("5. Disable Loan Feature")
                print("6. Logout")
                admin_choice = int(input("Enter your choice: "))

                if admin_choice == 1:
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    janata.create_account(username, password)
                elif admin_choice == 2:
                    total_balance = janata.check_total_balance()
                    print(f"Total balance in the bank: {total_balance} taka")
                elif admin_choice == 3:
                    total_loan_amount = janata.check_total_loan_amount()
                    print(
                        f"Total loan amount in the bank: {total_loan_amount} taka")
                elif admin_choice == 4:
                    janata.enable_loan_feature()
                elif admin_choice == 5:
                    janata.disable_loan_feature()
                elif admin_choice == 6:
                    break
                else:
                    print("Invalid choice, Try again.")
        else:
            print("Invalid admin.")

    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        janata.create_account(username, password)

    elif choice == 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        account = janata.find_account(username)
        if account and account.password == password:
            while True:
                print("\nUser Menu")
                print("1. Deposit Amount")
                print("2. Withdraw Amount")
                print("3. Check Available Balance")
                print("4. Transfer Amount")
                print("5. Check Transaction History")
                print("6. Take Loan")
                print("7. Logout")
                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    amount = int(input("Enter the amount to deposit: "))
                    janata.deposit(username, amount)
                elif user_choice == 2:
                    amount = int(input("Enter the amount to withdraw: "))
                    janata.withdraw(username, amount)
                elif user_choice == 3:
                    balance = janata.check_balance(username)
                    if balance is not None:
                        print(f"Available balance: {balance} taka")
                elif user_choice == 4:
                    receiver_name = input("Enter recipient username: ")
                    amount = int(input("Enter the amount to transfer: "))
                    janata.transfer(username, receiver_name, amount)
                elif user_choice == 5:
                    janata.check_transaction_history(username)
                elif user_choice == 6:
                    janata.take_loan(username)
                elif user_choice == 7:
                    break
                else:
                    print("Invalid choice, Try again.")
        else:
            print("Invalid username or password.")

    elif choice == 4:
        break
    else:
        print("Invalid choice, Try again.")
