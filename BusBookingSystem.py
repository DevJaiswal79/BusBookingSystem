from tkinter import *
from tkinter.messagebox import *
from datetime import date
tdate=date.today()
import sqlite3
con = sqlite3.Connection('My_Database1')
cur=con.cursor()
class Test:
    
    #01home screen
    def home(self):	
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        img = PhotoImage(file='.\\Bus_for_project.png')
        Label(root,image=img).grid(row=1,column=0,padx=w//3,pady=30,columnspan=3,ipady=20)
        Label(root,text="Online Bus Booking System",font='Arial 30 bold',bg ='skyblue',fg='red').grid(row=2,column=0,padx=w//3)
        Label(root,text = " Name : Dev Jaiswal ",fg='blue',font='1').grid(row=6,column=0,padx=w//3,pady=25)
        Label(root,text = "  Er : 211B102 ",fg='blue',font='1').grid(row=7,column=0,padx=w//3)
        Label(root,text = " Mobile : 91655550023 ",font='1',fg='blue').grid(row=8,column=0,padx=w//3,pady=30)
        Label(root,text="").grid(row=9,column=0,padx=w//3)
        Label(root,text=" Submitted to : Dr Mahesh Kumar ",font='Arial 15 bold',bg ='skyblue',fg='red').grid(row=11,column=0,padx=w//3)
        Label(root,text=" Project Based Learning, ",fg='red',font='1').grid(row=12,column=0,padx=w//3)
        def closeHome(e=0):
            root.destroy()
            self.bookingPage()
        root.bind('<KeyPress>',closeHome) 
        root.mainloop()


    #02bookingSelectionPage
    def bookingPage(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        def seatBooking():
            root.destroy()
            self.seatBooking()
        def checkBooking():
            root.destroy()
            self.checkBooking()
        def addBusDetail():
            root.destroy()
            self.addBusDetails()
        Button(root,text=" Seat Booking ",command=seatBooking,font='Arial 18 bold',bg='pale green',height= 1, width=20).grid(row=3,column=3,pady=50)
        Button(root,text=" Checked Booked Seat ",command=checkBooking,font='Arial 18 bold',bg='lime green',height= 1, width=20).grid(row=3,column=4,pady=50)
        Button(root,text=" Add Bus Details ",command=addBusDetail,font='Arial 18 bold',bg='dark green',height= 1, width=20).grid(row=3,column=5,pady=50)
        Label(root,text="For Admin Only",font='Arial 16 bold',fg='red').grid(row=4,column=5)
        root.mainloop()


    #03SeatBookingPage
    def seatBooking(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='raised')
        head_fr.grid(row=4,column=3,padx=w//3)
        Label(head_fr,text="Enter Journey Details",font='Arial 20 bold',bg ='pale green',fg='green').grid(row=3,column=4)
        fr= Frame(root)
        fr.grid(row=9,column=0,pady=20,columnspan=20)
        Label(fr,text=" To ",font='Arial 14 bold').grid(row=5,column=3)
        start=Entry(fr,font='Arial 12 bold')
        start.grid(row=5,column=4,padx=20)
        Label(fr,text=" From ",font='Arial 14 bold').grid(row=5,column=5)
        end=Entry(fr,font='Arial 12 bold')
        end.grid(row=5,column=6,padx=20)
        Label(fr,text=" Journey Date ",font='Arial 14 bold').grid(row=5,column=7)
        date=Entry(fr,font='Arial 12 bold')
        date.grid(row=5,column=8,padx=20)
        mobile=IntVar()
        #funtion to transfer data to bticket 
        def getBus():
            
            #Attributes
            Label(fr,text="Select Bus", fg="green", font=("Arial Bold", 15)).grid(row=6,column=3, pady=40)
            Label(fr,text="Operator", fg="green", font=("Arial Bold", 15)).grid(row=6,column=4)
            Label(fr,text="Bus Type", fg="green", font=("Arial Bold", 15)).grid(row=6,column=5, padx=10)
            Label(fr,text="Availability/Capacity", fg="green", font=("Arial Bold", 15)).grid(row=6,column=6)
            Label(fr,text="Fare", fg="green", font=("Arial Bold", 15)).grid(row=6,column=7)
            istart=start.get()
            iend=end.get()
            idate=date.get()
            print(istart, iend, idate)
            data=cur.execute('''
                        select name,type,seatAvail,fare, b.busid
                        from operator as o,bus as b,run as r,route as t,route as f 
                        where o.opid=b.opid 
                        and r.RunsDate="{2}"
                        and b.busid=r.busid 
                        and t.routeid=b.routeid 
                        and t.station_name="{0}" 
                        and f.routeid=b.routeid 
                        and t.sid<f.sid
                        and seatAvail>0
                        and f.station_name="{1}" '''.format(istart,iend,idate))
            data=data.fetchall()
            print('Bus details: ',data)
            b=IntVar()
            for i in range(len(data)):
                boption=Radiobutton(fr,text="{}".format("Bus"+str(i+1)), variable=b, value=data[i][4], bg="lightblue" , font=("Arial Bold", 15)).grid(row=i+7,column=0, pady=10)
                Label(fr,text="{}".format(data[i][0]), fg="blue", font=("Arial Bold", 15)).grid(row=i+7,column=4)
                Label(fr,text="{}".format(data[i][1]), fg="blue", font=("Arial Bold", 15)).grid(row=i+7,column=5)
                Label(fr,text="{}".format(data[i][2]), fg="blue", font=("Arial Bold", 15)).grid(row=i+7,column=6)
                Label(fr,text="{}".format(data[i][3]), fg="blue", font=("Arial Bold", 15)).grid(row=i+7,column=7)
        #----------------------after showing bus result---------------------------
            def afterSelection():
                fr2= Frame(root)
                fr2.grid(row=10,column=0,pady=50,columnspan=20)
                Label(fr2,text="Fill Passenger Details to book the bus ticket",font='Arial 22 bold',bg ='skyblue',fg='red').grid(row=8,column=3,columnspan=20,pady=50)
                Label(fr2,text=" Name ",font='Arial 14 bold').grid(row=9,column=3)
                name=Entry(fr2,font='Arial 12 bold',width=15)
                name.grid(row=9,column=4,padx=5,ipadx=0)
                Label(fr2,text=" Gender ",font='Arial 14 bold').grid(row=9,column=5)
                gender=StringVar()
                opt=['Male','Female','Third Gender']
                g_drop_menu=OptionMenu(fr2,gender,*opt)
                g_drop_menu.grid(row=9,column=6,padx=5)
                #Entry(fr2,font='Arial 12 bold').grid(row=9,column=6,padx=5)
                Label(fr2,text=" No of Seats ",font='Arial 14 bold').grid(row=9,column=7)
                ns=Entry(fr2,font='Arial 12 bold',width=10)
                ns.grid(row=9,column=8,padx=5,ipadx=0)
                Label(fr2,text=" Mobile No ",font='Arial 14 bold').grid(row=9,column=9)
                mb=Entry(fr2,font='Arial 12 bold',width=15)
                mb.grid(row=9,column=10,padx=5)
                Label(fr2,text=" Age ",font='Arial 14 bold').grid(row=9,column=11)
                ag=Entry(fr2,font='Arial 12 bold',width=5)
                ag.grid(row=9,column=12,padx=5)
                    #04BusTicketConfirmPAge
                def seatConfirm(mob):
                    root = Tk()
                    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
                    root.geometry("%dx%d" % (w,h))
                    bus_frame = Frame(root);
                    bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
                    self.img = PhotoImage(file='.\\Bus_for_project.png')
                    Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
                    Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
                    head_fr = Frame(root)
                    head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
                    Label(head_fr,text="Bus Ticket",font='Arial 20 bold').grid(row=3,column=0,pady=5)
                    ticket_fr = Frame(root, borderwidth=1,relief='solid')
                    ticket_fr.grid(row=15,column=0,columnspan=10,pady=10)
                    
                    try:
                        print(mobile)
                        data=cur.execute("SELECT * FROM booking_history WHERE ref_no={}".format(mob))
                        userdata=data.fetchall()
                    except:
                        showerror("Invalid Input", message="Unacceptable Input.")
                    print("out of if")
                    if len(userdata)!=0:
                        print("inside if", len(userdata))
                        for i in range(len(userdata)):
                            data=cur.execute("SELECT * FROM bus WHERE busid={}".format(userdata[i][3]))
                            busdata=data.fetchall()
                            data=cur.execute("SELECT name FROM operator WHERE opid={}".format(busdata[0][4])) 
                            odata=data.fetchall()
                            print(userdata[i][1], "Here")
                            Label(ticket_fr,text='Passenger : {}'.format(userdata[i][1]),font='Arial 14 bold').grid(row=7,column=0)
                            Label(ticket_fr,text='Gender : {}'.format(userdata[i][2]),font='Arial 14 bold').grid(row=7,column=1)
                            Label(ticket_fr,text='No of seats : {}'.format(userdata[i][4]),font='Arial 14 bold').grid(row=8,column=0)
                            Label(ticket_fr,text='Phone : {}'.format(userdata[i][0]),font='Arial 14 bold').grid(row=8,column=1)
                            Label(ticket_fr,text='Age : {} '.format(userdata[i][7]),font='Arial 14 bold').grid(row=9,column=0)
                            Label(ticket_fr,text='Fare Rs : {}'.format(busdata[0][3]*userdata[i][4]),font='Arial 14 bold').grid(row=9,column=1)
                            Label(ticket_fr,text='Booking Ref: {}'.format(userdata[i][0]),font='Arial 14 bold').grid(row=10,column=0)
                            Label(ticket_fr,text=' Bus Details : {}'.format(odata[0][0]),font='Arial 14 bold').grid(row=10,column=1)
                            Label(ticket_fr,text='Travel On: {} '.format(userdata[i][6]),font='Arial 14 bold').grid(row=11,column=0)
                            Label(ticket_fr,text=' Booked On : {}'.format(tdate),font='Arial 14 bold').grid(row=11,column=1)
                            Label(ticket_fr,text='No of seats : {}'.format(userdata[i][4]),font='Arial 14 bold').grid(row=12,column=0)
                            Label(ticket_fr,text='Boarding Point : {}'.format(userdata[i][8]),font='Arial 14 bold').grid(row=12,column=1)
                            Label(ticket_fr,text=' *Total amount Rs {}/ to be paid at time of boarding te bus'.format(busdata[0][3]*userdata[i][4]),font='Arial 11').grid(row=13,column=0,columnspan=2)
                            showinfo('Success','Seat Booked....')
                def add_book(mob):
                    cur.execute("insert into booking_history values({}, '{}', '{}', {}, {}, '{}', '{}', {}, '{}')".format(mb.get(), name.get(), gender.get(), b.get(), ns.get(), tdate, date.get(), ag.get(), start.get()))
                    cur.execute("update run SET seatAvail=seatAvail- {} where busid={} and RunsDate='{}'".format(ns.get(), b.get(), date.get()))
                    con.commit()
                    root.destroy()
                    seatConfirm(mob)
                def confirm():
                    print(mb.get(), "mobile")
                    mob=mb.get()
                    fare=cur.execute("Select fare from bus where busid={}".format(b.get())) 
                    fare=fare.fetchall()
                    f=fare[0][0]*int(ns.get())
                    flag=askyesno("Fare Confirm",message="Total amount to be paid Rs {}".format(f))
                    if flag:
                        add_book(mob)
                print(b.get(), start.get(), date)
                    
                Button(fr2,command=confirm,text=" Book seat ",font='Arial 14 bold',bg='Pale green1').grid(row=9,column=13,padx=10)
            # def afterSelection():
            #     bticket(b.get(),istart, idate)
            proceed=Button(fr, text="Proceed to Book",command=afterSelection, bg="seagreen2", font=15).grid(row=i+7, column=9,padx=30)
            # Label(root, text="{}".format(operatorDetail[0][0]+" "+operatorDetail[0][1])+" "+str(operatorDetail[0][2])+" "+str(operatorDetail[0][3])).pack()
            
        
        Button(fr,text=" Show Bus ",command=getBus,font='Arial 14 bold',bg='sea green3').grid(row=5,column=9)
        self.home_img = PhotoImage(file='.\\home.png')
        def home():
            root.destroy()
            self.bookingPage()
        Button(fr,command=home,image=self.home_img).grid(row=5,column=10,padx=20)
        con.commit()
        
        
        
    #05checkBookingPage
    def checkBooking(self):
        def notBooking():
            res=askyesno('No Booking Record','Do you want to book seat now ?')
            if res:
                root.destroy()
                self.seatBooking()
        def seatConfirm():
            head_fr = Frame(root)
            head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
            ticket_fr = Frame(root, borderwidth=1,relief='solid')
            ticket_fr.grid(row=15,column=0,columnspan=10,pady=10)
            
            try:
                print(mob.get())
                data=cur.execute("SELECT * FROM booking_history WHERE ref_no={}".format(mob.get()))
                userdata=data.fetchall()
            except:
                showerror("Invalid Input", message="Unacceptable Input.")
            print("out of if")
            if len(userdata)!=0:
                print("inside if", len(userdata))
                for i in range(len(userdata)):
                    data=cur.execute("SELECT * FROM bus WHERE busid={}".format(userdata[i][3]))
                    busdata=data.fetchall()
                    data=cur.execute("SELECT name FROM operator WHERE opid={}".format(busdata[0][4])) 
                    odata=data.fetchall()
                    print(userdata[i][1], "Here")
                    Label(ticket_fr,text='Passenger : {}'.format(userdata[i][1]),font='Arial 14 bold').grid(row=7,column=0)
                    Label(ticket_fr,text='Gender : {}'.format(userdata[i][2]),font='Arial 14 bold').grid(row=7,column=1)
                    Label(ticket_fr,text='No of seats : {}'.format(userdata[i][4]),font='Arial 14 bold').grid(row=8,column=0)
                    Label(ticket_fr,text='Phone : {}'.format(userdata[i][0]),font='Arial 14 bold').grid(row=8,column=1)
                    Label(ticket_fr,text='Age : {} '.format(userdata[i][7]),font='Arial 14 bold').grid(row=9,column=0)
                    Label(ticket_fr,text='Fare Rs : {}'.format(busdata[0][3]*userdata[i][4]),font='Arial 14 bold').grid(row=9,column=1)
                    Label(ticket_fr,text='Booking Ref: {}'.format(userdata[i][0]),font='Arial 14 bold').grid(row=10,column=0)
                    Label(ticket_fr,text=' Bus Details : {}'.format(odata[0][0]),font='Arial 14 bold').grid(row=10,column=1)
                    Label(ticket_fr,text='Travel On: {} '.format(userdata[i][6]),font='Arial 14 bold').grid(row=11,column=0)
                    Label(ticket_fr,text=' Booked On : {}'.format(tdate),font='Arial 14 bold').grid(row=11,column=1)
                    Label(ticket_fr,text='No of seats : {}'.format(userdata[i][4]),font='Arial 14 bold').grid(row=12,column=0)
                    Label(ticket_fr,text='Boarding Point : {}'.format(userdata[i][8]),font='Arial 14 bold').grid(row=12,column=1)
                    Label(ticket_fr,text=' *Total amount Rs {}/ to be paid at time of boarding te bus'.format(busdata[0][3]*userdata[i][4]),font='Arial 11').grid(row=13,column=0,columnspan=2)
                    # showinfo('Success','Seat Booked....')
            else:
                notBooking()
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='solid')
        head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
        Label(head_fr,text="Check Your Booking",font='Arial 20 bold',bg ='pale green',fg='green', borderwidth=1,relief='flat').grid(row=3,column=0)
        fr=Frame(root)
        fr.grid(row=5,column=0,padx=w//3,columnspan=10,pady=25)
        Label(fr,text="Enter your Mobile No: ",font='Arial 14 bold').grid(row=4,column=0)
        mob=Entry(fr,font='Arial 15 ')
        mob.grid(row=4,column=1)
        Button(fr,text=" Check Booking ",command=seatConfirm,font='Arial 14 bold').grid(row=4,column=2,padx=20)
        self.home_img = PhotoImage(file='.\\home.png')
        def home():
            root.destroy()
            self.bookingPage()
        Button(fr,command=home,image=self.home_img).grid(row=4,column=5,padx=25)
#------------after entering  number------------------------------
        # ticket_fr = Frame(root, borderwidth=1,relief='solid')
        # ticket_fr.grid(row=15,column=0,columnspan=10)
        # Label(ticket_fr,text='Passenger : Dev jaiswal',font='Arial 14 bold').grid(row=7,column=0)
        # Label(ticket_fr,text='Gender : Male',font='Arial 14 bold').grid(row=7,column=1)
        # Label(ticket_fr,text='No of seats : 3 ',font='Arial 14 bold').grid(row=8,column=0)
        # Label(ticket_fr,text='Phone : 8888888889',font='Arial 14 bold').grid(row=8,column=1)
        # Label(ticket_fr,text='Age : 22 ',font='Arial 14 bold').grid(row=9,column=0)
        # Label(ticket_fr,text='Fare Rs : 3000',font='Arial 14 bold').grid(row=9,column=1)
        # Label(ticket_fr,text='Booking Ref: 9 ',font='Arial 14 bold').grid(row=10,column=0)
        # Label(ticket_fr,text=' Bus Details : Kamla',font='Arial 14 bold').grid(row=10,column=1)
        # Label(ticket_fr,text='Travel On: 24/12/2022 ',font='Arial 14 bold').grid(row=11,column=0)
        # Label(ticket_fr,text=' Booked On : oct 31 2022',font='Arial 14 bold').grid(row=11,column=1)
        # Label(ticket_fr,text='Destination Point : Bhopal ',font='Arial 14 bold').grid(row=12,column=0)
        # Label(ticket_fr,text='Boarding Point : Guna',font='Arial 14 bold').grid(row=12,column=1)
        # Label(ticket_fr,text=' *Total amount Rs 3000.00/ to be paid at time of boarding te bus',font='Arial 11').grid(row=13,column=0,columnspan=2)

        
    #06AddBusDetailsPage
    def addBusDetails(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='sunken')
        head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
        Label(head_fr,text="Add New Details to DataBase",font='Arial 20 bold',fg='green').grid(row=3,column=0)
        b_fr=Frame(root)
        b_fr.grid(row=5,column=0,columnspan=10,pady=45)
        def addNewOperator():
            root.destroy()
            self.addNewOperator()
        def addNewBus():
            root.destroy()
            self.addNewBus()
        def addNewRoute():
            root.destroy()
            self.addNewRoute()
        def addNewRun():
            root.destroy()
            self.addNewRun()
        Button(b_fr,text=" New Operator ",command=addNewOperator,font='Arial 16 ',bg='Pale green2').grid(row=4,column=0,padx=45)
        Button(b_fr,text=" New Bus ",font='Arial 16 ',command=addNewBus,bg='Orange red').grid(row=4,column=1,padx=45)
        Button(b_fr,text=" New Route ",font='Arial 16 ', command=addNewRoute,bg='Royal blue1').grid(row=4,column=2,padx=45)
        Button(b_fr,text=" New Run ",font='Arial 16 ',command=addNewRun,bg='Hotpink1').grid(row=4,column=3,padx=45)

    
    #07AddNewOperatorPage
    def addNewOperator(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='sunken')
        head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
        Label(head_fr,text="Add Bus Operator Details",font='Arial 24 bold',fg='green').grid(row=3,column=0)
        details_fr= Frame(root)
        details_fr.grid(row=5,column=0,pady=70,columnspan=10)
        Label(details_fr,text=" Operator id ",font='Arial 14 bold').grid(row=4,column=0)
        opid1=Entry(details_fr,font='Arial 12 bold',width=8)
        opid1.grid(row=4,column=1)
        Label(details_fr,text=" Name ",font='Arial 14 bold').grid(row=4,column=2)
        name=Entry(details_fr,font='Arial 12 bold',width=15)
        name.grid(row=4,column=3)
        Label(details_fr,text=" Address ",font='Arial 14 bold').grid(row=4,column=4)
        address=Entry(details_fr,font='Arial 12 bold',width=15)
        address.grid(row=4,column=5)
        Label(details_fr,text=" Phone ",font='Arial 14 bold').grid(row=4,column=6)
        phn=Entry(details_fr,font='Arial 12 bold',width=15)
        phn.grid(row=4,column=7)
        Label(details_fr,text=" Email ",font='Arial 14 bold').grid(row=4,column=8)
        mail=Entry(details_fr,font='Arial 12 bold',width=15)
        mail.grid(row=4,column=9)
        
        #add Bus Operator function
        def add():
            try:
                iopid=opid1.get()
                iname=name.get()
                iaddress=address.get()
                iphn=phn.get()
                print("phone ", iphn)
                imail=mail.get()        
                cur.execute("insert into operator values({},'{}','{}','{}',{})".format(iopid,iname,iaddress,imail,iphn))
                Label(details_fr, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn))).grid(row=5,column=4)
                showinfo("Operator Entry", message="Operator Record Added")
                con.commit()
            except:
                showerror("DB insertion Error", message="Operator Record Already Exists")

        Button(details_fr,text=" Add ",command=add,font='Arial 14 bold',bg='Pale green1').grid(row=4,column=11,padx=10)
        #edit Bus Operator function
        def edit():
            try:
                iopid=opid1.get()
                iname=name.get()
                iaddress=address.get()
                iphn=phn.get()
                imail=mail.get()
                cur.execute("update operator set name='{1}',address='{2}',email='{3}',phone={4} where opid={0}".format(iopid1,iname,iaddress,imail,iphn))       
                Label(details_fr, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn))).grid(row=5,column=4)
                showinfo("Operator Entry Updated", message="Operator Record updated Successfully")
                con.commit()
            except:
                showerror("Record Not Found", message="Operator Record does not Exists")
        Button(details_fr,text=" Edit ",command=edit,font='Arial 14 bold',bg='Pale green1').grid(row=4,column=12,padx=10)

        def home():
            root.destroy()
            self.bookingPage()
        home_img = PhotoImage(file='.\\home.png')
        Button(details_fr,image=home_img,command=home).grid(row=5,column=8,columnspan=3,pady=60)
        root.mainloop()


    #08AddNewBusPage
    def addNewBus(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='sunken')
        head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
        Label(head_fr,text="Add Bus Details",font='Arial 24 bold',fg='green').grid(row=3,column=0)
        details_fr= Frame(root)
        details_fr.grid(row=5,column=0,pady=70,columnspan=10)
        Label(details_fr,text=" Bus id ",font='Arial 14 bold').grid(row=4,column=0)
        busid=Entry(details_fr,font='Arial 12 bold',width=6)
        busid.grid(row=4,column=1,padx=20)
        Label(details_fr,text=" Bus Type ",font='Arial 14 bold').grid(row=4,column=2)
        Bus_Type = StringVar()
        Bus_Type.set("Select Bus Type")
        drop = OptionMenu(details_fr, Bus_Type, 'AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2','AC-Sleeper 2X1','Non-AC Sleeper 2X1')
        drop.grid(row=4,column=3,padx=20)
        Label(details_fr,text=" Capacity ",font='Arial 14 bold').grid(row=4,column=4)
        capacity=Entry(details_fr,font='Arial 12 bold',width=6)
        capacity.grid(row=4,column=5,padx=20)
        Label(details_fr,text=" Fare Rs ",font='Arial 14 bold').grid(row=4,column=6)
        fare=Entry(details_fr,font='Arial 12 bold',width=10)
        fare.grid(row=4,column=7,padx=20)
        Label(details_fr,text=" Operator ID ",font='Arial 14 bold').grid(row=4,column=8)
        opid1=Entry(details_fr,font='Arial 12 bold',width=8)
        opid1.grid(row=4,column=9,padx=20)
        Label(details_fr,text=" Route ID ",font='Arial 14 bold').grid(row=4,column=10)
        routeid=Entry(details_fr,font='Arial 12 bold',width=8)
        routeid.grid(row=4,column=11,padx=20)
        def add():
            try:
                ibusid=busid.get()
                ibustype=Bus_Type.get()
                icapacity=capacity.get()
                ifare=fare.get()
                print("phone ", iphn)
                iopid=opid1.get()        
                cur.execute("insert into bus values({},'{}','{}','{}',{})".format(ibusid,ibustype,icapacity,ifare,iopid))
                Label(details_fr, text="{}".format(str(busid)+" "+str(bustype)+" "+str(icapacity)+" "+str(ifare)+" "+str(iopif))).grid(row=5,column=4)
                showinfo("Operator Entry", message="Operator Record Added")
                con.commit()
            except:
                showerror("DB insertion Error", message=" Record Already Exists")
        def edit():
            # try:
            #     iopid=opid1.get()
            #     iname=name.get()
            #     iaddress=address.get()
            #     iphn=phn.get()
            #     imail=mail.get()
            #     cur.execute("update operator set name='{1}',address='{2}',email='{3}',phone={4} where opid={0}".format(iopid1,iname,iaddress,imail,iphn))       
            #     Label(details_fr, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn))).grid(row=5,column=4)
            #     showinfo("Operator Entry Updated", message="Operator Record updated Successfully")
            #     con.commit()
            # except:
            showerror("Record Not Found", message="bus Record does not Exists")
                
        Button(details_fr,text=" Add ",command=add,font='Arial 14 bold',bg='Pale green1').grid(row=5,column=5,padx=10,pady=40)
        def edit():
            showinfo('Bus entry update','Bus record updated succesfully')
        def home():
            root.destroy()
            self.bookingPage()
        Button(details_fr,text=" Edit ",font='Arial 14 bold',command=edit,bg='Pale green1').grid(row=5,column=6,padx=10,pady=40)
        home_img = PhotoImage(file='.\\home.png')
        Button(details_fr,image=home_img,command=home).grid(row=5,column=7,padx=15,pady=40)
        root.mainloop()


    #09AddNewRoutePage
    def addNewRoute(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='sunken')
        head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
        Label(head_fr,text="Add Bus Route Details",font='Arial 24 bold',fg='green').grid(row=3,column=0)
        details_fr= Frame(root)
        details_fr.grid(row=5,column=0,pady=70,columnspan=10)
        Label(details_fr,text=" Route id ",font='Arial 14 bold').grid(row=4,column=0)
        Entry(details_fr,font='Arial 12 bold',width=5).grid(row=4,column=1,padx=10)
        Label(details_fr,text=" Station Name ",font='Arial 14 bold').grid(row=4,column=2)
        Entry(details_fr,font='Arial 12 bold',width=20).grid(row=4,column=3,padx=10)
        Label(details_fr,text=" Station Id ",font='Arial 14 bold').grid(row=4,column=4)
        Entry(details_fr,font='Arial 12 bold',width=12).grid(row=4,column=5,padx=10)
        Button(details_fr,text=" Add Route",font='Arial 14 bold',bg='Pale green1').grid(row=4,column=6,padx=20)
        def delete():
            showinfo('Route entry ','Route record deleted')
        def home():
            root.destroy()
            self.bookingPage()
        Button(details_fr,text=" Delete Route ",command=delete,font='Arial 14 bold',bg='Pale green1',fg='red').grid(row=4,column=7)
        home_img = PhotoImage(file='.\\home.png')
        Button(details_fr,image=home_img,command=home).grid(row=5,column=5,columnspan=3,pady=60)
        root.mainloop()


    #10AddNewRunPage
    def addNewRun(self):
        root = Tk()
        w,h = root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d" % (w,h))
        bus_frame = Frame(root);
        bus_frame.grid(row=2,column=0,columnspan=10,padx=w//3,pady=50)
        self.img = PhotoImage(file='.\\Bus_for_project.png')
        Label(bus_frame,image=self.img).grid(row=1,column=0,columnspan=10)
        Label(bus_frame,text="Online Bus Booking System",font='Arial 32 bold',bg ='skyblue',fg='red').grid(row=2,column=3,columnspan=3)
        head_fr = Frame(root, borderwidth=1,relief='sunken')
        head_fr.grid(row=3,column=0,padx=w//3,columnspan=10)
        Label(head_fr,text="Add Bus Running Details",font='Arial 24 bold',fg='green').grid(row=3,column=0)
        details_fr= Frame(root)
        details_fr.grid(row=5,column=0,pady=70,columnspan=10)
        Label(details_fr,text=" Bus Id ",font='Arial 14 bold').grid(row=4,column=0)
        Entry(details_fr,font='Arial 12 bold',width=8).grid(row=4,column=1,padx=10)
        Label(details_fr,text=" Running Date ",font='Arial 14 bold').grid(row=4,column=2)
        Entry(details_fr,font='Arial 12 bold',width=15).grid(row=4,column=3,padx=10)
        Label(details_fr,text=" Seat Available ",font='Arial 14 bold').grid(row=4,column=4)
        Entry(details_fr,font='Arial 12 bold',width=15).grid(row=4,column=5,padx=10)
        Button(details_fr,text=" Add Run",font='Arial 14 bold',bg='Pale green1').grid(row=4,column=6,padx=20)
        def delete():
            showinfo('Run entry delete','Run record deleted')
        def home():
            root.destroy()
            self.bookingPage()
        Button(details_fr,text=" Delete Run ",command=delete,font='Arial 14 bold',bg='Pale green1',fg='red').grid(row=4,column=7)
        home_img = PhotoImage(file='.\\home.png')
        Button(details_fr,image=home_img,command=home).grid(row=5,column=5,columnspan=3,pady=60)
        root.mainloop()

        root.mainloop()


t=Test()
t.home()
con.close()
