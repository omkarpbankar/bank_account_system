class BankAccount:
    bank_name = "Default Bank"
    total_accounts = 0

    def __init__(self, holder_name, account_number, balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance
        BankAccount.total_accounts += 1

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
            return True
        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            return True
        print("Insufficient funds! Cannot withdraw more than available balance.")
        return False

    def check_balance(self):
        return self.balance

    def display_account_details(self):
        print("--------------------------")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print("--------------------------")

if __name__ == "__main__":
    # Test the class
    acc1 = BankAccount("Alice Smith", "1001", 500)
    acc2 = BankAccount("Bob Johnson", "1002", 1500)

    print(f"Total Accounts Created: {BankAccount.total_accounts}")

    acc1.display_account_details()
    
    # Test Deposit
    acc1.deposit(200)
    
    # Test Withdrawal (valid)
    acc1.withdraw(100)
    
    # Test Withdrawal (invalid - insufficient funds)
    acc1.withdraw(1000)

    # Change bank name for all accounts
    BankAccount.change_bank_name("Global Trust Bank")
    
    acc2.display_account_details()
