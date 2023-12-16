from math import expm1
import random
from sqlite3 import Row
from tkinter import*
from tkinter import messagebox
import tkinter

root=Tk()
root.geometry("1300x700")
root.title("welcome page")
username=StringVar()
password=StringVar()
reglabel=StringVar() 
z=random.randint(1000,9999)
reglabel.set(str(z))
global user1
global passw1 
def ok():
    username=user1.get()
    password=passw1.get()
    if(username==" " and password==" "):
        messagebox.showinfo("","blank space not allowed")
    elif(username=="kashish" and password=="admin"):
        messagebox.showinfo("","login successful")
    else:
        messagebox.showinfo("","incorrect username or password")
    
def login():
    logf=Frame(relief=GROOVE,bd=15,bg="#E5B4F3")
    logf.place(x=0,y=0,width=1370,height=700)
    title=Label(logf,text="Login Page ",bd=15,relief=RIDGE,font=("Arial Black",25),bg="#A569BD",fg="white")
    title.pack(fill=X) 
    #-------------frame to user and password -----------------------
    
    center=Frame(logf,relief=GROOVE,bg="#A569BD",bd=10)
    center.place(x=350,y=140,width=660,height=400)
    user=Label(center,text="Username",font=("Airal 50"),bg="#A569BD",fg="black")
    user.pack()
    user1=Entry(center,borderwidth=10,width=50)
    user1.pack()
    passw=Label(center,text="Password",font="Airal 50",bg="#A569BD",fg="black")
    passw.pack()
    passw1=Entry(center,borderwidth=10,width=50)
    passw1.pack()
    loginbutton=Button(center,text="login",command=ok,font=("Airal 20"),relief=SUNKEN,bg="#A569BD",fg="white",bd=5)
    loginbutton.place(x=400,y=270,width=170)
    backbutton=Button(center,text="back",command=home,font=("Airal 20"),relief=SUNKEN,bg="#A569BD",fg="white",bd=5)
    backbutton.place(x=100,y=270,width=170)
 
