from tkinter import *
import external_funcs


blue_col = "#2280A9"
scrollbar_col = "#E4E4E4"
scrollbar_col_dark = "#8E8E8E"
update_col = "#0BE019"
login_grey_light = "#818080"
login_grey_dark =  "#6E6E72"
login_entrys = "#A6A6A6"
blue_for_link = "#001AFF"

root = Tk()
root.geometry("830x500")
root.title("Temperaturüberwachung")
root.resizable(False, False)
# root.config(background)

def login_root():
    external_funcs.del_items(root)
    root.configure(bg=login_grey_light)

    login_frame = Frame(root)
    login_frame.config(height="250", width="320", background=login_grey_dark)
    
    login_frame.place(relx=0.5, rely=0.44, anchor="center")


    # photo = PhotoImage(file=r"external\Circle-min.png")
    # login_canvas = Canvas(login_frame)
    # login_canvas.config(height="80", width="320", background=login_grey_light)
    # login_canvas.place(relx=0.5, rely=0.19, anchor="center")
    # login_canvas.create_image(160, 45, image=photo) 
    
    login_label = Label(root, text="Einloggen")
    login_label.config(background=login_grey_dark, font=("Inria Serif", 18))
    login_label.place(relx=0.5, rely=0.325, anchor="center")

    
    
    next_button_field = Frame(root)
    next_button_field.config(height="60", width="320", background=login_grey_dark)
    next_button_field.place(relx=0.5, rely=0.75, anchor="center")
    

    # Benutzername
    password_lb = Label(root, text="Benutzername", bg=login_grey_dark)
    password_lb.place(relx=0.5, rely=0.43, anchor="center")
    username_entry = Entry(root, bg=login_entrys, cursor="hand2", justify="center", font=("Arial", 12))#,state=DISABLED)
    username_entry.bind("<Button-1>", external_funcs.del_on_click)
    username_entry.place(relx=0.5, rely=0.47, anchor="center", width=200)
    username_entry.config(width=35, bg=login_entrys)

    
    # Passwort
    password_lb = Label(root, text="Passwort", bg=login_grey_dark)
    password_lb.place(relx=0.5, rely=0.55, anchor="center")
    password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))

    password_entry.bind("<Button-1>", external_funcs.del_on_click)
    password_entry.place(relx=0.5, rely=0.59, anchor="center", width=200)
    password_entry.config(width=35, bg=login_entrys)


    userbtn = Button(root, text="Weiter", command=lambda: validate_login(username_entry.get(), password_entry.get()))
    userbtn.config(bg="#343434", fg="white", width=16, height="2")
    userbtn.place(relx=0.5, rely=0.7,anchor="center")

    register = Label(root, text="Registrieren", bg=login_grey_dark, fg=blue_for_link, cursor="hand2")
    register.place(relx=0.5, rely=0.78,anchor="center")
    register.bind("<Button-1>", lambda e: open_register())
    

    root.mainloop()

def open_register():
    external_funcs.del_items(root)
    root.configure(bg=login_grey_light)

    login_frame = Frame(root)
    login_frame.config(height="250", width="320", background=login_grey_dark)
    
    login_frame.place(relx=0.5, rely=0.44, anchor="center")


    # photo = PhotoImage(file=r"external\Circle-min.png")
    # login_canvas = Canvas(login_frame)
    # login_canvas.config(height="80", width="320", background=login_grey_light)
    # login_canvas.place(relx=0.5, rely=0.19, anchor="center")
    # login_canvas.create_image(160, 45, image=photo) 
    
    login_label = Label(root, text="Registrieren")
    login_label.config(background=login_grey_dark, font=("Inria Serif", 18))
    login_label.place(relx=0.5, rely=0.325, anchor="center")

    
    
    next_button_field = Frame(root)
    next_button_field.config(height="145", width="320", background=login_grey_dark)
    next_button_field.place(relx=0.5, rely=0.75, anchor="center")
    

    # Benutzername
    username_lb = Label(root, text="Benutzername", bg=login_grey_dark)
    username_lb.place(relx=0.5, rely=0.43, anchor="center")
    username_entry = Entry(root, bg=login_entrys, cursor="hand2", justify="center", font=("Arial", 12))#,state=DISABLED)
    username_entry.bind("<Button-1>", external_funcs.del_on_click)
    username_entry.place(relx=0.5, rely=0.47, anchor="center", width=200)
    username_entry.config(width=35, bg=login_entrys)

    
    # Benutzername wiederholen
    password_lb = Label(root, text="Passwort", bg=login_grey_dark)
    password_lb.place(relx=0.5, rely=0.55, anchor="center")
    password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))
    password_entry.bind("<Button-1>", external_funcs.del_on_click)
    password_entry.place(relx=0.5, rely=0.59, anchor="center", width=200)
    password_entry.config(width=35, bg=login_entrys)
    

    # Passwort
    second_password_lb = Label(root, text="Passwort wiederholen", bg=login_grey_dark)
    second_password_lb.place(relx=0.5, rely=0.67, anchor="center")
    second_password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))
    second_password_entry.bind("<Button-1>", external_funcs.del_on_click)
    second_password_entry.place(relx=0.5, rely=0.71, anchor="center", width=200)
    second_password_entry.config(width=35, bg=login_entrys)


    userbtn = Button(root, text="Weiter", command=lambda: register_new_user(username_entry.get(), password_entry.get() ,second_password_entry.get()))
    userbtn.config(bg="#343434", fg="white", width=16, height="2")
    userbtn.place(relx=0.5, rely=0.8,anchor="center")

    register = Label(root, text="Einloggen", bg=login_grey_dark, fg=blue_for_link, cursor="hand2")
    register.place(relx=0.5, rely=0.87,anchor="center")
    register.bind("<Button-1>", lambda e: login_root())
    

    root.mainloop()


def validate_login(username, password):
    main_root()
    return None


def register_new_user(username, password ,second_password):
    if username != "" and password != "" and second_password != "":
        if password != second_password:
            external_funcs.show_err("Die eingegebenen Passwörter stimmen nicht überein!", "Fehler")
        else:
            main_root()
            print(f"{username}, {second_password}, {password}")
    else:
        external_funcs.show_err("Die Eingaben dürfen nicht leer sein!", "Fehler")

def main_root():
    external_funcs.del_items(root)
    root.configure(bg=login_grey_light)

    
login_root()