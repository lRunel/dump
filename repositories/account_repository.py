class AccountRepository:
    #Class attribute to store all the elements
    accounts = []
    account_counter = 1000

    # 1. class-level access: classmethod can access and modify the class-level attributes
    # 2. Differences
    # a. class method takes cls as its first argument
    # b. Instance.regular method takes self as its first argument
    # c. static method takes neither cls nor self as its first argument

    #Method to generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter
    
    #Method to save Account
    @classmethod
    def save_account(cls, account):
        cls.accounts.append(account) 
    
    #Method to get all account
    def get_all_accounts(self):
        return self.account