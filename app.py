import customtkinter

app = customtkinter.CTk()

class Application(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.app = app 
        self.screen()
        self.frames()
        self.labels()
        self.inputs()
        self.buttons()
        app.mainloop()

    def screen(self):
        self.app.geometry("1080x720")
        self.app.resizable(True, True)
        self.app.title("Manager Store")

    def frames(self):
        self.top_container = customtkinter.CTkFrame(self, bg_color="#fff").place(relx=0.10, rely=0.10, relwidth=0.96, relheight=0.46)

    def labels(self):
        self.name_label = customtkinter.CTkLabel(master=self.top_container, text="Nome")
        self.name_label.place(relx=0.02, rely=0.02, relwidth=0.20, relheight=0.10)

        self.cpf_label = customtkinter.CTkLabel(master=self.top_container, text="CPF")
        self.cpf_label.place(relx=0.51, rely=0.02, relwidth=0.20, relheight=0.10)

        self.cep_label = customtkinter.CTkLabel(master=self.top_container, text="CEP")
        self.cep_label.place(relx=0.02, rely=0.2, relwidth=0.20, relheight=0.10)

        self.phone_label = customtkinter.CTkLabel(master=self.top_container, text="Telefone")
        self.phone_label.place(relx=0.52, rely=0.2, relwidth=0.20, relheight=0.10)

    def inputs(self):
        self.name_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8)
        self.name_input.place(relx=0.10, rely=0.12, relwidth=0.30, relheight=0.05)

        self.cpf_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8)
        self.cpf_input.place(relx=0.60, rely=0.12, relwidth=0.30, relheight=0.05)

        self.cep_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8)
        self.cep_input.place(relx=0.10, rely=0.30, relwidth=0.30, relheight=0.05)

        self.phone_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8)
        self.phone_input.place(relx=0.60, rely=0.30, relwidth=0.30, relheight=0.05 )

    def buttons(self):
        self.register_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Cadastrar")
        self.register_button.place(relx=0.15, rely=0.40, relwidth=0.10, relheight=0.05)

        self.update_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Atualizar")
        self.update_button.place(relx=0.35, rely=0.40, relwidth=0.10, relheight=0.05)

        self.delete_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Deletar", fg_color="#ec5353")
        self.delete_button.place(relx=0.55, rely=0.40, relwidth=0.10, relheight=0.05)

        self.clear_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Limpar")
        self.clear_button.place(relx=0.75, rely=0.40, relwidth=0.10, relheight=0.05)

Application()