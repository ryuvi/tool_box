import customtkinter as ctk
from tkinter import StringVar, IntVar
import src.password_generator as pg
import src.timestamp_converter as tc

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Vicente's Tools")
        self.geometry("500x300")
        self.height = 300
        self.width = 500

        self.password_generator = None
        self.pass_gen_button = ctk.CTkButton(self, text="Password Generator", command=self.open_password_generator)
        self.pass_gen_button.grid(row=0, column=0, padx=10, pady=10)
        # self.pass_gen_button.place(relx=(self.width/2), rely=(self.height/2))
        
        self.timestamp_converter = None
        self.timestamp_converter_button = ctk.CTkButton(self, text="Timestamp Converter", command=self.open_timestamp_converter)
        self.timestamp_converter_button.grid(row=1, column=0, padx=10, pady=10)
        # self.timestamp_converter_button.place(relx=(self.width/3), rely=(self.height/3))

        self.close_button = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.close_button.grid(row=2, column=0, padx=10, pady=10, sticky='swse')
        # self.close_button.place(relx=(self.width/2), rely=(self.height))

    def open_password_generator(self):
        if self.password_generator is None or not self.password_generator.winfo_exists():
            self.password_generator = pg.Password_Generator(self)
            self.password_generator.grab_set()
        else:
            self.password_generator.focus()

    def open_timestamp_converter(self):
        if self.timestamp_converter is None or not self.timestamp_converter.winfo_exists():
            self.timestamp_converter = tc.TimeStampConverter(self)
            self.timestamp_converter.grab_set()
        else:
            self.timestamp_converter.focus()


app = App()
app.mainloop()
