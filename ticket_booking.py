#1st sub part of user window
#window for booking of ticket
from tkcalendar import*
import tkinter as tk
from tkinter import *
import mysql.connector as sql
import tkinter.messagebox as messagebox
import customer_win

def connect():
    #making coonection with sql
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cr=cn.cursor()
    except sql.Error as error:
        print("connection error",error)

def receipt():
    win5.withdraw()
    win6=Tk()
    win6.title("ticket")
    win6.geometry("1200x780")
    #********************************************************************************************
    x=Label(win6,text='BOOKING CONFIRMED',fg="blue",font="impact 70 bold").place(x=300,y=10)
    #********************************************************************************************
    x=Label(win6,text='TICKET ID',fg="blue",font="14").place(x=50,y=250)
    x=Label(win6,text='TRAIN NO',fg="blue",font="14").place(x=150,y=250)
    x=Label(win6,text='NAME',fg="blue",font="14").place(x=250,y=250)
    x=Label(win6,text='DATE',fg="blue",font="14").place(x=350,y=250)
    x=Label(win6,text='ADDRESS',fg="blue",font="14").place(x=440,y=250)
    x=Label(win6,text='CONTACT NO',fg="blue",font="14").place(x=550,y=250)
    x=Label(win6,text='TICKETS',fg="blue",font="14").place(x=680,y=250)
    x=Label(win6,text='DEPARTURE',fg="blue",font="14").place(x=775,y=250)
    x=Label(win6,text='DESTINATION',fg="blue",font="14").place(x=905,y=250)
    x=Label(win6,text='TIME DEPARTURE',fg="blue",font="14").place(x=1040,y=250)
    x=Label(win6,text='TIME ARRIVAL',fg="blue",font="14").place(x=1210,y=250)
    x=Label(win6,text='CHARGES',fg="blue",font="14").place(x=550,y=460)
    x=Label(win6,text='PAY MODE',fg="blue",font="14").place(x=670,y=460)   
    #********************************************************************************************
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cr=cn.cursor()
        stmt="select * from booking"
        cr.execute(stmt)
        data=cr.fetchall()
        for a in data:
            if a[0]==tcktid:
                n=Label(win6,text=a[0],fg="black",font="calibri 12").place(x=60,y=330)
                o=Label(win6,text=a[1],fg="black",font="calibri 12").place(x=160,y=330)
                w=Label(win6,text=a[2],fg="black",font="calibri 12").place(x=260,y=330)
                p=Label(win6,text=a[3],fg="black",font="calibri 12").place(x=350,y=330)
                q=Label(win6,text=a[4],fg="black",font="calibri 12").place(x=440,y=330)
                r=Label(win6,text=a[5],fg="black",font="calibri 12").place(x=560,y=330)
                s=Label(win6,text=a[6],fg="black",font="calibri 12").place(x=690,y=330)
                t=Label(win6,text=a[7],fg="black",font="calibri 12").place(x=785,y=330)
                u=Label(win6,text=a[8],fg="black",font="calibri 12").place(x=915,y=330)
                v=Label(win6,text=a[9],fg="black",font="calibri 12").place(x=1050,y=330) 
                x=Label(win6,text=a[10],fg="black",font="calibri 12").place(x=1220,y=330)
                x=Label(win6,text=a[11],fg="black",font="calibri 12").place(x=557,y=540)
                x=Label(win6,text=a[13],fg="black",font="calibri 12").place(x=675,y=540)
        cn.close()     
    except sql.Error as error:
        print("connection error",error)
    #********************************************************************************************
    Button(win6,text='print receipt',fg="black",bg="white",font="calibri 14").place(x=1250,y=650)

