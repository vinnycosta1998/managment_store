import customtkinter
from tkinter import ttk

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
        self.treeview()
        app.mainloop()

    def screen(self):
        self.app.geometry("1080x720")
        self.app.resizable(True, True)
        self.app.title("Manager Store")

    def frames(self):
        self.top_container = customtkinter.CTkFrame(self).place(relx=0.10, rely=0.10, relwidth=0.96, relheight=0.46)
        self.bottom_container = customtkinter.CTkFrame(self).place(relx=0.10, rely=0.60, relwidth=0.96, relheight=0.46)

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
    
    def treeview(self):
        self.listView = ttk.Treeview(self.bottom_container, height=3, column=("Nome", "CPF", "CEP", "Telefone", "Cidade", "Bairro", "Rua"))
        self.listView.heading("#0", text="")
        self.listView.heading("#1", text="Nome")
        self.listView.heading("#2", text="CPF")
        self.listView.heading("#3", text="CEP")
        self.listView.heading("#4", text="Telefone")
        self.listView.heading("#5", text="Cidade")
        self.listView.heading("#6", text="Bairro")
        self.listView.heading("#7", text="Rua")

        self.listView.column("#0", width=1)
        self.listView.column("#1", width=40)
        self.listView.column("#2", width=40)
        self.listView.column("#3", width=40)
        self.listView.column("#4", width=40)
        self.listView.column("#5", width=40)
        self.listView.column("#6", width=40)
        self.listView.column("#7", width=40)

        self.listView.place(relx=0.05, rely=0.60, relwidth=0.90, relheight=0.36)

Application()