import customtkinter as ctk
import tkinter as tk
import string as stri
import random as rand
import pyperclip as pc
import dbqueries as db

class Password_Output(ctk.CTkToplevel):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = f'Your password is: {text}'

        self.label = ctk.CTkLabel(self, text=self.text)
        self.label.pack(expand=True, fill='both', padx=10, pady=10)
        self.label.configure(font=("Comic Sans MS", 20))
        self.button = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.button.pack(expand=True, fill='both', padx=10, pady=10)

class Password_Generator(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Generator")
        # self.geometry("800x600")

        self.label = ctk.CTkLabel(self, text="Password Generator")
        self.label.pack(padx=20, pady=20)

        self.title = ctk.CTkLabel(self, text="Password Title")
        self.title.pack(side="top")
        self.title_str = tk.StringVar(value="")
        self.title_entry = ctk.CTkEntry(self, textvariable=self.title_str)
        self.title_entry.pack(side="top")

        self.check_frame = ctk.CTkFrame(self)
        self.check_frame.pack(side="top", padx=10, pady=20, ipadx=10, ipady=10)
        self.number_str = tk.StringVar(value="on")
        self.number_check = ctk.CTkCheckBox(self.check_frame, text="Add Numbers", variable=self.number_str, onvalue="on", offvalue="off", command=self.change_number_state)
        self.number_check.pack(side="left", expand=True, fill='both')
        self.symbol_str = tk.StringVar(value="on")
        self.symbol_check = ctk.CTkCheckBox(self.check_frame, text="Add Symbols", variable=self.symbol_str, onvalue="on", offvalue="off", command=self.change_symbol_state)
        self.symbol_check.pack(side="left", expand=True, fill='both')
        self.capitalize_str = tk.StringVar(value="on")
        self.capitalize_check = ctk.CTkCheckBox(self.check_frame, text="Add Caps", variable=self.capitalize_str, onvalue="on", offvalue="off", command=self.change_capitalize_state)
        self.capitalize_check.pack(side="left", expand=True, fill='both')

        self.range_frame = ctk.CTkFrame(self)
        self.range_frame.pack(side="top", padx=10, pady=20, ipadx=10, ipady=10)
        self.range_one = ctk.CTkFrame(self.range_frame)
        self.range_one.pack(side="left", expand=True, fill='both')
        self.length_title = ctk.CTkLabel(self.range_one, text="Password Length")
        self.length_title.pack(expand=True, fill='both')
        self.length_var = tk.IntVar(value=8)
        self.length_slider = ctk.CTkSlider(self.range_one, from_=1, to=16, variable=self.length_var, command=self.update_length_value, number_of_steps=15)
        self.length_slider.pack(expand=True, fill='both')
        self.length_label = ctk.CTkLabel(self.range_one, text=self.length_var.get())
        self.length_label.pack(expand=True, fill='both')
        self.number_title = ctk.CTkLabel(self.range_one, text="Numbers Quantity")
        self.number_title.pack(expand=True, fill='both')
        self.number_var = tk.IntVar(value=3)
        self.number_slider = ctk.CTkSlider(self.range_one, from_=1, to=6, variable=self.number_var, command=self.update_number_value, number_of_steps=5)
        self.number_slider.pack(expand=True, fill='both')
        self.number_label = ctk.CTkLabel(self.range_one, text=self.number_var.get())
        self.number_label.pack(expand=True, fill='both')
        self.range_two = ctk.CTkFrame(self.range_frame)
        self.range_two.pack(side="right", expand=True, fill='both')
        self.symbol_title = ctk.CTkLabel(self.range_two, text="Symbols Quantity")
        self.symbol_title.pack(expand=True, fill='both')
        self.symbol_var = tk.IntVar(value=3)
        self.symbol_slider = ctk.CTkSlider(self.range_two, from_=1, to=6, variable=self.symbol_var, command=self.update_symbol_value, number_of_steps=5)
        self.symbol_slider.pack(expand=True, fill='both')
        self.symbol_label = ctk.CTkLabel(self.range_two, text=self.symbol_var.get())
        self.symbol_label.pack(expand=True, fill='both')
        self.caps_title = ctk.CTkLabel(self.range_two, text="Caps Letter Quantity")
        self.caps_title.pack(expand=True, fill='both')
        self.caps_var = tk.IntVar(value=3)
        self.caps_slider = ctk.CTkSlider(self.range_two, from_=1, to=6, variable=self.caps_var, command=self.update_caps_value, number_of_steps=5)
        self.caps_slider.pack(expand=True, fill='both')
        self.caps_label = ctk.CTkLabel(self.range_two, text=self.caps_var.get())
        self.caps_label.pack(expand=True, fill='both')

        self.generate_btn = ctk.CTkButton(self, text="Generate", command=self.generate_password)
        self.generate_btn.pack(padx=20, pady=10, expand=True, fill='both')

        self.exit_btn = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.exit_btn.pack(padx=20, pady=10, expand=True, fill='both')

    def update_length_value(self, value):
        self.length_label.configure(text=int(value))

    def update_number_value(self, value):
        self.number_label.configure(text=int(value))

    def update_symbol_value(self, value):
        self.symbol_label.configure(text=int(value))

    def update_caps_value(self, value):
        self.caps_label.configure(text=int(value))

    def change_number_state(self):
        if self.number_str.get() == 'on':
            self.number_slider.configure(state='disabled')
        else:
            self.number_slider.configure(state='normal')

    def change_symbol_state(self):
        if self.symbol_str.get() == 'on':
            self.symbol_slider.configure(state='disabled')
        else:
            self.symbol_slider.configure(state='normal')

    def change_capitalize_state(self):
        if self.capitalize_str.get() == 'on':
            self.caps_slider.configure(state='disabled')
        else:
            self.caps_slider.configure(state='normal')

    def generate_password(self):
        font = stri.ascii_lowercase
        count = 0

        if self.number_str.get() == 'on':
            font += stri.digits
            count += 1

        if self.symbol_str.get() == 'on':
            font += stri.punctuation
            count += 1
        
        if self.capitalize_str.get() == 'on':
            font += stri.ascii_uppercase
            count += 1

        def gen():
            idx = 0
            password = ''
            
            for i in range(self.length_var.get()):
                password += rand.choice(font)

            return password
        
        password = gen()
        
        database = db.Database()
        # TODO: break if != 0
        database.connect_db()

        if database.select_password(title=self.title_str.get()) not in (None, ''):
            database.insert_password(title=self.title_str.get(), password=password)
        else:
            database.update_password(title=self.title_str.get(), password=password)

        # with open("Passwords.txt", 'a') as f:
        #     f.write(f'{self.title_str.get()}: {password}\n')

        pc.copy(password)
        pass_output = Password_Output(password)
        pass_output.grab_set()

if __name__ == "__main__":
    pg = Password_Generator()
    pg.mainloop()