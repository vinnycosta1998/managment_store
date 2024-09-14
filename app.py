import customtkinter
from tkinter import ttk, messagebox 
import sqlite3
import cpf
import phone
import email

app = customtkinter.CTk()
    
class AppFunctions():
    def clean_inputs(self):
        self.name_input.delete("0.0", "end")
        self.cpf_input.delete("0.0", "end")
        self.email_input.delete("0.0", "end")
        self.phone_input.delete("0.0", "end")

    def connect_database(self):
        self.connection = sqlite3.connect("clients.bd")
        self.cursor = self.connection.cursor()
    
    def disconnect_database(self):
        self.connection.close()
        print("disconected database")

    def create_tables(self):
        self.connect_database()
        print("Conecting a database...")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS CLIENTS(
                ID INTEGER PRIMARY KEY,
                NAME VARCHAR(40) NOT NULL,
                CPF CHAR(11) UNIQUE,
                EMAIL VARCHAR(40) NOT NULL UNIQUE,
                PHONE CHAR(12) NOT NULL UNIQUE       
            );
        """)
        self.connection.commit()
        print("Database created")
        self.list_clients()


    def insert_client(self):
        self.name = self.name_input.get("1.0", "end")
        self.cpf = self.cpf_input.get("1.0", "end")
        self.email = self.email_input.get("1.0", "end")
        self.phone = self.phone_input.get("1.0", "end")
        
        self.cpf_verify = cpf.CPF(self.cpf)
        self.cpf_is_truth = self.cpf_verify.verify_cpf()

        self.email_verify = email.Email(self.email)
        self.email_is_truth = self.email_verify.validate_email()
        
        self.phone_verify = phone.Phone(self.phone)
        self.phone_is_truth = self.phone_verify.validate_phone_number()
        print(self.cpf_is_truth, self.email_is_truth, self.phone_is_truth)
        
        if self.cpf_is_truth and self.email_is_truth and self.phone_is_truth:
            self.cursor.execute("""
                INSERT INTO CLIENTS (NAME, CPF, EMAIL, PHONE)
                VALUES (?, ?, ?, ?)
            """, (self.name, self.cpf, self.email, self.phone))
            self.connection.commit()
            self.clean_inputs()
            self.disconnect_database()
            self.connect_database()
        else:
            messagebox.showwarning(title="input invalid", message="CPF, Email, ou Numero de telefone invalidos")

    def list_clients(self):
        self.listView.delete(*self.listView.get_children())
        self.connect_database()
        self.list = self.cursor.execute("""
            SELECT NAME, CPF, EMAIL, PHONE FROM CLIENTS
            ORDER BY NAME ASC;       
        """)

        for index in self.list:
            self.listView.insert("", "end", values=index)

    def onDoubleClick(self, event):
        self.clean_inputs()
        self.listView.selection()

        for i in self.listView.selection():
            col1, col2, col3, col4 = self.listView.item(i, 'values')
            self.name_input.insert("end", col1)
            self.cpf_input.insert("end", col2)
            self.email_input.insert("end", col3)
            self.phone_input.insert("end", col4)

    
class Application(customtkinter.CTk, AppFunctions):
    def __init__(self):
        super().__init__()
        self.app = app 
        self.screen()
        self.frames()
        self.labels()
        self.inputs()
        self.buttons()
        self.treeview()
        self.create_tables()
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

        self.email_label = customtkinter.CTkLabel(master=self.top_container, text="Email",)
        self.email_label.place(relx=0.02, rely=0.2, relwidth=0.20, relheight=0.10)

        self.phone_label = customtkinter.CTkLabel(master=self.top_container, text="Telefone")
        self.phone_label.place(relx=0.52, rely=0.2, relwidth=0.20, relheight=0.10)

    def inputs(self):
        self.name_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8, activate_scrollbars=False)
        self.name_input.place(relx=0.10, rely=0.12, relwidth=0.30, relheight=0.05)

        self.cpf_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8, activate_scrollbars=False)
        self.cpf_input.place(relx=0.60, rely=0.12, relwidth=0.30, relheight=0.05)

        self.email_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8, activate_scrollbars=False)
        self.email_input.place(relx=0.10, rely=0.30, relwidth=0.30, relheight=0.05)

        self.phone_input = customtkinter.CTkTextbox(master=self.top_container, width=30, height=20, corner_radius=8, activate_scrollbars=False)
        self.phone_input.place(relx=0.60, rely=0.30, relwidth=0.30, relheight=0.05 )

    def buttons(self):
        self.register_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Cadastrar", command=self.insert_client)
        self.register_button.place(relx=0.15, rely=0.40, relwidth=0.10, relheight=0.05)

        self.update_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Atualizar")
        self.update_button.place(relx=0.30, rely=0.40, relwidth=0.10, relheight=0.05)

        self.delete_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Deletar", fg_color="#ec5353", command=self.delete_client)
        self.delete_button.place(relx=0.45, rely=0.40, relwidth=0.10, relheight=0.05)

        self.clear_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Limpar", command=self.clean_inputs)
        self.clear_button.place(relx=0.60, rely=0.40, relwidth=0.10, relheight=0.05)

        self.search_button = customtkinter.CTkButton(master=self.top_container, width=0.10, height=0.05, corner_radius=16, text="Buscar")
        self.search_button.place(relx=0.75, rely=0.40, relwidth=0.10, relheight=0.05)

    def treeview(self):
        self.listView = ttk.Treeview(self.bottom_container, height=3, column=("Nome", "CPF", "Email", "Telefone"))
        self.listView.heading("#0", text="")
        self.listView.heading("#1", text="Nome")
        self.listView.heading("#2", text="CPF")
        self.listView.heading("#3", text="Email")
        self.listView.heading("#4", text="Telefone")

        self.listView.column("#0", width=1)
        self.listView.column("#1", width=40)
        self.listView.column("#2", width=40)
        self.listView.column("#3", width=40)
        self.listView.bind("<Double-1>", self.onDoubleClick)

        self.listView.place(relx=0.05, rely=0.60, relwidth=0.90, relheight=0.36)

Application()