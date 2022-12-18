import tkinter as tk
from tkinter import *
from tkinter import Canvas
import ticket_booking
import mysql.connector as sql
from tkinter import ttk
import admin_win


def passenger_info():
    try:
        #admin_win.close_win2()
        win9=Tk()
        win9.title("passenger portal")
        win9.geometry("1200x780")
        win9.configure(background="powder blue")
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cr=cn.cursor()
        stmt="select * from booking;"
        cr.execute(stmt)
        data=cr.fetchall()
        cn.close()
        a=Label(win9,text="PASSENGER INFORMATION",bg="powder blue",fg="green",font="impact 20 ").place(x=560,y=0)
        b=Label(win9,text="TICKET ID",bg="powder blue",fg="blue",font="calibri 12").place(x=40,y=60)
        c=Label(win9,text="TRAIN NO",bg="powder blue",fg="blue",font="calibri 12").place(x=130,y=60)
        d=Label(win9,text="NAME",bg="powder blue",fg="blue",font="calibri 12").place(x=230,y=60)
        e=Label(win9,text="ADDRESS",bg="powder blue",fg="blue",font="calibri 12").place(x=315,y=60)
        f=Label(win9,text="CONTACT NO",bg="powder blue",fg="blue",font="calibri 12").place(x=440,y=60)
        g=Label(win9,text="TICKETS",bg="powder blue",fg="blue",font="calibri 12").place(x=560,y=60)
        h=Label(win9,text="DEPARTURE",bg="powder blue",fg="blue",font="calibri 12").place(x=640,y=60)
        i=Label(win9,text="DESTINATION",bg="powder blue",fg="blue",font="calibri 12").place(x=740,y=60)
        j=Label(win9,text="TIME DEPARTURE",bg="powder blue",fg="blue",font="calibri 12").place(x=860,y=60)
        k=Label(win9,text="TIME ARRIVAL",bg="powder blue",fg="blue",font="calibri 12").place(x=1010,y=60)
        l=Label(win9,text="CHARGES",bg="powder blue",fg="blue",font="calibri 12").place(x=1130,y=60)
        m=Label(win9,text="TOTAL CHARGES",bg="powder blue",fg="blue",font="calibri 12").place(x=1220,y=60)
        a1=40;b1=80
        for a in data:
            n=Label(win9,text=a[0],bg="powder blue",fg="black",font="calibri 12").place(x=a1,y=b1)
            o=Label(win9,text=a[1],bg="powder blue",fg="black",font="calibri 12").place(x=a1+90,y=b1)
            w=Label(win9,text=a[2],bg="powder blue",fg="black",font="calibri 12").place(x=a1+192,y=b1)
            p=Label(win9,text=a[3],bg="powder blue",fg="black",font="calibri 12").place(x=a1+273,y=b1)
            q=Label(win9,text=a[4],bg="powder blue",fg="black",font="calibri 12").place(x=a1+402,y=b1)
            r=Label(win9,text=a[5],bg="powder blue",fg="black",font="calibri 12").place(x=a1+525,y=b1)
            s=Label(win9,text=a[6],bg="powder blue",fg="black",font="calibri 12").place(x=a1+620,y=b1)
            t=Label(win9,text=a[7],bg="powder blue",fg="black",font="calibri 12").place(x=a1+725,y=b1)
            u=Label(win9,text=a[8],bg="powder blue",fg="black",font="calibri 12").place(x=a1+850,y=b1)
            v=Label(win9,text=a[9],bg="powder blue",fg="black",font="calibri 12").place(x=a1+990,y=b1) 
            x=Label(win9,text=a[10],bg="powder blue",fg="black",font="calibri 12").place(x=a1+1090,y=b1)
            y=Label(win9,text=a[12],bg="powder blue",fg="black",font="calibri 12").place(x=a1+1185,y=b1)
            b1+=20
        win9.mainloop()
        
    except sql.Error as error:
        print("connection error",error)

def custom():
    global win3
    win3=Tk()
    win3.title("ticket portal")
    win3.geometry("1200x780")
    win3.configure(background="powder blue")
    a=Label(win3,text="TICKETING WINDOW",bg="powder blue",fg="blue",padx="500",pady="50",font="impact 74 bold").place(x=-230,y=-10)
    button1=Button(win3,text='book a ticket',fg="blue",bg="white",font="calibri 18 bold",padx='100',command=lambda:ticket_booking.custom_1()).place(x=515,y=260)
    button2=Button(win3,text='cancel a ticket',fg="blue",bg="white",font="calibri 18 bold",padx='95',command=lambda:cancellation()).place(x=515,y=340)
    button3=Button(win3,text='back to main menu',fg="blue",bg="white",font="calibri 18 bold",padx='70',command=lambda:win3.withdraw()).place(x=515,y=420)
    win3.mainloop()

