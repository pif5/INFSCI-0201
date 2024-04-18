import json

class Customer:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        # Convert the object into a dictionary 
        customer_dict = {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        # make it to string
        return json.dumps(customer_dict, indent=2)

    
john = Customer(1, "John", "Smith")

# Print the JSON representation of the object
print(john.to_json())


class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        account_dict = {
            'account_id': self.account_id,
            'balance': self.balance
        }
     
        return json.dumps(account_dict, indent=4)  
# Instantiate 
john_account = Account(1, 5000)
print(john_account.to_json())




class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
        else:
            raise ValueError("add_customer expects a Customer instance")

    def remove_customer(self, user_id):
        self.customers = [customer for customer in self.customers if customer.user_id != user_id]

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:
            raise ValueError("add_account expects an Account instance")

    def remove_account(self, account_id):
        self.accounts = [account for account in self.accounts if account.account_id != account_id]

    def to_json(self):
        
        customers_json = [json.loads(customer.to_json()) for customer in self.customers]
        accounts_json = [json.loads(account.to_json()) for account in self.accounts]
        bank_dict = {
            'customers': customers_json,
            'accounts': accounts_json
        }
        return json.dumps(bank_dict, indent=2)
    
    
    # Instantiate Bank
the_bank = Bank()

# Existing customer and account
john = Customer(1, "John", "Smith")
john_account = Account(1, 5000)

# Add customer and account to the bank
the_bank.add_customer(john)
the_bank.add_customer(Customer(2, "Jane", "Doe"))
the_bank.add_account(john_account)

# Print the JSON representation of the bank
print(the_bank.to_json())