from tkinter import *
import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector as sql
import customer_win 

def schedule():
    #win2.withdraw()
    #after clicking 'set schedule' button 
    global h;global h1;global k
    global k1;global l;global l1;global m;global m1;global p;global p1
    global q;global q1;global r;global r1;global ab;global ab1;global cd;global cd1
    #global i;global i1;global j;global j1
    #code for window which pops out after clicking login
    global win5
    win5=Tk()
    win5.title("train information")
    win5.geometry("1200x780")
    win5.configure(background="powder blue")
    z=Label(win5,text="SCHEDULE",bg="powder blue",fg="blue",padx="500",pady="16",font="impact 72 bold")
    z.place(x=-15,y=-16)
    #****************************************************LABELS*****************************************************************
    z=Label(win5,text="Date Of Departure (YYYY-MM-DD)  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    z.place(x=450,y=120)
    a=Label(win5,text="Train no.   :",bg="powder blue",fg="blue",font="calibri 16 bold")
    a.place(x=450,y=170)
    b=Label(win5,text="departure  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    b.place(x=450,y=220)
    c=Label(win5,text="destination  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    c.place(x=450,y=270)
    d=Label(win5,text="Seats 1st A/c  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    d.place(x=450,y=320)
    e=Label(win5,text="Seats sleeper  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    e.place(x=450,y=370)
    fi=Label(win5,text="Seats economy  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    fi.place(x=450,y=420)
    oi=Label(win5,text="time of departure (HH:MM:SS)  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    oi.place(x=450,y=470)
    w=Label(win5,text="time of arrival (HH:MM:SS) :",bg="powder blue",fg="blue",font="calibri 16 bold")
    w.place(x=450,y=520)
    w1=Label(win5,text="Date Of Arrival (YYYY-MM-DD) :",bg="powder blue",fg="blue",font="calibri 16 bold")
    w1.place(x=450,y=570)
    w2=Label(win5,text="Kilometers :",bg="powder blue",fg="blue",font="calibri 16 bold")
    w2.place(x=450,y=620)
    #***************************************************************************************************************************
    #****************************************************ENTERIES***************************************************************
    h=StringVar();h1=StringVar()
    i=StringVar();i1=StringVar()
    j=StringVar();j1=StringVar()
    k=StringVar();k1=StringVar()
    l=StringVar();l1=StringVar()
    m=StringVar();m1=StringVar()
    p=StringVar();p1=StringVar()
    q=StringVar();q1=StringVar()
    r=StringVar();r1=StringVar()
    ab=StringVar();ab1=StringVar()
    cd=StringVar();cd1=StringVar()
    p=Entry(win5,textvariable=p1)
    p.place(x=780,y=130)
    h=Entry(win5,textvariable=h1)
    h.place(x=780,y=180)
    #***************************************************************************************************************************
    #dropdown for departure
    global o
    global departure
    o= tk.StringVar()#departure city
    departure=ttk.Combobox(win5, width =10,textvariable =o)
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
  
    departure.place(x=780,y=230)
    departure.current(0)  
    #***************************************************************************************************************************
    #dropdown for destination
    global f
    global destination
    f= tk.StringVar()#destination city
    destination=ttk.Combobox(win5, width =10,textvariable =f)
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
  
    destination.place(x=780,y=285)
    destination.current(0)
    #******************************************************************************************************************************* 
    k=Entry(win5,textvariable=k1)
    k.place(x=780,y=330)
    l=Entry(win5,textvariable=l1)
    l.place(x=780,y=380)
    m=Entry(win5,textvariable=m1)
    m.place(x=780,y=430)
    q=Entry(win5,textvariable=q1)
    q.place(x=780,y=480)
    r=Entry(win5,textvariable=r1)
    r.place(x=780,y=530)
    ab=Entry(win5,textvariable=ab1)
    ab.place(x=780,y=570)
    cd=Entry(win5,textvariable=cd1)
    cd.place(x=780,y=620)
    btn=Button(win5,text='enter',fg="blue",bg="white",font="calibri 18 bold",command=lambda:insertion())
    btn.place(x=650,y=660)
    win5.mainloop()

def update_final():
    win10.withdraw()
    win11=Tk()
    win11.title("update schedule")
    win11.geometry("1200x780")
    win11.configure(background="powder blue")
    a=Label(win11,text="UPDATE DETAILS",bg="powder blue",fg="blue",font="calibri 48 bold")
    a.place(x=450,y=10)
    #********************************************************************************************************************************
    z=Label(win11,text="Date(YYYY-MM-DD)  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    z.place(x=450,y=170)
    b=Label(win11,text="departure  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    b.place(x=450,y=220)
    c=Label(win11,text="destination  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    c.place(x=450,y=270)
    d=Label(win11,text="Seats 1st A/c  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    d.place(x=450,y=320)
    e=Label(win11,text="Seats sleeper  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    e.place(x=450,y=370)
    f=Label(win11,text="Seats economy  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    f.place(x=450,y=420)
    o=Label(win11,text="time of departure (HH:MM:SS)  :",bg="powder blue",fg="blue",font="calibri 16 bold")
    o.place(x=450,y=470)
    w=Label(win11,text="time of arrival (HH:MM:SS) :",bg="powder blue",fg="blue",font="calibri 16 bold")
    w.place(x=450,y=520)
    #********************************************************************************************************************************
    ab=StringVar();bc=StringVar()
    cd=StringVar();de=StringVar()
    ef=StringVar();fg=StringVar()
    gh=StringVar();hi=StringVar()
    ij=StringVar();jk=StringVar()
    kl=StringVar();lm=StringVar()
    mn=StringVar();no=StringVar()
    op=StringVar();pq=StringVar()
    #********************************************************************************************************************************
    ab=Entry(win11,textvariable=bc)
    ab.place(x=780,y=175)
    cd=Entry(win11,textvariable=de)
    cd.place(x=780,y=225)
    ef=Entry(win11,textvariable=fg)
    ef.place(x=780,y=275)
    gh=Entry(win11,textvariable=hi)
    gh.place(x=780,y=325)
    ij=Entry(win11,textvariable=jk)
    ij.place(x=780,y=375)
    kl=Entry(win11,textvariable=lm)
    kl.place(x=780,y=425)
    mn=Entry(win11,textvariable=no)
    mn.place(x=780,y=475)
    op=Entry(win11,textvariable=pq)
    op.place(x=780,y=525)
    #*************************************************************************************************************************************************    
    #*************************************************************************************************************************************************
    def update_sql():
        #function to update in table
        date="'"+ab.get()+"'"
        dep="'"+cd.get()+"'"
        des="'"+ef.get()+"'"
        firstac=gh.get()
        sleeper=ij.get()
        economy=kl.get()
        tdep="'"+mn.get()+"'"
        tarr="'"+op.get()+"'"
        seatbkdac=0
        seatbkdsleep=0
        seatbkdeco=0
        try:
            cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
            cr=cn.cursor()
            stmt="delete from train where train_no={}".format(tno)
            cr.execute(stmt)
            print(tno,date,dep,des,tdep,tarr,firstac,sleeper,economy,seatbkdac,seatbkdsleep,seatbkdeco)
            stmt1="insert into train values({},{},{},{},{},{},{},{},{},{},{},{});".format(tno,date,dep,des,tdep,tarr,firstac,sleeper,economy,seatbkdac,seatbkdsleep,seatbkdeco)
            cr.execute(stmt1)
            cn.commit()
            messagebox.showinfo("updating page", "successfully updated")
        except sql.Error as error:
            print("connection error",error)
            messagebox.showerror("Scheduling page", "failed to update")
    btn=Button(win11,text='update',fg="blue",bg="white",font="calibri 18 bold",command=lambda:update_sql())
    btn.place(x=630,y=610)
    win11.mainloop()   

def update_initial():
    #win2.withdraw()
    #after clicking update schedule button
    global win10
    win10=Tk()
    win10.title("update schedule")
    win10.geometry("1200x780")
    win10.configure(background="powder blue")
    y=Label(win10,text="UPDATE SCHEDULE",bg="powder blue",fg="blue",font="impact 50").place(x=470,y=10)
    Z=Label(win10,text="enter train no ",bg="powder blue",fg="blue",font="impact 20").place(x=510,y=160)
    #*************************************************************************************************************************************************
    global x
    global x1
    x=StringVar()
    x1=StringVar() 
    x=Entry(win10,textvariable=x1)
    x.place(x=690,y=170)
    def after_entering_tno():
        try:
            cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
            cr=cn.cursor()
            stmt="select * from train;"
            cr.execute(stmt)
            data=cr.fetchall()
            a=Label(win10,text="TRAIN NO",bg="powder blue",fg="blue",font="calibri 12").place(x=10,y=300)
            b=Label(win10,text="DATE",bg="powder blue",fg="blue",font="calibri 12").place(x=95,y=300)
            c=Label(win10,text="DEPARTURE",bg="powder blue",fg="blue",font="calibri 12").place(x=185,y=300)
            d=Label(win10,text="DESTINATION",bg="powder blue",fg="blue",font="calibri 12").place(x=290,y=300)
            e=Label(win10,text="TIME DEPARTURE",bg="powder blue",fg="blue",font="calibri 12").place(x=400,y=300)
            f=Label(win10,text="TIME ARRIVAL",bg="powder blue",fg="blue",font="calibri 12").place(x=540,y=300)
            g=Label(win10,text="1ST AC",bg="powder blue",fg="blue",font="calibri 12").place(x=670,y=300)
            h=Label(win10,text="SLEEPER",bg="powder blue",fg="blue",font="calibri 12").place(x=750,y=300)
            i=Label(win10,text="ECONOMY",bg="powder blue",fg="blue",font="calibri 12").place(x=830,y=300)
            j=Label(win10,text="SEATS BOOKED AC",bg="powder blue",fg="blue",font="calibri 12").place(x=920,y=300)
            j=Label(win10,text="SEATS BOOKED SlEEP",bg="powder blue",fg="blue",font="calibri 12").place(x=1055,y=300)
            j=Label(win10,text="SEATS BOOKED ECO",bg="powder blue",fg="blue",font="calibri 12").place(x=1215,y=300)
            button=Button(win10,text='update',fg="blue",bg="white",font="calibri 18 bold",command=lambda:update_final())
            button.place(x=640,y=500)
            for train in data:
                if train[0]==int(x.get()):
                    global tno
                    tno=int(train[0])
                    n=Label(win10,text=train[0],bg="powder blue",fg="black",font="calibri 12").place(x=10,y=320)
                    o=Label(win10,text=train[1],bg="powder blue",fg="black",font="calibri 12").place(x=95,y=320)
                    w=Label(win10,text=train[2],bg="powder blue",fg="black",font="calibri 12").place(x=195,y=320)
                    p=Label(win10,text=train[3],bg="powder blue",fg="black",font="calibri 12").place(x=300,y=320)
                    q=Label(win10,text=train[4],bg="powder blue",fg="black",font="calibri 12").place(x=400,y=320)
                    r=Label(win10,text=train[5],bg="powder blue",fg="black",font="calibri 12").place(x=540,y=320)
                    s=Label(win10,text=train[6],bg="powder blue",fg="black",font="calibri 12").place(x=670,y=320)
                    t=Label(win10,text=train[7],bg="powder blue",fg="black",font="calibri 12").place(x=750,y=320)
                    u=Label(win10,text=train[8],bg="powder blue",fg="black",font="calibri 12").place(x=830,y=320)
                    v=Label(win10,text=train[9],bg="powder blue",fg="black",font="calibri 12").place(x=925,y=320)
                    v=Label(win10,text=train[10],bg="powder blue",fg="black",font="calibri 12").place(x=1060,y=320)
                    v=Label(win10,text=train[11],bg="powder blue",fg="black",font="calibri 12").place(x=1220,y=320)
            cn.close()
        except sql.Error as error:
            print("connection error",error)
    btn=Button(win10,text='enter',fg="blue",bg="white",font="calibri 18 bold",command=lambda:after_entering_tno())
    btn.place(x=830,y=155)      
    win10.mainloop()
    
def login():
    #authentication of login
    if d.get()=="sujal" and e.get()=="1234":
        messagebox.showinfo("Login page", "Login successful!")
        win1.destroy()
        global win2
        win2=Tk()
        win2.title("admin")
        win2.geometry("1200x780")
        win2.configure(background="powder blue")
        o=Label(win2,text="ADMIN PORTAL",bg="powder blue",fg="blue",padx="500",pady="50",font="impact 74 bold").place(x=-90,y=-10)
        button_schedule=Button(win2,text='SET SCHEDULE',fg="blue",bg="white",font="calibri 22 bold",command=lambda:schedule())
        button_schedule.place(x=590,y=260)
        #********************************************************************************************************************************************************************************
        button_passengerinfo=Button(win2,text='PASSENGER INFORMATION',fg="blue",bg="white",font="calibri 22 bold",command=lambda:customer_win.passenger_info())
        button_passengerinfo.place(x=515,y=340)
        #********************************************************************************************************************************************************************************
        button_update=Button(win2,text='UPDATE SCHEDULE',fg="blue",bg="white",font="calibri 22 bold",command=lambda:update_initial())
        button_update.place(x=565,y=420)
        #********************************************************************************************************************************************************************************
        button_exit=Button(win2,text='EXIT',fg="blue",bg="white",font="calibri 22 bold",command=lambda:win2.destroy())
        button_exit.place(x=645,y=500)
        win2.mainloop()
    elif d.get()=="" or e.get()=="":
        messagebox.showwarning("Login failed", "all fields are mandatory")
    else:
        messagebox.showwarning("Login failed", "invalid username or password")
        
def connect():
    #making coonection with sql
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
    except sql.Error as error:
        print("connection error",error)

def admin():
    #code for main admin window
    global m
    global n
    global d
    global e
    m=StringVar()
    n=StringVar()
    d=StringVar()
    e=StringVar()
    global win1
    win1=Tk()
    win1.title("ADMIN")
    win1.geometry("1200x780")
    win1.configure(background="powder blue")
    a=Label(win1,text="ADMIN",bg="powder blue",fg="blue",padx="500",pady="50",font="impact 74 bold").pack()
    b=Label(win1,text='ADMIN NAME',bg="powder blue",fg="blue",font="impact 18").place(x=530,y=360)
    c=Label(win1,text='ENTER PASSWORD',bg="powder blue",fg="blue",font="impact 16").place(x=530,y=400)
    d=Entry(win1,textvariable=m)
    d.place(x=735,y=365)
    e=Entry(win1,show="*",textvariable=n)
    e.place(x=735,y=405)
    button=Button(win1,text='enter',fg="blue",bg="white",font="calibri 18 bold",command=login).place(x=645,y=490)
    win1.mainloop()

def insertion():
    win5.withdraw()
    #after clicking enter in scheduling window
    #putting data in table 
    #making coonection with sql
    try:
        cn=sql.connect(host="localhost",user="root",passwd="39#sharmas",database="railway")
        cur=cn.cursor()
        tno=h.get()
        datedep="'"+p.get()+"'"
        datearr="'"+ab.get()+"'"
        #dep="'"+i.get()+"'"
        #des="'"+j.get()+"'"
        dep="'"+departure.get()+"'"
        des="'"+destination.get()+"'"
        firstac=k.get()
        sleeper=l.get()
        economy=m.get()
        tdep="'"+q.get()+"'"
        tarr="'"+r.get()+"'"
        km=int(cd.get())
        #global seatbkd
        seatbkdac=0
        seatbkdsleep=0
        seatbkdeco=0
        if str(tno)=="":
            messagebox.showwarning("scheduling failed", "please enter train number")
        elif str(datedep)=="":
            messagebox.showwarning("scheduling failed", "please enter date of departures")
        elif dep=="":
            messagebox.showwarning("scheduling failed", "please enter strating station")
        elif des=="":
            messagebox.showwarning("scheduling failed", "please enter ending station")
        elif str(firstac)=="":
            messagebox.showwarning("scheduling failed", "please enter passengers of 1st ac")
        elif str(sleeper)=="":
            messagebox.showwarning("scheduling failed", "please enter passengers of 2nd ac")
        elif str(economy)=="":
            messagebox.showwarning("scheduling failed", "please enter passengers of 3rd ac")
        elif str(datearr)=="":
            messagebox.showwarning("scheduling failed", "please enter date of arrival")
        else:
            stmt="insert into train values({},{},{},{},{},{},{},{},{},{},{},{},{},{});".format(tno,datedep,datearr,dep,des,tdep,tarr,firstac,sleeper,economy,seatbkdac,seatbkdsleep,seatbkdeco,km)
            cur.execute(stmt)
            cn.commit()
            messagebox.showinfo("Scheduling page", "successfully added")
    except sql.Error as error:
        messagebox.showerror("Scheduling page", "unsuccessfull")
        print("connection error",error)
    





