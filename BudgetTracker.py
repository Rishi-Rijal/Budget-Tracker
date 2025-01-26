from email_validator import validate_email, EmailNotValidError
class Person:

    # validate the email using python email_validator
    @staticmethod
    def is_valid_email(email):
        try:
            # Validate email
            validate_email(email)
            return True
        except EmailNotValidError as e:
            print(f"Invalid email: {e}")
            return False

    #creating a new object of person class with name and email
    def __init__(self, name, email):
        if not self.is_valid_email(email):
            print("Enter a Valid email address")
            return
        self._name = name
        self._email = email
        # initializing budget accounts to empty list to add accounts
        self._budget_accounts = []
        print("Object Created Successfully")
    
    def get_info(self):
        print(f"name: {self._name} Email: {self._email}")

    # method to change the person name
    def change_name(self, new_name):
        if new_name != self._name:
            self._name = new_name
        else:
            print("You already have that name")

    #method to change the email afterwards
    def change_email(self, new_email):
        if not self.is_valid_email(new_email):
            print("Invalid email, cannot update.")
            return
        if new_email != self._email:
            self._email = new_email
            print("Email updated successfully.")
        else:
            print("This email is already set.")
    
    # add budget account
    def add_budget_account(self, budget_account):
        if budget_account not in self._budget_accounts:
            self._budget_accounts.append(budget_account)
            print("Budget Account added successfully")
        
        else:
            print("Budget Account already exists")
    
    # remove budget account
    def remove_budget_account(self, budget_account):
        if budget_account not in self._budget_accounts:
            print(f"There is not budget Account with the name {budget_account}")
        else:
            self._budget_accounts.remove(budget_account)
            print("Removed account Successfully")




class BudgetAccount:
    def __init__(self, acc_name):
        self._acc_name = acc_name
        self._transactions = []
        print("Budget Account Created Successfully")
    
    # method to add transaction to the account:
    def add_transaction(self, transaction):
        self._transactions.append(transaction)
        print("Transaction added successfully")
    
    # method to remove transaction from the account
    def remove_transaction(self, transaction):
        if transaction not in self._transactions:
            print("Transaction does not exist")
        else:
            self._transactions.remove(transaction)
            print("Transaction removed successfully")
    
    # method to get all transactions
    def get_transactions(self):
        for transaction in self._transactions:
            print(transaction)


class Transction():
    def __init__(self, amount, type, description):
        self._amount = amount
        self._type = type
        self._description = description
        print("Transaction created successfully")

        