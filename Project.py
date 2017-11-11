from Tkinter import *                                                                                #importing a Header file to Add GUI effect To the Program 
from tkMessageBox import *                                                                           #importing a Header file to add Error Dialog Box And Various others
from random import randint
import sqlite3                                                                                       #importing a Header file to give connectiviity to The data base
con=sqlite3.Connection('database2')                                                                  #creating a Connection with The database
cur=con.cursor()                                                                                     #creating a Cursor for the database
root = Tk()                                                                                          #creating a Canvas to add image to the front page
root.title('Banking System')
root.config(bg='Black')
cur.execute("Create table if not exists Account ( Acc_no Number Primary key, f_name char(20),L_name char(20),P_address varchar(50),C_address char(50),Amount float(2),type char(10),Phno number(10),a_Phno number(10),Pin varchar(30))")
canvas = Canvas(root,width=1360,height=400,bg='Black')                                             
canvas.grid(row = 0,columnspan=32)
photo = PhotoImage(file = 'Welcome.gif')
image1=canvas.create_image(650,200, image=photo)
def exi():
    showinfo(title='Exit',message='Thank you for visiting')
    root.destroy()
def create():
    def sql_create(v1):                                                                             #function Create Will Execute SQL command and save the Entries to the database
        if(((e3.get())=='') or ((e4.get())=='' )or ((e5.get())=='') or ((e6.get())=='') or ((e7.get())=='') or ((e9.get())=='') or ((e10.get())=='') or ((e11.get())=='')):
            showinfo(title="Invalid",message='All Fields Are Mandatory')
        elif not (e3.get().isalpha() and e4.get().isalpha()):
            showinfo(title='INVALID ENTRY',message='The Name Must only Contain Alphabets')
        elif  (e7.get().isalpha()):
            showinfo(title='INVALID ENTRY',message='The Amount Should not Contain Alphabets')
        elif (e10.get().isalpha() and e9.get().isalpha()):
            showinfo(title='INVALID ENTRY',message='The Phone Number Should not contain Alphabets')
        elif(len(e10.get())!=10):
            showinfo(title='Invalid',message='Invalid Alternate Phone Number')
        elif not (len(e11.get())>6 and len(e11.get())<30):
            showinfo(title='Invalid',message='Invalid Password Length the Password Must be between 6 to 30 characters')
        elif(len(e9.get())!=10):
            showinfo(title="Invalid",message='Invalid Phone Number')
        else:
            if(v1==1):
                h='Saving'
            else:
                h='Current'
            l=(a,e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),h,e9.get(),e10.get(),e11.get())
            cur.execute("insert into Account values(?,?,?,?,?,?,?,?,?,?)",l)
            con.commit()                                                                                 #con.commit() is used to save the changes made in the database
            showinfo(title="Created",message='Account Was Created Successfully........')
            root1.destroy()
    root1=Toplevel()
    a=randint(1000000001,9999999999)
    v=StringVar()                                                                                          #Creating a Top level Window
    Label(root1,text="Your randomly created acc_no is:         ").grid(row=0,column=0)
    Label(root1,text=str(a)).grid(row=0,column=1,columnspan=2)                                             #Automatically Created Account Number
    Label(root1,text="Enter Your First Name:").grid(row=1,column=0)                                        #Taking The various Entries that are required to make a new bank account
    e3=Entry(root1)
    e3.grid(row=1,column=1,columnspan=2)
    Label(root1,text="Enter Your Last Name:").grid(row=2,column=0)
    e4=Entry(root1)
    e4.grid(row=2,column=1,columnspan=2)
    Label(root1,text="Enter Your Permanent Address:").grid(row=3,column=0)
    e5=Entry(root1)
    e5.grid(row=3,column=1,columnspan=2)
    Label(root1,text="Enter Your Corrosponding Address:").grid(row=4,column=0)
    e6=Entry(root1)
    e6.grid(row=4,column=1,columnspan=2)
    Label(root1,text="Enter Your Intial Amount:").grid(row=5,column=0)
    e7=Entry(root1)
    e7.grid(row=5,column=1,columnspan=2)
    Label(root1,text="Select The type of Account:").grid(row=6,column=0)
    Radiobutton(root1,text="Saving",variable=v,value=1).grid(row=6,column=1)
    Radiobutton(root1,text="Current",variable=v,value=2).grid(row=6,column=2)
    Label(root1,text="Enter Your Phone Number:").grid(row=7,column=0)
    e9=Entry(root1)
    e9.grid(row=7,column=1,columnspan=2)
    Label(root1,text="Enter Your Alternate Phone Number:").grid(row=8,column=0)
    e10=Entry(root1)
    e10.grid(row=8,column=1,columnspan=2)
    Label(root1,text="Enter the New Password:").grid(row=9,column=0)
    e11=Entry(root1)
    e11.grid(row=9,column=1,columnspan=2)
    Button(root1,text="Create Account", command=lambda :sql_create(v.get())).grid(row=10,column=0)                                   #calling of the Sql create command
    root1.mainloop()
