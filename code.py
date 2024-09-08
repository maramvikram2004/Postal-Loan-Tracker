from tkinter import * #to import all tkkinter modules
from tkinter import messagebox #to import messagebox used for pop up dialogue boxes or warning signs
import sqlite3 #for sql usage
#import bfs
con=sqlite3.Connection("postofficeDB") #connect with a database
cur=con.cursor() #cursor is created from the cursor object
cur.execute('create table if not exists post(accno number(10),accname varchar2(10),denom number(7),mupto number(60),duedate date)')
#create a table named post in the database
def paswrd_checker():
    if pswrd.get()=='123' and pswr.get() =='vikram': #check for authentication
        login.destroy() #shut the login page
        po1() #open the menu page
    else:
        messagebox.showerror('Error','Wrong Credential') #pop up box saying incorrect credentials

def po1():
    global po
    po=Tk()
    po.geometry('800x600')
    po.configure(bg='black')
    po.title('My Way Post')
    pic = PhotoImage(file="abt.png")
    Label(po,image=pic).grid(row=0,column=0,rowspan=10,columnspan=6)

    Button(po, text="Logoff",command=logoff,bd=10,bg='#2c1052',fg='blue').grid(row=5, column=2)
    Label(po,text='Choose option',font="Century 20 bold",bg='#311a4e',fg='white').grid(row=0,column=0)
    Button(po, text="Add Client",command=addclient,font="Century 20 bold",bd=10,bg='#2c1052',fg='blue').grid(row=2, column=0)
    Button(po, text="Modify",command=modify,font="Century 20 bold",bd=10,bg='#2c1052',fg='blue').grid(row=2, column=1)
    Button(po, text="Search",command=search,font="Century 20 bold",bd=10,bg='#2c1052',fg='blue').grid(row=2, column=2)
    Button(po, text="Backup",command=backup,font="Century 20 bold",bd=10,bg='#2c1052',fg='blue').grid(row=4, column=2)
    Button(po, text="Contact",command=contact,font="Century 20 bold",bd=10,bg='#2c1052',fg='blue').grid(row=4, column=0)
    Button(po, text="About",command=about,font="Century 20 bold",bd=10,bg='#2c1052',fg='blue').grid(row=4, column=1)
    po.mainloop()
def logoff():
    con.commit()
    po.destroy()
    logon()
def backup():
    con.commit()
    messagebox.showinfo('Backup','Backed up Successfully please re-Login')
    po.destroy()
    logon()
