# Create a "BankAccount" class to simulate basic banking operations.

# Requirements:

# - Define attributes for account number, account holder name, and balance.
# - Implement methods to deposit money, withdraw money, and check the current balance.
# - Prevent withdrawals that exceed the available balance.
# - Do not allow negative deposit or withdrawal amounts.
# - Create an object and demonstrate all the operations.


class BankAccount:
    def __init__(self,account_number , account_name , balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance 


    def deposit(self , amount):
            if amount <=0:
                print('The amount should be more than 0.')
                print("-" * 40)
            else:
                self.balance += amount 
                print(f'Deposited Amount: Rs {amount} | Total balance: Rs {self.balance}')
                print("-" * 40)

    def withdraw(self,amount):
            if amount<=0:
                print('The amount should be more than 0 to.')
                print("-" * 40)
            elif amount > self.balance:
                print('Insufficient balance. Please try again.')
                print("-" * 40)
            else:
                 self.balance -= amount
                 print(f'Withdrawn Amount: Rs {amount} | Total balance: Rs {self.balance}')
                 print("-" * 40)
                 
                 
    def check_balance(self):
            print("\n========================================")
            print('.                  BANKING REPORT    ')
            print(f'''
                  Account Number: {self.account_number} 
                  Account Name: {self.account_name}
                  Balance: Rs {self.balance}
                  ''')
            print("\n========================================")

account1 = BankAccount(account_number='100' , account_name='Sarwagya' , balance=500)


account1.deposit(100)
account1.withdraw(200)
account1.deposit(-90)
account1.withdraw(1000)
account1.check_balance()

