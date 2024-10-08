class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.phone_number_digits_list = []
        self.format_phone_number()
        self.clean_list()
            
    def format_phone_number(self):
        self.phone_number = self.phone_number.replace("(", "").replace(")", "").replace("-", "")
        self.validate_phone_number()

    def validate_phone_number(self):
        self.phone_number_list = list(self.phone_number)
        for i in range(0, len(self.phone_number_list) - 1):
            try:
                self.phone_number_list[i] = int(self.phone_number_list[i])
                if type(i) == int:
                    self.phone_number_digits_list.append(True)
            except ValueError:
                raise ValueError("phone number invalid")
        return all(self.phone_number_digits_list)
        
    def clean_list(self):
        self.phone_number_digits_list.clear
                
if __name__ == "__main__":
    Phone()

