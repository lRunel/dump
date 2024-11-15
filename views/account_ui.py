from services.account_manager import AccountManager
from services.transaction_manager import TransactionManager
from repositories.account_repository import AccountRepository
from repositories.User_repositary import UserRepository

class AccountUI():
    def start(self,user):
        while True:
            print("\nWelcome to Global Digital Bank")
            print("\nSelect an option")
            print("1. Open Account")
            print("2. Close Account")
            print("3. Withdraw Funds")
            print("4. Deposit Funds")
            print("5. Transfer Funds")
            print("9. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.open_account(user)
            elif choice == 2:
                self.close_account(user)
            elif choice == 3:
                self.withdraw_funds()
            elif choice == 4:
                self.deposit_funds()
            elif choice == 5:
                self.transfer_funds()
            elif choice == 9:
                break
            else:
                print("Invalid choice. Please try again")

    def open_account(self,user):
        account_type = input("Enter account type (savings/current): ").strip().lower()
        name = input("Enter your name: ")
        amount = float(input("Enter initial deposit amount: "))
        pin_number = int(input("Enter you pin number: "))
        privilege = input("Enter account privilege (PREMIUM/GOLD/SILVER): ").strip().upper()
        
        if account_type == "savings":
            date_of_birth = input("Enter your date of birth(YYYY-MM-DD): ")
            gender = input("Enter your gender (M/F): ")
            account = AccountManager().open_account(account_type, name = name,
                                                     balance = amount,date_of_birth = date_of_birth, 
                                                     gender = gender, pin_number = pin_number, 
                                                     privilege = privilege)
            user.useraccounts.append(account)
        
        elif account_type == "current":
            registration_number = input('Enter your registration number: ')
            website_url = input("Enter your website URL: ")
            account = AccountManager().open_account(account_type, name = name, 
                                                    balance = amount, registration_number = registration_number, 
                                                    website_url= website_url, pin_number=pin_number, 
                                                    privilege=privilege)
            user.useraccounts.append(account)
        else:
            print("Invalid account type. Please try again")
            return

        print(account_type.capitalize(), 'Account opened successfully. Account Number: ', account.account_number)
    
    def close_account(self,user):
        account_number = int(input("Enter your account number: "))
        account = next((acc for acc in AccountRepository.account if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().close_account(account)
                print("Account closed successfully")
                user.useraccounts.pop(account)
            except Exception as e:
                print("Error: ", e)
        else:
            print("Account Not Found. Please try again")

    def withdraw_funds(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input("Enter amount to withdraw: "))
        pin_number = int(input("Enter your pin number: "))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().withdraw(account, amount, pin_number)
                print("Amount withdrawed successfully")
            except Exception as e:
                print("Error: ", e)
        else:
            print("Account Not Found. Please try again")

    def deposit_funds(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input("Enter amount to deposit: "))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().deposit(account, amount)
                print("Amount deposited successfully")
            except Exception as e:
                print("Error: ", e)
        else:
            print("Account Not Found. Please try again")

    def transfer_funds(self):
        # Similar to other methods
        # Difference is need to take input of 2 account numbers
        # Need to Search for two accounts
        # Different Method needs to be called from AccountManeger()
        from_account_number = int(input('Enter your account number: '))
        to_account_number = int(input("Enter recipient account number: "))
        amount = float(input("Enter amount to tranfer: "))
        pin_number = int(input("Enter your pin number: "))
        
        from_account = next((acc for acc in AccountRepository.accounts if acc.account_number == from_account_number) , None)
        to_account = next((acc for acc in AccountRepository.accounts if acc.account_number == to_account_number), None)

        if from_account and to_account:
            try:
                AccountManager().transfer(from_account, to_account, amount, pin_number)
                print("Amount transferred successfully")
            except Exception as e:
                print("Error: ", e)
        else:
            print("One or Both Account(s) Not Found. Please try again")
    