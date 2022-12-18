def maketables():
    import mysql.connector as sql
    newcon=sql.connect(database='rose',user='root',host='localhost',password='39#sharmas')
    if newcon.is_connected()==True:
        print("CONNECTION SUCCESSFUL")
    else :
        print("CONNECTION UNSUCCESSFUL")
    cr=newcon.cursor()
    stmt1='''create table train
           (train_no int primary key,
            date_dep date not null,
            date_arr date not null,
            departure varchar(15) not null,
            destination varchar(15) not null,
            time_of_departure time not null,
            time_of_arrival time not null,
            1st_ac int not null,
            sleeper int not null,
            economy int not null,
            bookedac int not null,
            bookedsleep int not null,
            bookedeco int not null,
            kilometers int not null);'''
    cr.execute(stmt1)
    stmt2='''create table booking
           (ticket_id int primary key,
            train_no int not null,
            name varchar(20) not null,
            date date not null,
            address varchar(30) not null,
            contact_no bigint not null,
            no_of_passengers int not null,
            departure varchar(15) not null,
            destination varchar(15)not null,
            time_of_departure time not null,
            time_of_arrival time not null,
            charges int not null,
            tickets_type varchar(10) not null,
            pay_mode varchar(15) not null);'''
    cr.execute(stmt2)
    newcon.close()
maketables()