def login(id_,pin):
    def w_D(v2):
        if(v2=='1'):
            Label(root3,text="Enter Amount To be withdrawn:").grid(row=8,column=4)
            e13=Entry(root3)
            e13.grid(row=8,column=6)
            cur.execute('select Amount from account where acc_no=(?)',[id_])
            c=cur.fetchall()
            Amount=c[0][0]
            Button(root3,text='Withdraw',command=lambda: withdraw(Amount,float(e13.get()))).grid(row=9,column=5)
        elif(v2=='2'):
            Label(root3,text="Enter Amount To be Deposited:").grid(row=8,column=4)
            e13=Entry(root3)
            e13.grid(row=8,column=6)
            cur.execute('select Amount from account where acc_no=(?)',[id_])
            c=cur.fetchall()
            Amount=c[0][0]
            Button(root3,text='Deposit',command=lambda: Deposit(Amount,e13.get())).grid(row=9,column=5)
        else:
            showinfo(title='Invalid',message='Invalid Choice!!!!!!!!!!!')
    def Deposit(Amount,e13):                                                                                                      #function to add Money in the account
        Amount=Amount+float(e13)
        cur.execute('UPDATE Account set Amount=? where Acc_no=?',(Amount,id_))
        con.commit()
        showinfo(title='Deposit',message='The Amount was Deposited Successfully!!')
        root3.destroy()
        login(id_,pin)
    def withdraw(Amount,e13):
        if(Amount-float(e13)>0):                                                                                                #function to withdraw the amount
                    Amount=Amount-e13
                    cur.execute('UPDATE Account set Amount=(?) where Acc_no=(?)',(Amount,id_))
                    con.commit()
                    showinfo(title='Withdraw',message='The Withdraw was Successfull!!!!!!')
                    root3.destroy()
                    login(id_,pin)
        else:
            showinfo(title='Insufficient Funds',message='You Dont Have Sufficient Balance in your Account!!!!!')
    def all_acc():                                                                                                            #all_acc:Function To display all The Bank Account in the BAnk Which is only Visisble to the Administrator
        cur.execute('Select * from Account')
        s=cur.fetchall()
        Label(root2,text='Acc_no').grid(row=1,column=0)
        Label(root2,text='First Name').grid(row=1,column=1)
        Label(root2,text='Last Name').grid(row=1,column=2)
        Label(root2,text='Permanent Address').grid(row=1,column=3)
        Label(root2,text='Corrosponding Address').grid(row=1,column=4)
        Label(root2,text='Amount').grid(row=1,column=5)
        Label(root2,text='Type').grid(row=1,column=6)
        Label(root2,text='Phone Number').grid(row=1,column=7)
        Label(root2,text='Alternate Phone Number').grid(row=1,column=8)
        Label(root2,text='Pin').grid(row=1,column=9)
        r=0
        for i in s:
            t=0
            for j in s[r]:
                Label(root2,text=s[r][t]).grid(row=r+2,column=t)
                t=t+1
            r=r+1
    if(id_=='Administrator'):                                                                                                   #checking Wheather if Correct password id Admin
        if(pin=='sarthak'):                                                                
             root2=Toplevel()
             Button(root2,text='View All Accounts',command=all_acc).grid(row=0,column=0)
             Button(root2,text='Logout',command=root2.destroy).grid(row=0,column=10)                                            #calling all_acc And displaying all the bank Account and there Details which exsis in the bank
        else:
            showinfo(title="Invalid Password",message='Invalid Password For The Administraor.................')
    elif(id_=='' or pin==''):
        showinfo(title='INVALID',message='You Cannot leave Account Number or Pin Empty')
    elif(len(id_)!=10):
        showinfo(title='INVALID',message='Invalid Account Number')
    elif not (len(pin)>6 and len(pin)<30):
        showinfo(title='INVALID',message='Invalid Pin(must be between 6-30 characters)')
    else:
        cur.execute('select * from Account where acc_no=(?)',[id_])
        p=cur.fetchall()
        try:
            if(pin==str(p[0][9])):
                root3=Toplevel()
                Label(root3,text='Acc_no').grid(row=1,column=0)
                Label(root3,text='First Name').grid(row=1,column=1)
                Label(root3,text='Last Name').grid(row=1,column=2)
                Label(root3,text='Permanent Address').grid(row=1,column=3)
                Label(root3,text='Corrosponding Address').grid(row=1,column=4)
                Label(root3,text='Amount').grid(row=1,column=5)
                Label(root3,text='Type').grid(row=1,column=6)
                Label(root3,text='Phone Number').grid(row=1,column=7)
                Label(root3,text='Alternate Phone Number').grid(row=1,column=8)
                Label(root3,text='Pin').grid(row=1,column=9)
                w=0
                for i in p[0]:
                    Label(root3,text=p[0][w]).grid(row=2,column=w)
                    w=w+1
                Label(root3,text='Enter Your Choice').grid(row=3,column=5)
                Label(root3,text="1)Withdrawl").grid(row=4,column=5)
                Label(root3,text="2)Deposit").grid(row=5,column=5)
                Label(root3,text='Enter Your Choice:').grid(row=6,column=4)
                e12=Entry(root3)
                e12.grid(row=6,column=6)
                Button(root3,text='Select',command=lambda :w_D(e12.get())).grid(row=7,column=5)
                Button(root3,text='LOGOUT',command=root3.destroy).grid(row=10,columnspan=10)
                root3.mainloop()
            else:
                showinfo(title="Invalid ",message='Invalid id or the password!!!!!!!!!')
        except IndexError:
            showinfo(title='Error',message='No Account Number of this Name \n Wanna Create click on Create Account')
Label(root,text="Enter Your Login Details",fg='White',bg='Black',font='Vivaldi 20').grid(row=1,column=15,columnspan=4)                                 #Input the login details
Label(root,text="Enter your Account Number:",fg='White',bg='Black',font='Vivaldi 14').grid(row=2,column=15)    
Label(root,text="Enter your Pin:",fg='White',bg='Black',font='Vivaldi 14').grid(row=3,column=15)
e1=Entry(root,width=41)
e1.grid(row=2,column=16,columnspan=3)
e2=Entry(root,show='*',width=41)
e2.grid(row=3,column=16,columnspan=3)
Button(root,text="Login",width=25,command=lambda : login(e1.get(),e2.get())).grid(row=4,column=15,sticky=E)
Button(root,text="Create Account",width=17,command=create).grid(row=4,column=16,sticky=W+E)
Button(root,text="Exit",width=20,command= exi).grid(row=4,column=17,sticky=W)
root.mainloop()