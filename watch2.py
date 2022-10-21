from datetime import datetime
from distutils import bcppcompiler
import pytz
import pyglet
from tkinter import *
import time

pyglet.font.add_file("digital-7.ttf")
win=Tk()
win.geometry("800x500")
win.resizable(width="False", height="False")
win.configure(bg="grey")


def times():
	home=pytz.timezone("Asia/Kolkata")
	local_time=datetime.now(home)
	current_time=local_time.strftime("%H:%M:%S %p")
	clock.configure(text=current_time)
	name.configure(text="ASIA")
	#clock.after(200, times)
	weekday=time.strftime("%A")
	day=time.strftime("%x")
	month=time.strftime("%b")
	year=time.strftime("%Y")
	date.configure(text=weekday +" " + str(day) + "/" + str(month) + "/" + str(year))

	home1=pytz.timezone("Australia/Victoria")
	local_time1=datetime.now(home1)
	current_time1=local_time1.strftime("%H:%M:%S %p")
	clock1.configure(text=current_time1)
	name1.configure(text="AUSTRALIA")
	#clock1.after(200, times)
	weekday=time.strftime("%A")
	day=time.strftime("%x")
	
	
	date1.configure(text=weekday +" " + str(day))

	home2=pytz.timezone("Europe/London")
	local_time2=datetime.now(home2)
	current_time2=local_time2.strftime("%H:%M:%S %p")
	clock2.configure(text=current_time2)
	name2.configure(text="EUROPE")
	#clock1.after(200, times)
	weekday=time.strftime("%A")
	day=time.strftime("%x")
	month=time.strftime("%b")
	year=time.strftime("%Y")
	date2.configure(text=weekday +" " + str(day) + "/" + str(month) + "/" + str(year))

	home3=pytz.timezone("Africa/Accra")
	local_time3=datetime.now(home3)
	current_time3=local_time3.strftime("%H:%M:%S %p")
	clock3.configure(text=current_time3)
	name3.configure(text="AFRICAN")
	clock1.after(200, times)
	weekday=time.strftime("%A")
	day=time.strftime("%x")
	month=time.strftime("%b")
	year=time.strftime("%Y")
	date3.configure(text=weekday +" " + str(day) + "/" + str(month) + "/" + str(year))
	


name=Label(win, font=("times", 20,"bold"))
name.place(x=30, y=5)
clock=Label(win,font=("digital-7",50,"bold"), borderwidth=10)
clock.place(x=10,y=40)
date=Label(win, font=("digital-7", 15,"bold"))
date.place(x=10,y=110) 

name1=Label(win, font=("times", 20,"bold"))
name1.place(x=515, y=5)
clock1=Label(win,font=("digital-7",50,"bold"))
clock1.place(x=490,y=40)
date1=Label(win, font=("digital-7", 15, "bold"))
date1.place(x=510,y=110)

name2=Label(win, font=("times", 20,"bold"))
name2.place(x=30, y=320)
clock2=Label(win, font=("digital-7",50,"bold"))
clock2.place(x=10,y=350)
date2=Label(win, font=("digital-7", 15, "bold"))
date2.place(x=10,y=420) 

name3=Label(win, font=("times", 20,"bold"))
name3.place(x=515, y=320)
clock3=Label(win,font=("digital-7",50,"bold"))
clock3.place(x=480,y=350)
date3=Label(win, font=("digital-7", 15, "bold"))
date3.place(x=510,y=420) 

times()
win.mainloop() 



home=pytz.timezone('Australia/Victoria')
local_time=datetime.now(home)
current_time=local_time.strftime("%H:%M:%S")
print(current_time)