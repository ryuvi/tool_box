import customtkinter as ctk
import tkinter as tk

class TimeStampConverter(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Timestamp Converter")
        self.geometry("800x600")
