# Import Librarys
from tkinter import *
from tkinter import ttk
import json
import requests
import re
import pandas as pd

# Import Module
import external_funcs as ef


url = "http://localhost:8080"


blue_col = "#2280A9"
scrollbar_col = "#E4E4E4"
scrollbar_col_dark = "#8E8E8E"
update_col = "#0BE019"
# login_grey_light = "#818080"
login_grey_light = "#e8e8e8"
# login_grey_dark =  "#6E6E72"
login_grey_dark="#cfcfcf"
login_entrys = "#A6A6A6"
blue_for_link = "#001AFF"
navbar_col = "#4F4646"
option_entrys = "#b8b9ba"

root = Tk()
root.geometry("830x500")
root.title("Temperaturüberwachung")
root.resizable(False, False)
# root.config(background)

def login_root():
    ef.del_items(root)
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
    username_entry.bind("<Button-1>", ef.del_on_click)
    username_entry.place(relx=0.5, rely=0.47, anchor="center", width=200)
    username_entry.config(width=35, bg=login_entrys)

    
    # Passwort
    password_lb = Label(root, text="Passwort", bg=login_grey_dark)
    password_lb.place(relx=0.5, rely=0.55, anchor="center")
    password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))

    password_entry.bind("<Button-1>", ef.del_on_click)
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
    ef.del_items(root)
    root.configure(bg=login_grey_light)

    login_frame = Frame(root)
    login_frame.config(height="250", width="500", background=login_grey_dark)
    
    login_frame.place(relx=0.5, rely=0.35, anchor="center")


    login_label = Label(root, text="Registrieren")
    login_label.config(background=login_grey_dark, font=("Inria Serif", 18))
    login_label.place(relx=0.5, rely=0.22, anchor="center")

    
    
    next_button_field = Frame(root)
    next_button_field.config(height="210", width="500", background=login_grey_dark)
    next_button_field.place(relx=0.5, rely=0.75, anchor="center")
    

    # Benutzername
    username_lb = Label(root, text="Benutzername", bg=login_grey_dark)
    username_lb.place(relx=0.35, rely=0.35, anchor="center")
    username_entry = Entry(root, bg=login_entrys, cursor="hand2", justify="center", font=("Arial", 12))#,state=DISABLED)
    username_entry.bind("<Button-1>", ef.del_on_click)
    username_entry.place(relx=0.35, rely=0.39, anchor="center", width=200)
    username_entry.config(width=35, bg=login_entrys)

    
    # Benutzername wiederholen
    password_lb = Label(root, text="Passwort", bg=login_grey_dark)
    password_lb.place(relx=0.35, rely=0.48, anchor="center")
    password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))
    password_entry.bind("<Button-1>", ef.del_on_click)
    password_entry.place(relx=0.35, rely=0.52, anchor="center", width=200)
    password_entry.config(width=35, bg=login_entrys)
    

    # Passwort
    second_password_lb = Label(root, text="Passwort wiederholen", bg=login_grey_dark)
    second_password_lb.place(relx=0.35, rely=0.60, anchor="center")
    second_password_entry = Entry(root, cursor="hand2", show="*", justify="center", font=("Arial", 12))
    second_password_entry.bind("<Button-1>", ef.del_on_click)
    second_password_entry.place(relx=0.35, rely=0.65, anchor="center", width=200)
    second_password_entry.config(width=35, bg=login_entrys)


    # phoneNumber
    phoneNumber_lb = Label(root, text="Telefonnummer eingeben", bg=login_grey_dark)
    phoneNumber_lb.place(relx=0.65, rely=0.35, anchor="center")
    phoneNumber_entry = Entry(root, cursor="hand2", justify="center", font=("Arial", 12))
    phoneNumber_entry.bind("<Button-1>", ef.del_on_click)
    phoneNumber_entry.place(relx=0.65, rely=0.39, anchor="center", width=200)
    phoneNumber_entry.config(width=35, bg=login_entrys)

    #firstName
    firstName_lb = Label(root, text="Vornamen eingeben", bg=login_grey_dark)
    firstName_lb.place(relx=0.65, rely=0.48, anchor="center")
    firstName_entry = Entry(root, cursor="hand2", justify="center", font=("Arial", 12))
    firstName_entry.bind("<Button-1>", ef.del_on_click)
    firstName_entry.place(relx=0.65, rely=0.52, anchor="center", width=200)
    firstName_entry.config(width=35, bg=login_entrys)

    #lastName
    lastName_lb = Label(root, text="Nachnamen eingeben", bg=login_grey_dark)
    lastName_lb.place(relx=0.65, rely=0.60, anchor="center")
    lastName_entry = Entry(root, cursor="hand2", justify="center", font=("Arial", 12))
    lastName_entry.bind("<Button-1>", ef.del_on_click)
    lastName_entry.place(relx=0.65, rely=0.65, anchor="center", width=200)
    lastName_entry.config(width=35, bg=login_entrys)


    var1 = IntVar()
    isAdmin = Checkbutton(root, text="isAdmin", variable=var1, onvalue=1, offvalue=0, bg=login_grey_dark, font=("Arial", 12))
    isAdmin.place(relx=0.5, rely=0.75, anchor="center")


    loginTries = 0
    userbtn = Button(root, text="Weiter", command=lambda: register_new_user(
        username_entry.get(), 
        password_entry.get(),
        second_password_entry.get(),
        phoneNumber_entry.get(),
        loginTries,
        firstName_entry.get(),
        lastName_entry.get(),
        var1.get()
    ))
    userbtn.config(bg="#343434", fg="white", width=16, height="2")
    userbtn.place(relx=0.5, rely=0.85,anchor="center")

    register = Label(root, text="Einloggen", bg=login_grey_dark, fg=blue_for_link, cursor="hand2")
    register.place(relx=0.5, rely=0.925,anchor="center")
    register.bind("<Button-1>", lambda e: login_root())
    
    root.mainloop()


