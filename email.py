import re

class Email:

    def __init__(self, email):
        self.email = email

    def validate_email(self):
        self.__email_pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        self.email_is_truth =  re.match(self.__email_pattern, self.email)
        if not self.email_is_truth:
            return False
        else:
            return True

if __name__ == "main":
    Email()