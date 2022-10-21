from tkinter import*
win = Tk()
win.title("Simple calculator")

# Creating Entry
e = Entry(win, width=50, borderwidth=5)
e.grid( row=0, column=0, columnspan=3, padx=10, pady=10)

# Creating a function
def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

# creating a clear function
def button_clear():
 e.delete(0, END)

# creating add function 
def button_add():
	first_num = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_num)
	e.delete(0,END) 

# creating equal to function
def button_equal():
  second_num = e.get()
  e.delete(0, END)

  if math == "addition": e.insert(0,f_num + int(second_num))

  if math == "divide": e.insert(0,f_num / int(second_num))

  if math == "multiply": e.insert(0,f_num * int(second_num))

  if math == "subtract": e.insert(0,f_num - int(second_num))

# creating divide button
def button_divide():	
  first_num = e.get()
  global f_num
  global math
  math = "divide"
  f_num = int(first_num)
  e.delete(0,END) 

# creating multiply button
def button_multiply():
  first_num = e.get()
  global f_num
  global math
  math = "multiply"
  f_num = int(first_num)
  e.delete(0,END) 	

# creating subtract button
def button_subtract():
  first_num = e.get()
  global f_num
  global math
  math = "subtract"
  f_num = int(first_num)
  e.delete(0,END) 		



#Creating Buttons
btn_1 = Button(win, text="1", padx=40, pady=20, command=lambda:button_click(1))
btn_2 = Button(win, text="2", padx=40, pady=20, command=lambda:button_click(2))
btn_3 = Button(win, text="3", padx=40, pady=20, command=lambda:button_click(3))
btn_4 = Button(win, text="4", padx=40, pady=20, command=lambda:button_click(4))
btn_5 = Button(win, text="5", padx=40, pady=20, command=lambda:button_click(5))
btn_6 = Button(win, text="6", padx=40, pady=20, command=lambda:button_click(6))
btn_7 = Button(win, text="7", padx=40, pady=20, command=lambda:button_click(7))
btn_8 = Button(win, text="8", padx=40, pady=20, command=lambda:button_click(8))
btn_9 = Button(win, text="9", padx=40, pady=20, command=lambda:button_click(9))
btn_0 = Button(win, text="0", padx=40, pady=20, command=lambda:button_click(0))
btn_add = Button(win, text="+", padx=40, pady=20, command=button_add)
btn_equal= Button(win, text="=", padx=90, pady=20, command=button_equal)
btn_clear= Button(win, text="C", padx=40, pady=20, command=button_clear)
btn_dot = Button(win, text=".", padx=40, pady=20, command=button_click)

btn_divide= Button(win, text="/", padx=40, pady=20, command=button_divide)
btn_multiply= Button(win, text="x", padx=40, pady=20, command=button_multiply)
btn_subtract = Button(win, text="-", padx=40, pady=20, command=button_subtract)


#Putting my buttons on the screen
btn_1.grid(row=3, column=0,)
btn_2.grid(row=3, column=1,)
btn_3.grid(row=3, column=2,)

btn_4.grid(row=2, column=0,)
btn_5.grid(row=2, column=1,)
btn_6.grid(row=2, column=2,)

btn_7.grid(row=1, column=0,)
btn_8.grid(row=1, column=1,)
btn_9.grid(row=1, column=2,)

btn_0.grid(row=4, column=0,)
btn_clear.grid(row=4, column=1,)
btn_add.grid(row=4, column=2,)

btn_equal.grid(row=6, column=1)
btn_dot.grid(row=6, column=0,)

btn_divide.grid(row=5, column=0,)
btn_multiply.grid(row=5, column=1,)
btn_subtract.grid(row=5, column=2,)





win.mainloop()