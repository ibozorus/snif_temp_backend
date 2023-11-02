from tkinter import *
import external_funcs


blue_col = "#2280A9"
scrollbar_col = "#E4E4E4"
scrollbar_col_dark = "#8E8E8E"
update_col = "#0BE019"
login_grey_light = "#ededed"
login_grey_dark =  "#C9C9C9"

root = Tk()
root.title("Temperaturüberwachung")

def login_root():
    external_funcs.del_items(root)
    
    login_frame = Frame(root)
    login_frame.config(height="320", width="320", background=login_grey_light)
    
    login_frame.place(relx=0.5, rely=0.45, anchor="center")


    photo = PhotoImage(file=r"external\Circle-min.png")
    login_canvas = Canvas(login_frame)
    login_canvas.config(height="120", width="320", background=login_grey_dark)
    login_canvas.place(relx=0.5, rely=0.19, anchor="center")
    login_canvas.create_image(160, 45, image=photo)
    
    login_label = Label(root, text="Einloggen")
    login_label.config(background=login_grey_dark, font=("Arial", 15))
    login_label.place(relx=0.5, rely=0.34, anchor="center")

    
    
    next_button_field = Frame(root)
    next_button_field.config(height="60", width="320", background=blue_col)
    next_button_field.place(relx=0.5, rely=0.75, anchor="center")
    

    # Benutzername
    password_lb = Label(root, text="Benutzername oder E-Mail")
    password_lb.place(relx=0.5, rely=0.43, anchor="center")
    username_entry = Entry(root, cursor="hand2", justify="center", font=("Arial", 12))#,state=DISABLED)
    username_entry.bind("<Button-1>", external_funcs.del_on_click)
    username_entry.place(relx=0.5, rely=0.47, anchor="center", width=200)
    username_entry.config(width=35, bg=login_grey_light)

    
    # Passwort
    password_lb = Label(root, text="Passwort")
    password_lb.place(relx=0.5, rely=0.55, anchor="center")
    password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))
    password_entry.bind("<Button-1>", external_funcs.del_on_click)
    password_entry.place(relx=0.5, rely=0.59, anchor="center", width=200)
    password_entry.config(width=35, bg=login_grey_light)


    userbtn = Button(next_button_field, text="Weiter", command=lambda: validate_login(username_entry.get(), password_entry.get()))
    userbtn.config(bg=blue_col, fg="white", width=13, height="2")
    userbtn.place(relx=0.5, rely=0.5,anchor="center")
    

    root.mainloop()

login_root()