def about():
    po.destroy()
    abt=Tk()
    abt.title("about")
    pic=PhotoImage(file="aboutus.png")
    Label(abt,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    def me1():
        Label(abt,text='Tamogh and Vikram Application Developer',bg='red').grid(row=2,column=0)
    def sir1():
        Label(abt,text='Dr. Shalini Batra, Head CSED',bg='red').grid(row=2,column=4)
    Label(abt,text='Credit goes  To:-',bg='dark slate gray').grid(row=5,column=0,sticky='W')
    Label(abt,text=' Tamogh and Vikram',bg='pink').grid(row=6,column=0,sticky='E')
    def exitc():
        abt.destroy()
        po1()
    Button(abt,text='close',command=exitc,bg='saddle brown').grid(row=8,column=5)
    abt.mainloop()
def contact():
    po.destroy()
    cont=Tk()
    cont.title('Contact')
    pic=PhotoImage(file="abt.png")
    cont.geometry('800x600')
    Label(cont,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    Label(cont,text='For Any Help Contact Through Given Below Details',bg='yellow green').grid(row=2)
    Label(cont,text='Vikram Maram, Devlopment Manager',bg='yellow green').grid(row=3)
    Label(cont,text='Email :-',bg='yellow green').grid(row=4,column=0)
    Label(cont,text='maramvikram2004@gmail.com',bg='yellow green').grid(row=4,column=1)
    Label(cont,text='Phone(office)',bg='yellow green').grid(row=5,column=0)
    Label(cont,text='+91 6309435918',bg='yellow green').grid(row=5,column=1)
    def exitc():
        cont.destroy()
        po1()
    Button(cont,text='close',command=exitc,bg='yellow green').grid(row=6,column=1)
    cont.mainloop()
def search():
    global search
    po.destroy()
    srch=Tk()
    global s
    srch.title('Search')
    srch.configure(bg='red')
    j=PhotoImage(file="abt.png")
    srch.geometry('800x600')
    Label(srch,image=j).grid(row=0,column=0,rowspan=10,columnspan=10)
    Label(srch,text='Detail finding  portal',font='Harrington 14 bold',bg='blue').grid(row=3,column=2)
    Label(srch,text='Enter the account no.',font='Harrington 10 bold',bg='blue').grid(row=4,column=1)
    s=Entry(srch,bg='LightCyan4')
    s.grid(row=4,column=2)
    Button(srch, text='Search',font='Harrington 10 bold',command=find,bg='blue').grid(row=4, column=3)
    def exitc():
        srch.destroy()
        po1()
    Button(srch,text='close',font='Harrington 10 bold',command=exitc,bg='blue').grid(row=6,column=3)
    srch.mainloop()
def find():
    k=int(s.get())
    print (k)
    global a
    cur.execute('select * from post where accno=(?)',(k,))
    a=cur.fetchone()
    print (a)
    amount=str(int(a[2])*int(a[3]))
    print (amount)
    messagebox.showinfo('Info',message='    Account no. - '+str(a[0])+' \nAccount name - '+ a[1] +' \nDenomination - '+str(a[2])+'  \nTotal amount paid - '+amount+'    \nDue date - '+a[4])

def modify():
    global s
    global modify
    global a
    po.destroy()
    modify=Tk()
    modify.title('Modification Portal')
    pic=PhotoImage(file="abt.png")
    modify.geometry('800x600')
    Label(modify,image=pic).grid(row=0,column=0,rowspan=15,columnspan=15)
    Label(modify,text='Modification Portal',font='Harrington 14 bold',bg='red').grid(row=4,column=1)
    Label(modify,text='Enter the account no.',font='Harrington 10 bold',bg='dark olive green').grid(row=5,column=0)
    s=Entry(modify,bg='orange2')
    s.grid(row=5,column=1)
    Button(modify, text='check',font='Harrington 10 bold',command=find,bg='dark olive green').grid(row=5, column=2)
    v=IntVar()
    Label(modify,text='Select the one which u wanna modify',font='Harrington 10 bold',bg='dark olive green').grid(row=6,column=1)
    Radiobutton(modify,text='Account no',font='Harrington 10 bold',variable=v,value=1,bg='dark olive green').grid(row=7,column=0)
    Radiobutton(modify,text='Account name',font='Harrington 10 bold',variable=v,value=2,bg='dark olive green').grid(row=7,column=1)
    Radiobutton(modify,text='Denomination',font='Harrington 10 bold',variable=v,value=3,bg='dark olive green').grid(row=7,column=2)
    Radiobutton(modify,text='Months Paid upto',font='Harrington 10 bold',variable=v,value=4,bg='dark olive green').grid(row=8,column=0)
    Radiobutton(modify,text='Next Installment Due',font='Harrington 10 bold',variable=v,value=5,bg='dark olive green').grid(row=8,column=1)

    def update():
        global l
        if v.get()==1:
            Label(modify,text='Enter the account no. to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=9,column=1,sticky='EW')
            m='acno'
            l=Entry(modify)
            l.grid(row=10,column=1)
        if v.get()==2:
            Label(modify,text='Enter the account name to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=9,column=1,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)

        if v.get()==3:
            Label(modify,text='Enter the denomination to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=9,column=1,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)

        if v.get()==4:
            Label(modify,text='Enter the months paid upto to which u wanna modify- ',bg='dark sea green').grid(row=9,column=1,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)

        if v.get()==5:
            Label(modify,text='Enter the next due date to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=9,column=1,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)
    def done():
        if v.get()==1:
            m=(int(l.get()),a[0])
            print (m)
            cur.execute('update post set accno =(?) where accno=(?)',m)
            con.commit()
            messagebox.showinfo(title='Modify Result',message='Modification Successful')
        if v.get()==2:
            m=(str(l.get()),a[0])
            print (m)
            cur.execute('update post set accname =(?) where accno=(?)',m)
            messagebox.showinfo(title='Modify Result',message='Modification Successful')
            con.commit()
        if v.get()==3:
            m=(int(l.get()),a[0])
            print (m)
            cur.execute('update post set denom =(?) where accno=(?)',m)
            messagebox.showinfo(title='Modify Result',message='Modification Successful')
            con.commit()

        if v.get()==4:
            m=(int(l.get()),a[0])
            print (m)
            cur.execute('update post set mupto =(?) where accno=(?)',m)
            messagebox.showinfo(title='Modify Result',message='Modification Successful')
            con.commit()
        if v.get()==5:
            m=(str(l.get()),a[0])
            print (m)
            cur.execute('update post set duedate =(?) where accno=(?)',m)
            messagebox.showinfo(title='Modify Result',message='Modification Successful')
            con.commit()
    Button(modify,text='Done',font='Harrington 10 bold',command=done,bg='sienna3').grid(row=10,column=2)
    Button(modify,text='Next',font='Harrington 10 bold',command=update,bg='sienna3').grid(row=8,column=2)
    def exitc():
        modify.destroy()
        po1()
    Button(modify,text='close',font='Harrington 10 bold',command=exitc,bg='DarkOrange1').grid(row=12,column=2)
    modify.mainloop()
def addclient():
    global insert
    po.destroy()
    insert=Tk()
    pic=PhotoImage(file="abt.png")
    insert.geometry('800x600')
    Label(insert,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    insert.title('Insert Details Of Client')
    Label(insert,text='Account No. ',font=("Arial Bold", 15),bg='#311a4e',fg='white').grid(row=1,column=1, sticky='w')
    acno=Entry(insert,bg='dodger blue')
    acno.grid(row=1,column=2)
    Label(insert,text='Account Name ',font=("Arial Bold", 15),bg='#311a4e',fg='white').grid(row=2,column=1, sticky='w')
    acname=Entry(insert,bg='dodger blue')
    acname.grid(row=2,column=2)
    Label(insert,text='Denomination ',font=("Arial Bold", 15),bg='#311a4e',fg='white').grid(row=3,column=1, sticky='w')
    denom=Entry(insert,bg='dodger blue')
    denom.grid(row=3,column=2)
    Label(insert,text='Months Paid Upto',font=("Arial Bold", 15),bg='#311a4e',fg='white').grid(row=4,column=1, sticky='w')
    mpo=Entry(insert,bg='dodger blue')
    mpo.grid(row=4,column=2)
    Label(insert,text='Next RD Installment Due Date',font=("Arial Bold", 15),bg='#311a4e',fg='white').grid(row=5,column=1, sticky='w')
    duedate=Entry(insert,bg='dodger blue')
    duedate.grid(row=5,column=2)
    def done():
          tup=(int(acno.get()),str(acname.get()),int(denom.get()),int(mpo.get()),str(duedate.get()))
          cur.execute('insert into post values(?,?,?,?,?)',tup)
          con.commit()
          messagebox.showinfo('Inserted Record',tup)
          insert.destroy()
          po1()
    Button(insert,text='DONE',command=done,bg='dodger blue').grid(row=6,column=2)
    def exitc():
        insert.destroy()
        po1()
    Button(insert,text='close',command=exitc,bg='red').grid(row=6,column=1)
    insert.mainloop()


def logon():

    global pswrd
    global pswr
    global login
    login=Tk()
    login.title('MY WAY POST LOGIN')
    login.geometry('760x595')
    pic=PhotoImage(file="abt.png")
    pic1=Label(login,image=pic)
    pic1.grid(row=0,column=0,rowspan=18,columnspan=12)
    Label(login, text='Welcome to Mail Management',font=('Century 10 bold',20),bd=10,bg='#311a4e',fg='white',).grid(row=1, column=1)

    import datetime
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    activebackground="#badee2"

    
    #Button(login,text='close',bg='grey',command=login.destroy).grid(row=0,column=0,sticky='E')
    Button(login,text='Login',command=paswrd_checker,font='Century 10 bold',bd=10,bg='#311a4e',fg='white').grid(row=6,column=1)
    pswrd=Entry(show='*')
    pswr=Entry(show='')
    Label(login, text='Password ',font='Century 10 bold',bd=10,bg='#311a4e',fg='white' ).grid(row=5, column=0)
    Label(login, text='User ID ',font='Century 10 bold',bd=10,bg='#311a4e',fg='white' ).grid(row=4, column=0)
    pswrd.grid(row=5,column=1)
    pswr.grid(row=4, column=1,)

    login.mainloop()

logon()
