import sqlite3
con = sqlite3.Connection('My_Database1')
cur=con.cursor()
cur.execute('create table operator(opid INTEGER PRIMARY KEY AUTOINCREMENT,name varchar(15),address varchar(25),phone number,email varchar(40))')
cur.execute('insert into operator values(1,"Kamla","AB Road Guna",1231231231,"Kamla@gmail.com")')
cur.execute('insert into operator values(2,"Hans","AB Road Guna",2312312311,"Hans@gmail.com")')
cur.execute('insert into operator values(3,"Rajratan","harinager delhi",4324324321,"Raj@gmail.com")')
cur.execute('insert into operator values(4,"Mohani","AB road jhasi",5435435432,"Mohani@gmail.com")')
con.commit()
cur.execute('Select * from operator')
operatorDetail=cur.fetchall()
print('operator details: ',operatorDetail)
cur.execute('create table route(routeid number,sid number,station_name varchar(25),PRIMARY KEY(routeid, sid))')
cur.execute('insert into route values(1,1,"Guna")')
cur.execute('insert into route values(1,2,"JP collage")')
cur.execute('insert into route  values(1,3,"Binaganj")')
cur.execute('insert into route  values(1,4,"Biora")')
cur.execute('insert into route  values(1,5,"Bhopal")')
cur.execute('insert into route  values(2,1,"Bhopal")')
cur.execute('insert into route  values(2,2,"Biora")')
cur.execute('insert into route  values(2,3,"Binaganj")')
cur.execute('insert into route  values(2,4,"JP collage")')
cur.execute('insert into route  values(2,5,"Guna")')
cur.execute('insert into route  values(3,1,"Delhi")')
cur.execute('insert into route  values(3,2,"Agra")')
cur.execute('insert into route  values(3,3,"Jhasi")')
cur.execute('insert into route  values(3,4,"Shivpuri")')
con.commit()
cur.execute('Select * from route')
routeDetail=cur.fetchall()
print('route details: ',routeDetail)
cur.execute('create table bus(busid INTEGER PRIMARY KEY AUTOINCREMENT,type VARCHAR(20),capacity number,fare number,opid number,routeid number,CONSTRAINT fk_operator FOREIGN KEY (opid) REFERENCES OPERATOR(opid),CONSTRAINT fk_route FOREIGN KEY (routeid) REFERENCES ROUTE(routeid))')
cur.execute('insert into bus values(1,"AC 2x2",30,1000,1,1)')
cur.execute('insert into bus values(2,"AC 3x2",50,800,1,2)')
cur.execute('insert into bus values(3,"non AC 2x2",30,600,1,3)')
cur.execute('insert into bus values(4,"non AC 2x2",30,600,1,4)')
con.commit()
cur.execute('Select * from bus')
busDetail=cur.fetchall()
print('bus details: ',busDetail)
cur.execute('create table run(busid INTEGER,rDate date,seatAvail number,PRIMARY KEY(busid,rDate ), CONSTRAINT fk_bus FOREIGN KEY (busid) REFERENCES bus(busid)')
cur.execute("""create table run(
        busid INTEGER, 
        RunsDate DATE, 
        seatAvail INTEGER, 
        PRIMARY KEY(busid, RunsDate), 
        CONSTRAINT fk_bus 
        FOREIGN KEY (busid) 
        REFERENCES bus(busid)
        )""")
cur.execute('insert into run values(1,"2022-11-20",30)')
cur.execute('insert into run values(1,"2022-11-21",30)')
cur.execute('insert into run values(1,"2022-11-22",30)')
cur.execute('insert into run values(4,"2022-11-23",30)')
cur.execute('insert into run values(2,"2022-11-24",30)')
cur.execute('insert into run values(2,"2022-11-25",30)')
cur.execute('insert into run values(3,"2022-11-26",30)')
cur.execute('insert into run values(4,"2022-11-27",30)')
cur.execute('insert into run values(5,"2022-11-28",30)')
cur.execute('insert into run values(6,"2022-11-29",30)')
cur.execute('insert into run values(5,"2022-11-30",30)')
cur.execute('insert into run values(6,"2022-12-1",30)')
con.commit()
cur.execute('Select * from run')
runDetail=cur.fetchall()
print('run details: ',runDetail)
cur.execute("""create table booking_history(
        ref_no INTEGER, 
        name TEXT, 
        gender TEXT,
        busid INTEGER, 
        no_of_seats INTEGER, 
        dbook TEXT,
        dstart TEXT, 
        age INTEGER,
        boarding TEXT,
        CONSTRAINT fk_bus 
        FOREIGN KEY (busid) 
        REFERENCES BUS(busid)
        )""")
cur.execute('insert into booking_history values(1,"Dev", "Male",1, 2, "2022-11-19", "2022-11-20", 19, "Guna")')
con.commit()
cur.execute('Select * from booking_history')
bookingDetail=cur.fetchall()
print('user details: ',bookingDetail)
con.commit()