def customer():
    root.title("Restaurant menu slide")
    mainframecust=Frame(relief=GROOVE,bd=10,bg="white")  
    mainframecust.place(x=0,y=0,width=1370,height=700) 
    title=Label(root,text="RESTURANT MENU",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)               
    c_name=StringVar()      
    c_phno=StringVar()

    plain_roti=StringVar()
    tandoori_roti=StringVar()
    shahi_panner=StringVar()
    kadhai_panner=StringVar()   
    malai_kofta=StringVar()
    Paneer_Butter_Masala=StringVar()
    Butter_Naan=StringVar()
    chocolate_icecream=StringVar()
    ras_malai=StringVar()
    gulab_jammun=StringVar()
    vanilla_icecream=StringVar()
    brownie=StringVar()
    dount=StringVar()
    Custard=StringVar()

    Manchurian=StringVar()
    Chowmein=StringVar()
    rice=StringVar()
    maggie=StringVar()
    chilli=StringVar()
    burger=StringVar()
    pasta=StringVar()

    total_Desserts=StringVar()
    total_Maincourse=StringVar()
    total_Starters=StringVar()
    service_charge=StringVar()
    bill_no=StringVar()
    total_Tax=StringVar()
    total_all_bill=StringVar()
    item1=StringVar()
    x=random.randint(1000,9999)
    bill_no.set(str(x))
    phone=StringVar()



    #---------------------------------------------------customer details------------------------------------------------
    details=LabelFrame(mainframecust,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
    details.place(x=0,y=80,relwidth=1)

    c_name=Label(details,font="arial 18 bold",text="customer name.",fg="white",bd=10,anchor='w',bg="#A569BD")
    c_name.grid(row=0,column=0,padx=15)

    c_name=Entry(details,font="arial 13 bold",textvariable="c_name",bd=10,insertwidth=5,bg="white",justify='left')
    c_name.grid(row=0,column=2,pady=8)

    c_phno=Label(details,font="arial 18 bold",text="customer phno..",fg="white",bd=10,anchor='w',bg="#A569BD")
    c_phno.grid(row=0,column=3,padx=15)

    c_phno=Entry(details,font="arial 13 bold",textvariable="c_phno",bd=10,insertwidth=5,bg="white",justify='left')
    c_phno.grid(row=0,column=4,pady=8)

    #---------------------------------------------main course--------------------------------------------------
    main=LabelFrame(mainframecust,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
    main.place(x=340,y=180,height=380,width=325)

    item1=Label(main,font=("Arial Black",11),text="Plain Roti",bg="#E5B4F3",fg="#6C3483")
    item1.grid(row=0,column=0,pady=11)
    item1=Entry(main,textvariable="plain_roti",borderwidth=2,width=15)
    item1.grid(row=0,column=1,padx=10)

    item2=Label(main,font=("Arial Black",11 ),text="Tandoori Roti",bg="#E5B4F3",fg="#6C3483")
    item2.grid(row=1,column=0,pady=11)
    item2=Entry(main,textvariable="tandoori_roti",borderwidth=2,width=15)
    item2.grid(row=1,column=1,padx=10)

    item3=Label(main,font=("Arial Black",11),text="Khadai Panner",bg="#E5B4F3",fg="#6C3483")
    item3.grid(row=2,column=0,pady=11)
    item3=Entry(main,textvariable="khadai_panner",borderwidth=2,width=15)
    item3.grid(row=2,column=1,padx=10)

    item4=Label(main,font=("Arial Black",11),text="Shahi Panner",bg="#E5B4F3",fg="#6C3483")
    item4.grid(row=3,column=0,pady=11)
    item4=Entry(main,textvariable="shahi_panner",borderwidth=2,width=15)
    item4.grid(row=3,column=1,padx=10)

    item5=Label(main,text="Malai Kofta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item5.grid(row=4,column=0,pady=11)
    item5=Entry(main,borderwidth=2,width=15,textvariable="malai_kofta")
    item5.grid(row=4,column=1,padx=10)

    item6=Label(main,text="Paneer Butter Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item6.grid(row=5,column=0,pady=11)
    item6=Entry(main,borderwidth=2,width=15,textvariable=Paneer_Butter_Masala)
    item6.grid(row=5,column=1,padx=10)

    item7=Label(main,text="Butter Naan",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item7.grid(row=6,column=0,pady=11)
    item7=Entry(main,borderwidth=2,width=15,textvariable=Butter_Naan)
    item7.grid(row=6,column=1,padx=10)


    #---------------------------------------------------desserts-----------------------------------------------------

    Dessert=LabelFrame(mainframecust,text="Desserts",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
    Dessert.place(x=677,y=180,height=380,width=325)

    item8=Label(Dessert,text="Chocolate Icecream",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483",pady=11)
    item8.grid(row=1,column=0)
    item8=Entry(Dessert,textvariable="chocolate_icecream",borderwidth=2,width=15,)
    item8.grid(row=1,column=1,padx=10)


    item9=Label(Dessert,text="Ras Malai",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483",pady=11)
    item9.grid(row=2,column=0)
    item9=Entry(Dessert,textvariable="ras_malai",borderwidth=2,width=15)
    item9.grid(row=2,column=1,padx=10)

    item10=Label(Dessert,text="Gulab Jammun",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483",pady=11)
    item10.grid(row=3,column=0)
    item10=Entry(Dessert,textvariable="gulab_jammun",borderwidth=2,width=15)
    item10.grid(row=3,column=1,padx=10)

    item11=Label(Dessert,text="Vanilla Icecream",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483",pady=11)
    item11.grid(row=4,column=0)
    item11=Entry(Dessert,textvariable="vanilla_icecream",borderwidth=2,width=15)
    item11.grid(row=4,column=1,padx=10)

    item12=Label(Dessert,text="Brownie sizller",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483",pady=11)
    item12.grid(row=5,column=0)
    item12=Entry(Dessert,textvariable="brownie",borderwidth=2,width=15,)
    item12.grid(row=5,column=1,padx=10)

    item13=Label(Dessert,text="Sweet",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483",pady=11)
    item13.grid(row=6,column=0)
    item13=Entry(Dessert,textvariable="sweet",borderwidth=2,width=15)
    item13.grid(row=6,column=1,padx=10)

    item14=Label(Dessert,text="Custard",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item14.grid(row=7,column=0,pady=11)
    item14=Entry(Dessert,borderwidth=2,width=15,textvariable="Custard")
    item14.grid(row=7,column=1,padx=10)


    #------------------------------------------starters-------------------------------------------
    Starters=LabelFrame(mainframecust,text="Starters",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
    Starters.place(x=5,y=180,height=380,width=325)

    item15=Label(Starters,text="Chowmein",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item15.grid(row=0,column=0,pady=11)
    item15=Entry(Starters,borderwidth=2,width=15,textvariable=Chowmein)
    item15.grid(row=0,column=1,padx=10)
    item16=Label(Starters,text="Fried Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item16.grid(row=1,column=0,pady=11)
    item16=Entry(Starters,borderwidth=2,width=15,textvariable=rice)
    item16.grid(row=1,column=1,padx=10)


    item17=Label(Starters,text="veg burger",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item17.grid(row=2,column=0,pady=11)
    item17=Entry(Starters,borderwidth=2,width=15,textvariable=burger)
    item17.grid(row=2,column=1,padx=10)


    item18=Label(Starters,text="maggie",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item18.grid(row=3,column=0,pady=11)
    item18=Entry(Starters,borderwidth=2,width=15,textvariable=maggie)
    item18.grid(row=3,column=1,padx=10)

    item19=Label(Starters,text="Cheese Chilly",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item19.grid(row=4,column=0,pady=11)
    item19=Entry(Starters,borderwidth=2,width=15,textvariable=chilli)
    item19.grid(row=4,column=1,padx=10)

    item20=Label(Starters,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item20.grid(row=5,column=0,pady=11)
    item20=Entry(Starters,borderwidth=2,width=15,textvariable=pasta)
    item20.grid(row=5,column=1,padx=10)


    item21=Label(Starters,text="Manchurian",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483")
    item21.grid(row=6,column=0,pady=11)
    item21=Entry(Starters,borderwidth=2,width=15,textvariable=Manchurian)
    item21.grid(row=6,column=1,padx=10)
    #-----------------------------------------billarea---------------------------------------------------
    billarea=Frame(mainframecust,bd=10,relief=GROOVE,bg="#E5B4F3")
    billarea.place(x=1010,y=188,width=330,height=372)   

    bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

    scrol_y=Scrollbar(billarea,orient=VERTICAL)
    txtarea=Text(billarea,yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack()
    #-----------------------------print data in bill area------------------------------
    def intro():
        txtarea.delete(1.0,END)
        txtarea.insert(END,"\tWELCOME TO OUR RESTAURANT\n\tPhone-No.739275410")
        txtarea.insert(END,f"\n\nBill no. : {bill_no.get()}")
        txtarea.insert(END,f"\nCustomer Name : {c_name.get()}")
        txtarea.insert(END,f"\nPhone No. : {phone.get()}")
        txtarea.insert(END,"\n====================================\n")
        txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
        txtarea.insert(END,"\n====================================\n")

    #---------------------------------------------billing menu---------------------------------------------
    billing_menu=LabelFrame(mainframecust,text="Billing Summary",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
    billing_menu.place(x=0,y=560,relwidth=1,height=137)

    total_Starters=Label(billing_menu,text="Cost Of Chinese ",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
    total_Starters_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=total_Starters).grid(row=0,column=1,padx=10,pady=7)

    total_Maincourse=Label(billing_menu,text="Cost Of Maincourse ",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
    total_Maincourse_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=total_Maincourse).grid(row=1,column=1,padx=10,pady=7)

    total_Desserts=Label(billing_menu,text="Cost Of Desserts ",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
    total_Desserts_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=total_Desserts).grid(row=2,column=1,padx=10,pady=7)
    def billarea():
        intro()
        if Chowmein.get()!=0:
            txtarea.insert(END,f"Chowmein\t\t {Chowmein.get()}\t\n")
        if rice.get()!=0:
            txtarea.insert(END,f"Fried Rice\t\t {rice.get()}\t\n")
        if Manchurian.get()!=0:
            txtarea.insert(END,f"Manchurian\t\t {Manchurian.get()}\t\n")
        if chilli.get()!=0:
            txtarea.insert(END,f"Cheese Chilly\t\t {chilli.get()}\t\n")
        if burger.get()!=0:
            txtarea.insert(END,f"Veg Burger\t\t {burger.get()}\t\n")
        if maggie.get()!=0:
            txtarea.insert(END,f"Veg Maggie\t\t {maggie.get()}\t\n")
        if pasta.get()!=0:
            txtarea.insert(END,f"Pasta\t\t {pasta.get()}\t\n")
        if shahi_panner.get()!=0:
            txtarea.insert(END,f"Shahi panner\t\t {shahi_panner()}\t\n")
        if Paneer_Butter_Masala.get()!=0:
            txtarea.insert(END,f"Paneer Butter Masala\t\t {Paneer_Butter_Masala.get()}\t\n")
        if malai_kofta.get()!=0:
            txtarea.insert(END,f"Malai Kofta\t\t {malai_kofta.get()}\t\n")
        if kadhai_panner.get()!=0:
            txtarea.insert(END,f"Kadhai Paneer\t\t {kadhai_panner.get()}\t\n")
        if plain_roti.get()!=0:
            txtarea.insert(END,f"Plain Roti\t\t {plain_roti.get()}\t\n")
        if Butter_Naan.get()!=0:
            txtarea.insert(END,f"Butter Naan\t\t {Butter_Naan.get()}\t\n")
        if tandoori_roti.get()!=0:
            txtarea.insert(END,f"Tandoori_Roti\t\t {tandoori_roti.get()}\t\n")
        if vanilla_icecream.get()!=0:
            txtarea.insert(END,f"Vanilla Icecream\t\t {vanilla_icecream.get()}\t\n")
        if chocolate_icecream.get()!=0:
            txtarea.insert(END,f"chocolate Icecream\t\t {chocolate_icecream.get()}\t\n")
        if ras_malai.get()!=0:
            txtarea.insert(END,f"Ras Malai\t\t {ras_malai.get()}\t\n")
        if gulab_jammun.get()!=0:
            txtarea.insert(END,f"Gulab Jamun\t\t {gulab_jammun.get()}\t\n")
        if dount.get()!=0:
            txtarea.insert(END,f"Dount\t\t {dount.get()}\t\n")
        if Custard.get()!=0:
            txtarea.insert(END,f"Custard\t\t {Custard.get()}\t\n")
        if brownie.get()!=0:
            txtarea.insert(END,f"Brownie Sizzler\t\t {brownie.get()}\t\n")

        txtarea.insert(END,f"------------------------------------\n")
        txtarea.insert(END,f"Total Tax Amount: {total_Tax}\n")
        txtarea.insert(END,f"Total Bill incl Taxex: {total_all_bill}\n")
        txtarea.insert(END,f"------------------------------------\n")    
    
    def total():
        if (c_name.get=="" or c_phno.get()==""):
            tkinter.messagebox.messagebox.showerror("Error", "Fill the complete Customer Details!!")
 

        total_Starters_price=(
              (Chowmein.get()*160)+
              (rice.get()*180)
              (Manchurian.get()*200)
              (chilli.get()*240)
              (burger.get()*160)
              (maggie.get()*140)
              (maggie.get()*140)   
    )  


        total_Maincourse_price=(
            (shahi_panner.get()*130)
            (Paneer_Butter_Masala.get()*160)
            (malai_kofta.get()*150)
            (kadhai_panner.get()*160)
            (plain_roti.get()*10)
            (Butter_Naan.get()*30)
            (tandoori_roti.get()*15)
        )
        
        total_Maincourse.set(str(total_Maincourse_price)+" Rs")


        VI=vanilla_icecream.get()*40
        CI=chocolate_icecream.get()*40
        RM=ras_malai.get()*60
        GJ=gulab_jammun.get()*50
        DD=dount.get()*60
        Cu=Custard.get()*60
        BS=brownie.get()*80

        total_Desserts_price=(
                (vanilla_icecream.get()*40)
                (chocolate_icecream.get()*40)
                (ras_malai.get()*60)
                (gulab_jammun.get()*50)
                (dount.get()*60)
                (Custard.get()*60)
                (brownie.get()*80)
        )   
    
        
        total_Desserts.set(str(total_Desserts_price)+" Rs")
    
    
        total_all_bill=(total_Starters_price+
                total_Maincourse_price+
                total_Desserts_price)

        total_Tax=(round(total_all_bill*0.18,3))
                
        total_all_bil=str(total_all_bill+total_Tax)+" Rs"

        billarea()
    #------------------------button in restaurant menu------------------------------------
    button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
    button_frame.place(x=730,width=600,height=95)
        
    button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total()).grid(row=0,column=0,padx=12)
    
    button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:Reset()).grid(row=0,column=1,padx=10,pady=6)
    
    button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit()).grid(row=0,column=2,padx=10,pady=6)
    
    button_back=Button(button_frame,text="Back",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:home()).grid(row=0,column=3,padx=10,pady=6)
    intro() 
    #-----------------------------------reset fucntion---------------------------------
    def Reset():
        item1.delete(0,END)
        item2.delete(0,END)
        item3.delete(0,END)
        item4.delete(0,END)
        item5.delete(0,END)
        item6.delete(0,END)
        item7.delete(0,END)
        item8.delete(0,END)
        item9.delete(0,END)
        item10.delete(0,END)
        item11.delete(0,END)
        item12.delete(0,END)
        item13.delete(0,END)
        item14.delete(0,END)
        item15.delete(0,END)
        item16.delete(0,END)
        item17.delete(0,END)
        item18.delete(0,END)
        item19.delete(0,END)
        item20.delete(0,END)
        item21.delete(0,END)
        total_Starters.delete(0,END)
        total_Desserts.delete(0,END)
        total_Maincourse.delete(0,END)
    #------------------------------------exit function---------------------------------
    def Exit():
                r=tkinter.messagebox.askyesno("restaurent  management system","do you want to exit")
                if r>0:
                    root.destroy()
                    return
        #-----------------------------------submit function -----------------------------
    def Submit():
        q=tkinter.messagebox.askokcancel("restaurent management system","your data has ben successfully submitted")
        if q>0:
            root.destroy()
            return
def employee():
    root.title("employee details page")  
    employeeframe=Frame(relief=RIDGE,bd=10,bg="#E5B4F3")
    employeeframe.place(x=0,y=0,height=700,width=1370)
    title=Label(employeeframe,text="Employee details",bd=15,relief=RIDGE,font=("Arial Black",25),bg="#A569BD",fg="white")
    title.pack(fill=X)
    frame=Frame(relief=GROOVE,bg="#A569BD",bd=10)
    frame.place(x=300,y=100,width=800,height=570)
    buttonframe=Frame(frame,bd=7,relief=RIDGE,bg="#6C3483")
    buttonframe.place(x=2,y=450,width=775,height=95)
    reglabel=Label(frame,text="Register Number",font=("Airal 18"),bg="#A569BD",fg="black")
    reglabel.place(x=15,y=20,width=200)
    reglabel=Entry(frame,borderwidth=5,width=50)
    reglabel.place(x=250,y=20,width=200)
    Id=Label(frame,text="Employee Id",font=("Airal 18"),bg="#A569BD",fg="black")
    Id.place(x=15,y=90,width=200)
    Id=Entry(frame,borderwidth=5,width=50)
    Id.place(x=250,y=90,width=200)
    name=Label(frame,text="Employee Name",font=("Airal 18"),bg="#A569BD",fg="black")
    name.place(x=15,y=160,width=200)
    name=Entry(frame,borderwidth=5,width=50)
    name.place(x=250,y=160,width=200)
    address=Label(frame,text="Employee Address",font=("Airal 18"),bg="#A569BD",fg="black")
    address.place(x=15,y=230,width=200)
    address=Entry(frame,borderwidth=5,width=50)
    address.place(x=250,y=230,width=200)
    contact=Label(frame,text="Contact Number",font=("Airal 18"),bg="#A569BD",fg="black")
    contact.place(x=15,y=300,width=200)
    contact=Entry(frame,borderwidth=5,width=50)
    contact.place(x=250,y=300,width=200)
    email=Label(frame,text="E-mail Address",font=("Airal 18"),bg="#A569BD",fg="black")
    email.place(x=15,y=370,width=200)
    email=Entry(frame,borderwidth=5,width=50)
    email.place(x=250,y=370,width=200)
    submitb=Button(buttonframe,text="Submit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483")
    submitb.grid(row=0,column=1,padx=10,pady=6)
    back=Button(buttonframe,text="Back",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=home)
    back.grid(row=0,column=3,padx=10,pady=6)
    reset=Button(buttonframe,text="Reset",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=reset)
    reset.grid(row=0,column=5,padx=10,pady=6)
    exit=Button(buttonframe,text="Submit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483")
    exit.grid(row=0,column=7,padx=10,pady=6)
    
def manage():
    root.title("Management Page")
    mframe=Frame(relief=RIDGE,bd=10,bg="#E5B4F3")
    mframe.place(x=0,y=0,height=700,width=1370)
    title=Label(mframe,text="Management menu",bd=15,relief=RIDGE,font=("Arial Black",25),bg="#A569BD",fg="white")
    title.pack(fill=X)  
    bframe=Frame(mframe,relief=GROOVE,bg="#A569BD",bd=10)
    bframe.place(x=350,y=140,width=660,height=400)
    employeedetails=Button(bframe,text="Employee Details",font="Airal 18",bg="#E5B4F3",fg="#6C3483",width=20,relief=FLAT,bd=5,command=employee)  
    employeedetails.place(x=180,y=10,width=290,height=60)
    salebutton=Button(bframe,text="Sales",font="Airal 20",bg="#E5B4F3",fg="#6C3483",width=20,relief=FLAT,bd=5)  
    salebutton.place(x=180,y=80,width=290,height=60)
    customerdetails=Button(bframe,text="Customer Details",font="Airal 18",bg="#E5B4F3",fg="#6C3483",width=20,relief=FLAT,bd=5)
    customerdetails.place(x=180,y=150,width=290,height=60)
    back=Button(bframe,text="Back",font="Airal 18",bg="#E5B4F3",fg="#6C3483",width=20,relief=FLAT,bd=5,command=home)
    back.place(x=180,y=220,width=290,height=60)
    exit=Button(bframe,text="Exit",font="Airal 18",bg="#E5B4F3",fg="#6C3483",width=20,relief=FLAT,bd=5)
    exit.place(x=180,y=290,width=290,height=60)
 
    
    
    
    
def home():    
    head=Frame(root,relief=GROOVE,bd=20,bg="#E5B4F3")
    head.place(x=0,y=0,width=1370,height=700)
    title=Label(head,text="Welcome To Restaurant ",bd=15,relief=RIDGE,font=("Arial Black",25),bg="#A569BD",fg="white")
    title.pack(fill=X)                 
    mang=Button(root,text="Managment",font=("Airal black",60),bg="#E5B4F3",fg="#6C3483",width=10,relief=GROOVE,bd=15,command=login)
    mang.place(x=500,y=200)
    
    cust=Button(root,text="Customer",font=("Airal black",60),bg="#E5B4F3",fg="#6C3483",width=10,relief=GROOVE,bd=15,command=customer)
    cust.place(x=500,y=450)
home()
root.mainloop()