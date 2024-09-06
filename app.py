import customtkinter

app = customtkinter.CTk()

class Application:
    def __init__(self):
        self.app = app 
        self.screen()
        app.mainloop()

    def screen(self):
        self.app.geometry("1920x1080")
        self.app.resizable(True, True)
        self.app.title("Manager Store")

Application()