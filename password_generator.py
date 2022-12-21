from tkinter import*
import string
import random

win = Tk()
win.geometry("500x400")
win.title("password generator")

def password_generator():
    character = list(string.ascii_letters + string.digits + "@#$&^!%")
    random.shuffle(character)
    
    password =[]
    password_length = 7
    
    for x in range(password_length):
        password.append(random.choice(character))
        
    random.shuffle(password)
    password= "".join(password)
    pass_word_l.configure(text=password)
    

u_name = Label(win, text="Usename:", font="arial,20")
u_name.place(x=70, y=100)
pass_word = Label(win, text="Password:", font="arial,20")
pass_word.place(x=70, y=160)

u_name_e = Entry(win, width=30).place(x=170, y=100)
pass_word_l = Label(win, font=("arial", 13,"bold"))
pass_word_l.place(x=170, y=160)

G_pass = Button(win, text="Generate Password", width=20, borderwidth=5, command=password_generator).place(x=190,y=220 )

win.mainloop()