class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.phone_number_digits_list = []
        self.format_phone_number()
        self.validate_phone_number()
        self.verify_phone_number()
            
    def format_phone_number(self):
        self.phone_number = self.phone_number.replace("(", "").replace(")", "").replace("-", "")

    def validate_phone_number(self):
        self.phone_number_list = list(self.phone_number)
        for i in range(0, len(self.phone_number_list)):
            try:
                self.phone_number_list[i] = int(self.phone_number_list[i])
                if type(i) == int:
                    self.phone_number_digits_list.append(True)
                print(self.phone_number_digits_list)
            except ValueError:
                raise ValueError("phone number invalid")
        
            
    def verify_phone_number(self):
        return all(self.phone_number_digits_list)
                
if __name__ == "__main__":
    Phone()

