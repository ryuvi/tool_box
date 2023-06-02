import customtkinter as ctk
import tkinter as tk
import datetime as dt
import enum as e
import pyperclip as pc

class TimeStampConverter(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Timestamp Converter")
        self.geometry("300x500")
        self.font = ("Comic Sans MS", 16)

        self.entry = ctk.CTkEntry(self, placeholder_text="Insert the timestamp/date...")
        self.entry.pack(padx=20, pady=20, ipadx=15, ipady=5, expand=True, fill='both')
        self.entry.configure(font=self.font)

        self.radio_frame = ctk.CTkFrame(self)
        self.radio_frame.pack(padx=10, pady=10, expand=True, fill='both')
        self.activated_radio = tk.IntVar(value=1)
        self.to_datetime = ctk.CTkRadioButton(self.radio_frame, text="Convert To Datetime", variable=self.activated_radio, value=1)
        self.to_datetime.pack(padx=10, expand=True, fill='both')
        self.to_timestamp = ctk.CTkRadioButton(self.radio_frame, text="Convert To Timestamp", variable=self.activated_radio, value=2)
        self.to_timestamp.pack(padx=10, expand=True, fill='both')

        self.to_datetime.configure(font=self.font)
        self.to_timestamp.configure(font=self.font)

        self.result = ctk.CTkLabel(self, text="Result will be show here...")
        self.result.pack(padx=20, pady=20, expand=True, fill='both')
        self.result.configure(font=self.font)

        self.convert_button = ctk.CTkButton(self, text="Convert", command=self.convert)
        self.convert_button.pack(padx=10, pady=10, expand=True, fill='both')
        self.convert_button.configure(font=self.font)
        self.close_button = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.close_button.pack(padx=10, pady=5, expand=True, fill='both')
        self.close_button.configure(font=self.font)

    def convert(self):
        if self.activated_radio.get() == 1:
            date = dt.datetime.fromtimestamp(int(self.entry.get()))
            self.result.configure(text=date)
            pc.copy()
        
        if self.activated_radio.get() == 2:
            timestamp = int(dt.datetime.timestamp(dt.datetime.fromisoformat(self.entry.get())))
            self.result.configure(text=timestamp)
            pc.copy(timestamp)

if __name__ == '__main__':
    t = TimeStampConverter()
    t.mainloop()