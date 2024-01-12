import tkinter as tk
from tkinter import*
import mysql.connector as ms
def win():
    window=tk.Tk()
    window.title("Details")
    global n
    n=tk.StringVar()
    global m
    m=tk.StringVar()
    nm=tk.Label(window,text="Enter name:").grid()
    enm=tk.Entry(window,textvariable=n).grid()
    mnm=tk.Label(window,text="Enter mobile number:").grid()
    emnm=tk.Entry(window,textvariable=m).grid()
    title=tk.Label(window,text="Select the place you want to visit:").grid()
    global rvar
    rvar=IntVar()
    global cvar
    cvar=IntVar()
    evar=tk.StringVar()
    tvar=tk.StringVar()
    global mvar
    mvar=tk.StringVar()
    R1=Radiobutton(window, text="Delhi", variable=rvar, value=1).grid()
    R2=Radiobutton(window, text="Assam", variable=rvar, value=2).grid()
    R3=Radiobutton(window, text="Haryana", variable=rvar, value=3).grid()
    R4=Radiobutton(window, text="Himachal Pradesh", variable=rvar, value=4).grid()
    R5=Radiobutton(window, text="Karnataka", variable=rvar, value=5).grid()
    date=tk.Label(window, text="Enter date:").grid()
    ebox=tk.Entry(window, textvariable=evar).grid()
    time=tk.Label(window, text="Enter time:").grid()
    tbox=tk.Entry(window, textvariable=tvar).grid()
    mode=tk.Label(window, text="Through which mode of transport do you want to travel ?").grid()
    C1=Radiobutton(window, text="Railways", variable=cvar, value=1).grid()
    C2=Radiobutton(window, text="Airways", variable=cvar, value=2).grid()
    members=tk.Label(window, text="How many members are travelling with you ?").grid()
    mbox=tk.Entry(window, textvariable=mvar).grid()
    cont=tk.Button(window, text="Continue",command=em).grid()
def em():
    swindow=tk.Tk()
    swindow.title("Confirmation")
    global s
    s=rvar.get()
    k=cvar.get()
    p=int(mvar.get())
    yvar=tk.StringVar()
    d1={1:4000,2:5000,3:4500,4:3500,5:4000}
    d2={1:1,2:2}
    r=tk.Label(swindow, text="The total cost of travelling is:").grid()
    q=tk.Label(swindow, text=d1[s]*p*d2[k]).grid()
    x=tk.Label(swindow, text="Enter your email:").grid()
    y=tk.Entry(swindow, textvariable=yvar).grid()
    global y
    t=tk.Button(swindow, text="Book package",command=thk).grid()
    des=tk.Button(swindow,text="QUIT",command=exit).grid()
def thk():
    lwindow=tk.Tk()
    lwindow.title("Feedback")
    l=tk.Label(lwindow, text="Thank you choosing us..").grid()
    ser=tk.Label(lwindow, text="We hope you enjoyed our services!!!").grid()
    g=tk.StringVar()
    global menu
    menu=tk.StringVar(lwindow)
    menu.set("Rating")
    drop= OptionMenu(lwindow, menu,"1", "2","3","4","5","6","7","8","9","10").grid()
    g1=tk.Label(lwindow,text="Your feedback:").grid()
    g2=tk.Entry(lwindow,textvariable=g).grid()
    ex=tk.Button(lwindow, text="SUBMIT",command=sql).grid()
def send_email(to_email, subject, body):
    gmail_user = '####'
    gmail_password = '####'

    msg = MIMEMultipart()
    msg['From'] = y
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.close()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')
def sql():
    con=ms.connect(host="localhost",user="root",password="123",database="project")
    mycur=con.cursor()
    nm=n.get()
    mb=m.get()
    rt=menu.get()
    d={1:"Delhi",2:"Assam",3:"Haryana",4:"Himachal Pradesh",5:"Karnataka"}
    pckg=d[s]
    query="insert into custinfo values('{}','{}','{}','{}')".format(nm,mb,pckg,rt)
    mycur.execute(query)
    con.commit()
    con.close()
    send_email(to_email=y.get(), subject="Booking Confirmation", body="Thank you for booking!")
    exit
win()
