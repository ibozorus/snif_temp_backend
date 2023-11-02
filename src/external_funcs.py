import webbrowser
import tkinter as tk
from tkinter import messagebox


def webbrowser_callback(url):
    webbrowser.open(url)


def del_on_click(event):
    event.widget.delete(0, tk.END)

def show_msg(msg, title):
    messagebox.showinfo(title, msg)

def show_err(msg, title):
    messagebox.showerror(title, msg)


def del_items(main):
    for widgets in main.winfo_children():
        widgets.destroy()