def confirmation_msgbox():
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cr=cn.cursor()
        name="'"+a.get()+"'"
        addrs="'"+b.get()+"'"
        cno=int(c.get())
        tickets=tckt.get()
        destination="'"+str(des)+"'"
        departure="'"+(dep)+"'"
        ndate="'"+date+"'"
        nst="'"+st+"'"
        #charge=int(abc.get())
        paym="'"+pay.get()+"'"
        stmt="insert into booking values({},{},{},{},{},{},{},{},{},{},{},{},{},{});".format(tcktid,tno,name,ndate,addrs,cno,tickets,departure,destination,timdep,timarr,charges,nst,paym)
        cr.execute(stmt)
        cn.commit()
        cn.close()
        #*****************************************************UPDATE********************************************************************************
        if st=="1st ac":
            cnn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
            crn=cnn.cursor()
            stmt1="update train set bookedac=bookedac+{} where train_no={};".format(tickets,tno)
            crn.execute(stmt1)
            cnn.commit()
            cnn.close()
            MsgBox = tk.messagebox.askquestion ('confirmation','TICKET CONFIRMED. HAPPY JOURNEY',icon = 'info')
        elif st=="sleeper":
            cnn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
            crn=cnn.cursor()
            stmt1="update train set bookedsleep=bookedsleep+{} where train_no={};".format(tickets,tno)
            crn.execute(stmt1)
            cnn.commit()
            cnn.close()
            MsgBox = tk.messagebox.askquestion ('confirmation','TICKET CONFIRMED. HAPPY JOURNEY',icon = 'info')
        elif st=="economy":
            cnn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
            crn=cnn.cursor()
            stmt1="update train set bookedeco=bookedeco+{} where train_no={};".format(tickets,tno)
            crn.execute(stmt1)
            cnn.commit()
            cnn.close()
            MsgBox = tk.messagebox.askquestion ('confirmation','TICKET CONFIRMED. HAPPY JOURNEY',icon = 'info')
        if MsgBox == 'yes':
            receipt()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen')
    except sql.Error as error:
        print("connection error",error)    

def passenger_data():
    win4.withdraw()
    import random
    global win5
    win5=Tk()
    win5.title("passenger")
    win5.geometry("1200x780")
    win5.configure(background="powder blue")
    x=Label(win5,text='passenger information',fg="blue",font="impact 74",bg="powder blue").place(x=240,y=10)
    x=Label(win5,text='name',fg="blue",font="impact 14 ",bg="powder blue").place(x=550,y=300)
    x=Label(win5,text='address :',fg="blue",font="impact 14",bg="powder blue").place(x=550,y=350)
    x=Label(win5,text='contact number :',fg="blue",font="impact 14",bg="powder blue").place(x=550,y=400)
    x=Label(win5,text='payment mode :',fg="blue",font="impact 14",bg="powder blue").place(x=550,y=450)
    Button(win5,text='book',fg="blue",bg="white",font="impact 20",command=lambda:confirmation_msgbox()).place(x=650,y=520)
    global tcktid
    tcktid=random.randint(1000,9999)
    global a;global a1;global b
    global b1;global c;global c1
    #*********************************************************************************************************************
    #dropdown for payment mode
    global pay
    global pay1
    pay1= tk.StringVar()#class of seat
    pay=ttk.Combobox(win5,width =10,textvariable=pay1)
    pay['values']=('credit card',  
                   'debit card', 
                   'net banking',
                   'paytm wallet',
                   'phonepe wallet',
                   'google pay',
                   'amazon pay',
                   'airtel money',)
    pay.place(x=720,y=455)
    pay.current(0)
    #*********************************************************************************************************************
    a=StringVar();a1=StringVar()
    b=StringVar();b1=StringVar()
    c=IntVar();c1=IntVar()
    a=Entry(win5,textvariable=a1)
    a.place(x=700,y=305)
    b=Entry(win5,textvariable=b1)
    b.place(x=700,y=355)
    c=Entry(win5,textvariable=c1)
    c.place(x=700,y=405)

