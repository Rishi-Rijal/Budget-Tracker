from email_validator import validate_email, EmailNotValidError

class Person:
    @staticmethod
    def is_valid_email(email):
        try:
            # Validate email
            validate_email(email)
            return True
        except EmailNotValidError as e:
            print(f"Invalid email: {e}")
            return False

    def __init__(self, name, email):
        if not self.is_valid_email(email):
            raise ValueError("Cannot create Person object: Invalid email address.")
        self._name = name
        self._email = email

    def change_name(self, new_name):
        if new_name != self._name:
            self._name = new_name
        else:
            print("You already have that name")

    def change_email(self, new_email):
        if not self.is_valid_email(new_email):
            print("Invalid email, cannot update.")
            return
        if new_email != self._email:
            self._email = new_email
            print("Email updated successfully.")
        else:
            print("This email is already set.")

# Example Usage
try:
    person = Person("John Doe", "example@rishi.com")
    print(f"Person created: {person._name}, {person._email}")
except ValueError as e:
    print(e)

# Attempting to create a person with an invalid email
try:
    invalid_person = Person("Jane Doe", "invalid-email")
except ValueError as e:
    print(e)