def validate_login(username, password):
    if username != "" and password != "":
        try:
            payload = json.dumps({
            "username": f"{username}",
            "password": f"{password}"
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("GET", f"{url}/user/check-login", headers=headers, data=payload)

            res = response.json()
            val_msg = res['message']

            if val_msg == "success":
                main_root()
            else:
                ef.show_err("Die eingegebene Kombination aus Nutzername und Passwort war leider nicht korrekt.", "Fehler")
        except KeyError:
            ef.show_err("Die eingegebene Kombination aus Nutzername und Passwort war leider nicht korrekt.", "Fehler")
    else:
        ef.show_err("Sie haben keinen Benutzer/Passwort eingegeben!", "Fehler")
        


def register_new_user(username, password ,second_password, phoneNumber, loginTries, firstName, lastName, isAdmin):
    if username != "" and password != "" and second_password != "":
        if password != second_password:
            ef.show_err("Die eingegebenen Passwörter stimmen nicht überein!", "Fehler")
        else:
            if isAdmin == 1: 
                isAdmin = True
            else:
                isAdmin = False

            payload = json.dumps({
            "username": f"{username}",
            "password": f"{password}",
            "phoneNumber": f"{phoneNumber}",
            "loginTries": f"{loginTries}",
            "firstName": f"{firstName}",
            "lastName": f"{lastName}",
            "admin": isAdmin
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", f"{url}/user", headers=headers, data=payload)


            ef.show_msg("Sie wurde erfolgreich registriert. Loggen Sie sich nun ein!", "Erfolg")
            login_root()
            # main_root()
            # print(f"{username}, {second_password}, {password}")
    else:
        ef.show_err("Die Eingaben dürfen nicht leer sein!", "Fehler")


def main_root():
    ef.del_items(root)

    # Navigationsbar
    navbar = Frame(root)
    navbar.config(height="100", width="830", background=navbar_col)
    navbar.place(relx=0.5, rely=0, anchor="center")

    # Ergebnisfeld
    results_canv = Canvas(root, bg="#dedede", height="400", width="500")
    results_canv.place(relx=0.68, rely=0.545, anchor="center")

    # Button für Logout
    logout_button = Button(navbar, bg=option_entrys,text="Ausloggen", width="15", command=login_root)
    logout_button.place(relx=0.92, rely=0.75, anchor="center")


    # Benutzeroptionen
    useroptions = Canvas(root)
    useroptions_lb = Label(useroptions, text="Benutzeroptionen", bg=option_entrys, font=("Arial", 12))
    useroptions_lb.place(relx=0.5, rely=0.08, anchor="center")
    useroptions.config(height="190", width="280", bg=option_entrys)
    useroptions.place(relx=0.2, rely=0.34, anchor="center")

    # Benutzer anzeigen
    show_user = Button(useroptions, text="Benutzer anzeigen", width="25", font=("Arial", 10), command=lambda: show_users(results_canv))
    show_user.place(relx=0.5, rely=0.3, anchor="center")

    # Benutzer anlegen
    show_user = Button(useroptions, text="Benutzer anlegen", width="25", font=("Arial", 10), command=lambda: add_user(results_canv))
    show_user.place(relx=0.5, rely=0.48, anchor="center")

    # Benuter bearbeiten
    show_user = Button(useroptions, text="Benutzer bearbeiten", width="25", font=("Arial", 10))
    show_user.place(relx=0.5, rely=0.66, anchor="center")

    # Benuter löschen
    show_user = Button(useroptions, text="Benutzer löschen", width="25", font=("Arial", 10))
    show_user.place(relx=0.5, rely=0.85, anchor="center")


    # Tabellenoptionen
    tableoptions = Canvas(root)
    tableoptions_lb = Label(tableoptions, text="Tabellenoptionen", bg=option_entrys, font=("Arial", 12))
    tableoptions_lb.place(relx=0.5, rely=0.08, anchor="center")
    tableoptions.config(height="190", width="280", bg=option_entrys)
    tableoptions.place(relx=0.2, rely=0.75, anchor="center")

    # Log-Tabelle anzeigen
    show_user = Button(tableoptions, text="Log-Tabelle anzeigen", width="25", font=("Arial", 10))
    show_user.place(relx=0.5, rely=0.3, anchor="center")

    # Temperaturdaten löschen   
    show_user = Button(tableoptions, text="Temperaturdaten löschen", width="25", font=("Arial", 10))
    show_user.place(relx=0.5, rely=0.48, anchor="center")

    # Sensordaten bearbeiten
    show_user = Button(tableoptions, text="Sensordaten bearbeiten", width="25", font=("Arial", 10))
    show_user.place(relx=0.5, rely=0.66, anchor="center")

    # Sensordaten löschen
    show_user = Button(tableoptions, text="Sensordaten löschen", width="25", font=("Arial", 10))
    show_user.place(relx=0.5, rely=0.85, anchor="center")

    root.configure(bg="white")


def add_user(canv):
    ef.del_items(canv)

    name_lb = Label(canv, text="Namen eingeben", bg="#dedede")
    name_lb.place(relx=0.5, rely=0.045, anchor="center")

    name_entr = Entry(canv, bg=login_entrys, width="50")
    name_entr.place(relx=0.5, rely=0.089, anchor="center")


    name_lb = Label(canv, text="Namen eingeben", bg="#dedede")
    name_lb.place(relx=0.5, rely=0.045, anchor="center")

    name_entr = Entry(canv, bg=login_entrys, width="50")
    name_entr.place(relx=0.5, rely=0.089, anchor="center")


def show_users(canv):
    ef.del_items(canv)
    # Alle Einträge aus SQL Befehl

    payload = {}
    headers = {}
    values = {}
    val_list = []

    response = requests.request("GET", f"{url}/user/all", headers=headers, data=payload)
    res = response.json()
    

    
        # val_list.append(values)
        
    

    
    # Column Namen der Datenbank
    # print(list(values.keys()))
    # print(val_list)

    col_names = list(values.keys())

    # col_names = [i[0] for i in col_names]
    for i in res:
        values = {
            'id' :i['id'], 
            'username': i['username'],
            'firstName': i['firstName'],
            'lastName': i['lastName'],
            'password': i['password'],
            'phoneNumber': i['phoneNumber'],
            'admin': i['admin'],
        } 

    # Treeview Widget, zum anzeigen der Datenbankergebnisse
    trv = ttk.Treeview(canv, selectmode="browse", columns=list(values.keys()), height=19)
    trv.place(relx=0.5, rely=0.5,anchor="center")

    for key in values.keys():
        trv.heading(key, text=key)

    trv.insert("", "end", values=list(values.values()))
        
    # Richtige Überschrift jeder Zeile
    # for i in col_names:
    #     trv.column(i, anchor="c", width=200, stretch=False)
    #     trv.heading(i, text=i)
    
    vsb = Scrollbar(canv, orient="vertical", command=trv.yview)
    vsb.place(relx=0.9, rely=0.175, relheight=0.7)

    hsb = Scrollbar(canv, orient="horizontal", command=trv.xview)
    hsb.place(relx=0.01 , rely=0.94, relwidth=0.9)

    trv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)


login_root() 