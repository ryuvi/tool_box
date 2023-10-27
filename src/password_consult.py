import customtkinter as ctk
import tkinter as tk
import pyperclip as pc
import dbqueries as db

class Password_Consulter(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.title("Password Consulter")
        self.rowconfigure(0, weight=1)
        self.lpanel = ctk.CTkFrame(self)
        self.pack(side=tk.LEFT)
        
    def left_panel(self):
        self.entry = ctk.CTkEntry(self.lpanel, placeholder_text="Password Title")
        self.entry.pack(padx=10, pady=10)
        self.search = ctk.CTkButton(self.lpanel, text="Search", command=take_passwd)
        self.search.pack(padx=10, pady=10)
        


    def right_panel(self):
        pass