def custom_1():
    customer_win.close_win3()
    #for taking requirements of customer
    #*****************************************************************************************************
    global win4
    win4=Tk()
    win4.title("ticket booking portal")
    win4.geometry("1200x780")
    win4.configure(background="powder blue")
    #*****************************************************************************************************
    #*****************************************************************************************************
    x=Label(win4,text='Rs.1 per KM',bg="powder blue",fg="black",font="impact 22").place(x=615,y=115)
    x=Label(win4,text='lets book a ticket !',bg="powder blue",fg="blue",font="impact 44").place(x=455,y=35)
    x=Label(win4,text='From (starting)',bg="powder blue",fg="blue",font="impact 22").place(x=510,y=180)
    x=Label(win4,text='To(ending)',bg="powder blue",fg="blue",font="impact 18").place(x=510,y=240)
    x=Label(win4,text='Date',bg="powder blue",fg="blue",font="impact 18").place(x=510,y=300)
    x=Label(win4,text='class of seat',bg="powder blue",fg="blue",font="impact 18").place(x=510,y=355)
    x=Label(win4,text='no. of tickets',bg="powder blue",fg="blue",font="impact 18").place(x=510,y=410)
    #x=Label(win4,text='kilometers',bg="powder blue",fg="blue",font="impact 18").place(x=510,y=460) 
    #dropdown of month
    global m
    global monthchoosen
    m= tk.StringVar()#month 
    monthchoosen=ttk.Combobox(win4, width =10,textvariable =m)
    monthchoosen['values']=('January',  
                            'February', 
                            'March', 
                            'April', 
                            'May', 
                            'June',  
                            'July',  
                            'August',  
                            'September',  
                            'October',  
                            'November',  
                            'December')
    monthchoosen.place(x=600,y=310)
    monthchoosen.current(0)

    
    #dropdown of date
    global e
    global datechoosen
    e= tk.StringVar()#date
    datechoosen = ttk.Combobox(win4, width =10,textvariable =e)
    datechoosen['values']=('01',  
                           '02', 
                           '03', 
                           '04', 
                           '05', 
                           '06',  
                           '07',  
                           '08',  
                           '09',  
                           '10',  
                           '11',  
                           '12', 
                           '13', 
                           '14', 
                           '15', 
                           '16',  
                           '17',  
                           '18',  
                           '19',  
                           '20',
                           '21',  
                           '22',  
                           '23', 
                           '24', 
                           '25', 
                           '26', 
                           '27',  
                           '28',  
                           '29',  
                           '30'
                           '31',)
    datechoosen.place(x=700,y=310)
    datechoosen.current(0)

    #dropdown of year
    global y
    global yearchoosen
    y= tk.StringVar()#year
    yearchoosen = ttk.Combobox(win4, width =10,textvariable =y)
    yearchoosen['values'] = ('2021',  
                             '2022', 
                             '2023', 
                             '2024', 
                             '2025', 
                             '2026',  
                             '2027',  
                             '2028',  
                             '2029',  
                             '2030',)
    yearchoosen.place(x=805,y=310)
    yearchoosen.current(0)

    
    #dropdown for departure
    global o
    global departure
    o= tk.StringVar()#departure city
    departure = ttk.Combobox(win4, width =10,textvariable =o)
    departure['values']=('delhi',  
                         'mumbai', 
                         'jaipur', 
                         'bhopal', 
                         'agra', 
                         'lucknow',  
                         'chennai',  
                         'kolkata',  
                         'udaipur',  
                         'punjab',  
                         'jammu',  
                         'pune') 
  
    departure.place(x=700,y=190)
    departure.current(0)

    #dropdown for destination
    global f
    global destination
    f= tk.StringVar()#destination city
    destination = ttk.Combobox(win4, width =10,textvariable =f)
    destination['values']=('delhi',  
                         'mumbai', 
                         'jaipur', 
                         'bhopal', 
                         'agra', 
                         'lucknow',  
                         'chennai',  
                         'kolkata',  
                         'udaipur',  
                         'punjab',  
                         'jammu',  
                         'pune') 
  
    destination.place(x=700,y=245)
    destination.current(0)

    #dropdown for class of seat
    global r
    global ticket_class
    r= tk.StringVar()#class of seat
    ticket_class = ttk.Combobox(win4, width =10,textvariable =r)
    ticket_class['values']=('1st ac',  
                           'sleeper', 
                           'economy',)
    ticket_class.place(x=700,y=360)
    ticket_class.current(0)
    #*************************************************************************************************************************************
    #for number of tickets
    global t
    global tckt
    t=tk.IntVar()
    tckt=tk.IntVar()
    tckt=Entry(win4,textvariable=t)
    tckt.place(x=680,y=420)
    #*************************************************************************************************************************************
    #for kilometers
    #global abc #for km
    #global abc1
    #abc=StringVar()
    #abc1=StringVar()
    #abc=Entry(win4,textvariable=abc1)
    #abc.place(x=680,y=470)
    #****************************************submission buttons***************************************************************************
    def withdrawing():
        win4.destroy()
        customer_win.custom()
    #*************************************************************************************************************************************
    Button(win4,text='check availability',fg="blue",bg="white",font="calibri 18 bold",command=lambda:custom_2()).place(x=585,y=570)
    Button(win4,text='Back To Previous Menu',fg="blue",bg="white",font="calibri 18 bold",command=lambda:withdrawing()).place(x=550,y=630)
    win4.mainloop()

