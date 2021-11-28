from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from PIL import ImageTk,Image

def student():

    def distroy3():
        stud.destroy()

    stud=Tk()
    stud.title("Student Info")
    stud.geometry("950x650")
    stud.configure(bg="lightgoldenrod")

    L=Label(stud,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
    L.place(x=60,y=50)
    label=Label(stud,text="Student Details",bg="cyan2",fg='pink',font=("sitkaheading",20,"bold"))
    label.place(x=160,y=160)

    style=ttk.Style()
    style.configure("Treeview", background="purple", foreground="white",rowheight=250,fieldbackground="lightgoldenrod")
    style.configure("Treeview.Heading", background="purple", foreground="white")
    
    table=ttk.Treeview(stud,column=("Name","Ad.No","Gender","Address","mail_id","Country_code","Phone","District"),selectmode="extended")
    
    table.heading('#0',text="Name",anchor=CENTER)
    table.heading('#1',text="Ad.NO",anchor=CENTER)
    table.heading('#2',text="Gender",anchor=CENTER)
    table.heading('#3',text="Address",anchor=CENTER)
    table.heading('#4',text="mail_id",anchor=CENTER)
    table.heading('#5',text="Country_code",anchor=CENTER)
    table.heading('#6',text="Contact",anchor=CENTER)
    table.heading('#7',text="District",anchor=CENTER)
       
    
    table.column('#0', stretch=YES, minwidth=50,width=80)
    table.column('#1', stretch=YES, minwidth=80,width=110)
    table.column('#2', stretch=YES, minwidth=50,width=80)
    table.column('#3', stretch=YES, minwidth=80,width=110)
    table.column('#4', stretch=YES, minwidth=30,width=50)
    table.column('#5', stretch=YES, minwidth=80,width=100)
    table.column('#6', stretch=YES, minwidth=30,width=80)
    table.column('#7', stretch=YES, minwidth=20,width=110)
        
    table.place(x=80,y=250)    
    con=sqlite3.connect("school.db")
    cur=con.cursor()
    cur.execute('SELECT * from stud');
    for row in cur.fetchall():
        table.insert("",1,text=row[1],values=(row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

    b5=Button(stud,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy3)
    b5.place(x=750,y=550)   
    stud.mainloop()

def enquiry():

    def distroy4():
        root.destroy()
        home()
    name=StringVar()
    def view():
        root2=Tk()
        root2.title("Student Enquiry")
        root2.geometry("950x650")
        root2.configure(bg="lightgoldenrod")

        L=Label(root2,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
        L.place(x=60,y=50)
        label=Label(root2,text="Student Enquiry",bg="cyan2",fg='pink',font=("sitkaheading",20,"bold"))
        label.place(x=160,y=160)

        table=ttk.Treeview(root2,column=("Name","Ad.No","Gender","Address","mail_id","Country_code","Phone","District"),selectmode="extended")
        table.heading('#0',text="Name",anchor=CENTER)
        table.heading('#1',text="Ad.NO",anchor=CENTER)
        table.heading('#2',text="Gender",anchor=CENTER)
        table.heading('#3',text="Address",anchor=CENTER)
        table.heading('#4',text="mail_id",anchor=CENTER)
        table.heading('#5',text="Country_code",anchor=CENTER)
        table.heading('#6',text="Contact",anchor=CENTER)
        table.heading('#7',text="District",anchor=CENTER)
        
        table.column('#0', stretch=YES, minwidth=50,width=80)
        table.column('#1', stretch=YES, minwidth=80,width=110)
        table.column('#2', stretch=YES, minwidth=30,width=50)
        table.column('#4', stretch=YES, minwidth=80,width=110)
        table.column('#5', stretch=YES, minwidth=80,width=110)
        table.column('#3', stretch=YES, minwidth=110,width=150)
        table.column('#6', stretch=YES, minwidth=30,width=80)
        table.column('#7', stretch=YES, minwidth=50,width=110)
        
        table.place(x=80,y=250)
        style=ttk.Style()
        style.configure("Treeview", background="royalblue", foreground="yellow",rowheight=50,fieldbackground="lightgoldenrod")
        style.configure("Treeview.Heading", background="royalblue", foreground="white")
    
        n=e.get()
        con=sqlite3.connect("school.db")
        cur=con.cursor()
        cur.execute('SELECT * from stud where Name=?',(n,));
        for row in cur.fetchall():
            table.insert("",0,text=row[1],values=(row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        b5=Button(root2,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy4)
        b5.place(x=750,y=600)
        root2.mainloop()
        
    root=Tk()
    root.title("Student Enquiry")
    root.geometry("650x650")
    root.configure(bg="lightgoldenrod")

    L=Label(root,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
    L.place(x=60,y=50)
    label=Label(root,text="Student Enquiry",bg="purple",fg='white',font=("simsun",20,"bold"))
    label.place(x=160,y=160)
    n=Label(root,text="Enter Name",font=("times new roman",14,"bold"),fg="deepskyblue")
    n.place(x=80,y=230)
    e=Entry(root,textvar=name,bd=1,width=35)
    e.place(x=250,y=235)
    button=Button(root,text="submit",fg="blue2",font=("rockwell",16),command=view)
    button.place(x=190,y=300)
    b5=Button(root,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy4)
    b5.place(x=350,y=450)
    root.mainloop()

def fee():

    def distroy2():
        fee.destroy()
    
    fee=Tk()
    fee.title("Fee Structure")
    fee.geometry("650x650")
    fee.configure(bg="lightgoldenrod")

    L=Label(fee,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
    L.place(x=60,y=50)
    label=Label(fee,text="Fee Structure",bg="cyan2",fg='pink',font=("sitkaheading",20,"bold"))
    label.place(x=160,y=160)
    table=ttk.Treeview(fee,height=10,column=("year","Approximate Fee"),selectmode="extended")
    table.heading('#0',text="Year",anchor=CENTER)
    table.heading('#1',text="Approximate Fee",anchor=CENTER)
    table.column('#0', stretch=YES, minwidth=50,width=80)
    table.column('#1', stretch=YES, minwidth=50,width=110)
    table.place(x=100,y=200)
    style=ttk.Style()
    style.configure("Treeview", background="royalblue", foreground="yellow",rowheight=50,fieldbackground="lightgoldenrod")
    style.configure("Treeview.Heading", background="royalblue", foreground="white")
    
    con=sqlite3.connect("school.db")
    cur=con.cursor()
    cur.execute('SELECT * from fee');
    for row in cur.fetchall():
        table.insert("",0,text=row[0],values=(row[1]))
       
    b5=Button(fee,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy2)
    b5.place(x=350,y=450)
    fee.mainloop()
    
def admsn():

    
    
    def distroy():
        w.destroy()   

    def login(): 
        
        name=entry_1.get()
        ad=e.get()
        id=e2.get()
        ph=e6.get()
        gndr=v.get()
        c=phcode.get()
        addr=t.get("1.0","end-1c")
        dst=district.get()
        con=sqlite3.connect("school.db")
        cur=con.cursor()
        cur.execute("create table if not exists stud(Id integer primary key autoincrement,Name text not null,Admission_no text,Gender text not null,Address text not null,mail_id text not null,Country text not null,Contact integer not null,District text not null)")
        cur.execute("insert into stud(Name,Admission_no,Gender,Address,mail_id,Country,Contact,District) values(?,?,?,?,?,?,?,?)",(name,ad,gndr,addr,id,c,ph,dst),)
        con.commit()
    w = Tk()
    w.title("Registration")
    w.geometry("650x850")
    w.configure(bg="lightgoldenrod")
    L=Label(w,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
    L.place(x=60,y=50)

    v1=StringVar() #name
    v2=StringVar() #admsn
    v3=StringVar() #mail
    v4=StringVar() #contact
    v=IntVar(w)    #gndr
    cod=StringVar()  #code
    d=StringVar()   #dstrct
    
    label_1 =Label(w,text="FullName",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label_1.place(x=80,y=130)
    entry_1=Entry(w,textvar=v1,width=45)
    entry_1.place(x=240,y=135)
    
    label=Label(w,text="Admission Number",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label.place(x=80,y=170)
    e=Entry(w,textvar=v2,width=20)
    e.place(x=250,y=175)

    label2=Label(w,text="Mail_id",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label2.place(x=80,y=210)
    e2=Entry(w,textvar=v3,width=50)
    e2.place(x=240,y=215)

    gndr1=IntVar()
    gndr2=IntVar()
    label_4 =Label(w,text="Gender",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label_4.place(x=80,y=250)
    c1=Radiobutton(w,text="Male",padx= 5, var=v, value=1)
    c1.place(x=240,y=255)
    c2=Radiobutton(w,text="Female",padx= 5, variable=v, value=2)
    c2.place(x=240,y=285)
    

    label3=Label(w,text="Address",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label3.place(x=80,y=325)
    t=Text(w,height=4,width=30)
    t.place(x=240,y=330)

    label_5=Label(w,text="Code",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label_5.place(x=80,y=400)
    phcode = ttk.Combobox(w, width = 27, textvariable = cod) 
    phcode['values'] =('+91' ,'+971' , '+353' ,'+42' ,'+48')
    phcode.config(width=4)
    phcode.place(x=240,y=400)
    phcode.current()

    label6=Label(w,text="Contact",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label6.place(x=80,y=440)
    e6=Entry(w,textvar=v4)
    e6.place(x=240,y=440)

    label_8=Label(w,text="District",bg="pink",fg="deepskyblue",font=("times new roman",14,"bold"))
    label_8.place(x=80,y=500)
    district = ttk.Combobox(w, width = 27, textvariable =d) 
    district['values'] =('Trivandrum' ,'Kollam' , 'Alapuzha' ,'Kottayam' ,'Ernakulam','Palakkad','Ernakulam','Wayanad','Thrissur','Kasargode','Idukki','Kozhikode','pathanthitta')
    district.place(x=240,y=505)
    district.current()
    
    b=Button(w,text="Submit",fg="blue2",font=("rockwell",16),command=login)
    b.place(x=200,y=650)
    b5=Button(w,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy)
    b5.place(x=300,y=650)
    w.mainloop()
    
def home():

    def distroy1():
        w1.destroy()
        
    w1 = Tk()
    w1.title("Home")
    w1.geometry("900x650")
    w1.configure(bg="lightgoldenrod")

    L=Label(w1,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
    L.place(x=60,y=50)
    
    b1=Button(w1,text="New Admission",command=admsn,bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"))
    b1.place(x=50,y=600)
    b2=Button(w1,text='fee details',bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=fee)
    b2.place(x=215,y=600)
    b3=Button(w1,text="Enquiry",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=enquiry)
    b3.place(x=340,y=600)
    b4=Button(w1,text="Student Info",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=student)
    b4.place(x=450,y=600)
    b5=Button(w1,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy1)
    b5.place(x=650,y=600)
    w1.mainloop()

def forgot():

    def distroy5():
        root1.destroy()
        
    pwd=StringVar()

    def reset():
        p1=e.get()
        con=sqlite3.connect("school.db")
        c=con.cursor()
        c.execute("update admin set password=? where id=?",(p1,1,))
        con.commit()
        
    root1=Tk()
    root1.geometry("650x500")
    root1.configure(bg="lightgoldenrod")
    Lab=Label(root1,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
    Lab.place(x=60,y=60)
    label=Label(root1,text="Reset Password",bg="purple",fg='white',font=("simsun",20,"bold"))
    label.place(x=160,y=160)
    n=Label(root1,text="New Password",font=("times new roman",14,"bold"),fg="deepskyblue")
    n.place(x=80,y=230)
    e=Entry(root1,textvar=pwd,bd=1)
    e.place(x=250,y=235)
    button=Button(root1,text="submit",fg="blue2",font=("rockwell",16),command=reset)
    button.place(x=190,y=300)
    b5=Button(root1,text="<<previous page",bg="skyblue2",fg="deeppink",font=("times new roman",14,"bold"),command=distroy5)
    b5.place(x=450,y=300)
    root1.mainloop()

def check():

    user=u.get()
    pwd=p.get()
    con=sqlite3.connect("school.db")
    c=con.cursor()
    u1="school"
    c.execute("select password from admin")
    p1=c.fetchall()
    for i in p1:
        t=i[0]
    """p1="123"""
    con.commit()
    
    if user==u1 and pwd==t:
        home()
    elif user=="" and pwd=="":
        tkinter.messagebox.showerror("check","Entry Required.")
    else:
        tkinter.messagebox.showerror("check","Incorrect username or password.")

r=Tk()
r.geometry("650x850")
r.configure(bg="lightgoldenrod")
r.title('SCHOOL MANAGEMENT SYSTEM')
bgImage=ImageTk.PhotoImage(file=r"C:\Users\manaf\OneDrive\Desktop\smpl prgrms\project\school.jpg")
background_Image =Label(r, image=bgImage)
background_Image.pack()
u=StringVar()
p=StringVar()
L=Label(r,text="GOVT HSS SCHOOL, ANCHAL",bg="royalblue",font=("algerian",28,"bold"))
L.place(x=60,y=60)
L1=Label(r,text='Username',fg="deepskyblue",font=('times new roman',18,"bold"))
L1.place(x=90,y=400)
L2=Label(r,text='Password',fg="deepskyblue",font=('times new roman',18,"bold"))
L2.place(x=90,y=450)
e1=Entry(r,textvar=u,bd=3,width=35)
e1.place(x=210,y=405)
e2=Entry(r,textvar=p,bd=3,width=35)
e2.place(x=210,y=460)
b=tkinter.Button(r,text='Login',fg='white',bg="deepskyblue",font=("rockwell",14),command=check)
b.place(x=200,y=530)
b1=Button(r,text="forgot password",fg="white",bg="deepskyblue",font=("rockwell",14),command=forgot)
b1.place(x=300,y=530)
r.mainloop()
