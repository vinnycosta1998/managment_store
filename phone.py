class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.format_phone_number()
    
    def format_phone_number(self):
        self.phone_number = self.phone_number.replace("(", "").replace(")", "").replace("-", "")

    def verify_phone_number(self):
        self.phone_number_list = list(self.phone_number)
        print(self.phone_number_list)
        for i in range(0, len(self.phone_number_list)):
            try:
                self.phone_number_list[i] = int(self.phone_number_list[i])
                return True
            except ValueError:
                raise ValueError("phone number invalid")
                
if __name__ == "__main__":
    Phone()