def custom_2():
    try:
        global dep
        global des
        global st
        global nt
        global date
        dep=departure.get()               #departure city
        des=destination.get()             #dsetination city
        dt=datechoosen.get()              #date
        mn=monthchoosen.get()             #month
        month=0
        if mn=="January":
            month="01"
        elif mn=="February":
            month="02"
        elif mn=="March":
            month="03"
        elif mn=="April":
            month="04"
        elif mn=="May":
            month="05"
        elif mn=="June":
            month="06"
        elif mn=="July":
            month="07"
        elif mn=="August":
            month="08"
        elif mn=="September":
            month="09"
        elif mn=="October":
            month="10"
        elif mn=="November":
            month="11"
        elif mn=="December":
            month="12"  
        yr=yearchoosen.get()              #year
        st=ticket_class.get()             #seat type
        nt=tckt.get()                     #no. of tickets
        date=yr+"-"+month+"-"+dt          #date
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cr=cn.cursor()
        stmt="select * from train;"
        cr.execute(stmt)
        data=cr.fetchall()
        #print(data)
        for train in data:
            global tno
            global timdep
            global timarr
            global tno
            global charges
            if st=="1st ac":
                if str(train[1])==date and train[3]==dep and train[4]==des and train[7]>int(nt):
                    timdep="'"+str(train[5])+"'"
                    timarr="'"+str(train[6])+"'"
                    tno=int(train[0])
                    charges=(int(train[13]))*(int(nt))
                    MsgBox = tk.messagebox.askquestion ('confirmation','ticket is available ,do you want to book the ticket',icon = 'info')
                    if MsgBox == 'yes':
                        passenger_data()
                        break
                    else:
                        tk.messagebox.showinfo('Return','You will now return to the application screen')
                        break
            if st=="sleeper":
                if str(train[1])==date and train[3]==dep and str(train[4])==des and train[8]>int(nt):
                    timdep="'"+str(train[5])+"'"
                    timarr="'"+str(train[6])+"'"
                    tno=int(train[0])
                    charges=(int(train[13]))*(int(nt))
                    MsgBox = tk.messagebox.askquestion ('confirmation','ticket is available ,do you want to book the ticket',icon = 'info')
                    if MsgBox == 'yes':
                        passenger_data()
                        break
                    else:
                        tk.messagebox.showinfo('Return','You will now return to the application screen')
                        break
            if st=="economy":
                if str(train[1])==date and train[3]==dep and str(train[4])==des and train[9]>int(nt):
                    timdep="'"+str(train[5])+"'"
                    timarr="'"+str(train[6])+"'"
                    tno=int(train[0])
                    charges=(int(train[13]))*(int(nt))
                    MsgBox = tk.messagebox.askquestion ('confirmation','ticket is available ,do you want to book the ticket',icon = 'info')
                    if MsgBox == 'yes':
                        passenger_data()
                        break
                    else:
                        tk.messagebox.showinfo('Return','You will now return to the application screen')
                        break
        else:
            tk.messagebox.showinfo('Unavailability','sorry! there is currently no train running on this route')
        cn.close()
                    
                    
            
    except sql.Error as error:
        print("connection error",error)  
    