def close_win3():
    #fn for destroying win3
    #dedicated fn because window which opens after clicking book a ticket is in other file
    win3.withdraw()

def delete_from_sql():
    win8.withdraw()
    MsgBox = tk.messagebox.askquestion ('cancellation','are you sure you want to cancel the ticket',icon = 'info')
    if MsgBox == 'yes':
        try:
            cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
            cr=cn.cursor()
            stmt="select * from booking;"
            cr.execute(stmt)
            data=cr.fetchall()   
            for booking in data:
                if booking[0]==int(b.get()):
                    if booking[12]=="1st ac":
                        stmt2="update train set bookedac=bookedac-{} where train_no={};".format(booking[6],booking[1])
                        cr.execute(stmt2)
                        cn.commit()
                    elif booking[12]=="sleeper":
                        stmt2="update train set bookedsleep=bookedsleep-{} where train_no={};".format(booking[6],booking[1])
                        cr.execute(stmt2)
                        cn.commit()
                    elif booking[12]=="economy":
                        stmt2="update train set bookedeco=bookedeco-{} where train_no={};".format(booking[6],booking[1])
                        cr.execute(stmt2)
                        cn.commit()
                    stmt1="delete from booking where ticket_id={};".format(b.get())
                    cr.execute(stmt1)
                    cn.commit()
                    tk.messagebox.showinfo('cancelled','Your ticket has been cancelled')
                    cn.close()
                else:
                    tk.messagebox.showerror('error','Your ticket has not been cancelled')
                break
        except sql.Error as error:
            print("connection error",error)         
    else:
        tk.messagebox.showinfo('cancellation','ticket cancellation denied')
    
def cancel_confirm():
    win7.withdraw()
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cr=cn.cursor()
        stmt="select * from booking;"
        cr.execute(stmt)
        data=cr.fetchall()
        for train in data:
            if train[0]==int(b.get()):
                global win8
                win8=Tk()
                win8.title("ticket cancellation confirmation")
                win8.geometry("1200x780")
                win8.configure(background="powder blue")
                a=Label(win8,text="CONFIRM YOUR CANCELLATION",bg="powder blue",fg="blue",padx="300",pady="50",font="impact 70 bold").place(x=-175,y=-10)
                o=Label(win8,text="Name",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=210)
                c=Label(win8,text="Train No",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=250)
                d=Label(win8,text="Ticket Id",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=290)
                e=Label(win8,text="Contact No",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=330)
                f=Label(win8,text="Tickets",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=370)
                g=Label(win8,text="Departure",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=410)
                g1=Label(win8,text="Destination",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=450)
                g=Label(win8,text="Total Charges",bg="powder blue",fg="blue",font="impact 16").place(x=550,y=500)
                #****************************************************************************************************************************************
                h=Label(win8,text=train[2],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=210)
                i=Label(win8,text=train[1],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=250)
                j=Label(win8,text=train[0],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=290)
                k=Label(win8,text=train[5],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=330)
                l=Label(win8,text=train[6],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=370)
                m=Label(win8,text=train[7],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=410)
                m1=Label(win8,text=train[8],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=450)
                m1=Label(win8,text=train[11],bg="powder blue",fg="blue",font="calibri 16").place(x=750,y=500)
                #****************************************************************************************************************************************
                button=Button(win8,text='Cancel Ticket',fg="blue",bg="white",font="calibri 18 bold",command=lambda:delete_from_sql())
                button.place(x=600,y=600)
                cn.close()
                break
        else:
            messagebox.showwarning("no ticket found", "invalid ticket id")
            cn.close()
    except sql.Error as error:
        print("connection error",error)
    

def cancellation():
    win3.withdraw()
    global win7
    win7=Tk()
    win7.title("ticket cancellation")
    win7.geometry("1200x780")
    win7.configure(background="powder blue")
    a=Label(win7,text="CANCELLATION WINDOW",bg="powder blue",fg="blue",padx="500",pady="50",font="impact 74 bold").place(x=-270,y=-10)
    a=Label(win7,text="Enter Your Ticket Id",bg="powder blue",fg="blue",padx="500",font="impact 18").place(x=-10,y=200)
    global b
    global c
    b=IntVar()
    c=IntVar()
    b=Entry(win7,textvariable=c)
    b.place(x=700,y=208)
    def withdrawing():
        win7.withdraw()
        custom()
    button=Button(win7,text='enter',fg="blue",bg="white",font="calibri 18 bold",command=lambda:cancel_confirm())
    button.place(x=640,y=250)
    button1=Button(win7,text='back to previous menu',fg="blue",bg="white",font="calibri 18 bold",command=lambda:withdrawing())
    button1.place(x=560,y=310)
    win7.mainloop()

