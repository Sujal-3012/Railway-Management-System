#1st WINDOW
import tkinter as tk
import tkinter.messagebox as messagebox
import admin_win
import customer_win
from tkinter import *
from tkinter import Canvas
import mysql.connector as sql

#********************* CONNECTION BLOCK *******************
def connect():
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
    except sql.Error as error:
        print("connection error",error)
    print(cn.is_connected())

#**********************************************************
win=Tk()
win.title("indian railways")
win.geometry("1200x780")
win.configure(background="powder blue")

a=Label(win,text="Railway Management",bg="powder blue",fg="blue",padx="500",pady="50",font="impact 74 bold").place(x=-230,y=-10)
admin_button=Button(win,text='ADMIN',fg="blue",bg="white",font="calibri 24 bold",padx=101,pady=12,command=lambda:admin_win.admin())
admin_button.place(x=800,y=235)
user_button=Button(win,text='TICKET WINDOW',fg="blue",bg="white",font="calibri 24 bold",padx=35.48,pady=12,command=lambda:customer_win.custom())
user_button.place(x=800,y=330)

#********************** IMAGE BLOCK ***********************
c=Canvas(win,width=350,height=350,bg="powder blue")
c.place(x=280,y=200)
i=PhotoImage(file="login.png")
c.create_image(0,0,anchor=NW, image=i)
#**********************************************************

button_exit=Button(win,text='EXIT',fg="blue",bg="white",font="calibri 24 bold",padx=120,pady=12,command=lambda:win.destroy())
button_exit.place(x=800,y=425)
win.mainloop()                
