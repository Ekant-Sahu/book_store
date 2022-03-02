#Importing extra modules

from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sqltor

#sql password error

try:
    print("Enter your MySQL user name and password (Notice: password and username are case sensitive)")
    
    #sql variables
    sql_username = input("Enter your Sql Username: ")
    sql_password = input("Enter your Sql Password: ")




    #Creating database

    def create_database():
        mydb = sqltor.connect(
        host="localhost",
        user= sql_username,
        password= sql_password)

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS xzy132")

    
    
    create_database()

    #creating table

    def create_table():
        mydb = sqltor.connect(
        host="localhost",
        user= sql_username,
        password= sql_password,
        database="xzy132")


        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), contact VARCHAR(30), email VARCHAR(255), book_name VARCHAR(255),issue_date VARCHAR(30),return_date VARCHAR(30))")

    create_table()




    class database:
        def __init__(self,app):
            self.app=app
            self.app.title("Save Data")
            self.app.geometry("536x750")
            self.app.resizable(False,False)

            #app Config

            self.app.title("Book Store")
            self.app.iconbitmap(r"elements\a .ico")

            #background Image

            self.bg=PhotoImage(file='elements/bg.png')
            self.bg_image=Label(self.app,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

            #Content Box

            frame_box = Frame(self.app,bg="black")
            frame_box.place(x=28,y=25,height=700,width=480)

            #content

            extra = Label(frame_box,text="(Fillup the book issue form, to issue books from Book Store)",font=("Gabriola", 15,),fg="white",bg="black").place(x=60,y=66)
            heading = Label(frame_box,text="°•. Book Issue Form .•°",font=("Impact", 25,),fg="orange",bg="black").place(x=100,y=35)

            #form

            name = Label(frame_box,text="Enter Your Full Name :",font=("Comic Sans MS", 10),fg="white",bg="black").place(x=30,y=125)
            self.text_name=ttk.Entry(frame_box,font=("times new romam",10,"italic"),justify = CENTER)
            self.text_name.place(x=75,y=150,width=350,height=25)
            
            contact = Label(frame_box,text="Enter Your Contact :",font=("Comic Sans MS", 10),fg="white",bg="black").place(x=30,y=195)
            self.text_contact=ttk.Entry(frame_box,font=("times new romam",10,"italic"),justify = CENTER)
            self.text_contact.place(x=75,y=220,width=350,height=25)
            
            email = Label(frame_box,text="Enter Your Email Adress :",font=("Comic Sans MS", 10),fg="white",bg="black").place(x=30,y=265)
            self.text_email=ttk.Entry(frame_box,font=("times new romam",10,"italic"),justify = CENTER)
            self.text_email.place(x=75,y=290,width=350,height=25)
            
            book_name = Label(frame_box,text="Enter Book Name :",font=("Comic Sans MS", 10),fg="white",bg="black").place(x=30,y=335)
            self.text_book_name=ttk.Entry(frame_box,font=("times new romam",10,"italic"),justify = CENTER)
            self.text_book_name.place(x=75,y=360,width=350,height=25)

            issue_date = Label(frame_box,text="Enter Book Issue Date (dd-mm-yy) :",font=("Comic Sans MS", 10),fg="white",bg="black").place(x=30,y=405)
            self.entry_issue_date=ttk.Entry(frame_box,font=("times new romam",10,"italic"),justify = CENTER)
            self.entry_issue_date.place(x=75,y=430,width=350,height=25)

            return_date = Label(frame_box,text="Enter Book Returning Date (dd-mm-yy) :",font=("Comic Sans MS", 10),fg="white",bg="black").place(x=30,y=475)
            self.entry_return_date=ttk.Entry(frame_box,font=("times new romam",10,"italic"),justify = CENTER)
            self.entry_return_date.place(x=75,y=500,width=350,height=25)


            #Submit_Buttom

            submit=Button(frame_box,text="Submit",command=self.submit_function,cursor="hand2",fg="black",bg="orange",bd=0,font=("impact",20,"bold"))
            submit.place(x = 191,y=570)

            #show_button

            show_button=Button(frame_box,text="Show Data",command=text_show,fg="black",cursor="hand2",bg="orange",bd=0,font=("impact",15))
            show_button.place(x = 315,y=580)

            #reset_button

            reset_button=Button(frame_box,text="Reset Form",command=self.reset_function,cursor="hand2",fg="black",bg="orange",bd=0,font=("impact",15))
            reset_button.place(x = 65,y=580)

            #conditions_terms
            term=Label(frame_box,text="(By clicking on SUBMIT button you atomaticaly agree to our terms and conditions)",fg="white",bg="black",bd=0,font=("Gabriola",13,"italic"))
            term.place(x = 20,y=640)

        def submit_function(self):
            if self.text_name.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.text_book_name.get()=="" or self.entry_issue_date.get=="" or self.entry_return_date.get=="":
                messagebox.showerror("Failed","All fields are required",parent=self.app)

            elif self.text_name.get().isnumeric() == True:
                messagebox.showerror("Failed","Invalid Name",parent=self.app)

            elif self.entry_issue_date.get().isalpha() == True or self.entry_return_date.get().isalpha() == True or not "-" in self.entry_return_date.get() and self.entry_issue_date.get():
                messagebox.showerror("Failed","Invalid Date",parent=self.app)

            elif self.text_contact.get().isnumeric() == False or len(self.text_contact.get()) >= 11:
                messagebox.showerror("Failed","Invalid contact : contact must be under 11 characters exclude +91 and letters are not allowed",parent=self.app)

            elif not "@" in self.text_email.get():
                messagebox.showerror("Failed","Invalid Email",parent=self.app)

            else:

                #saving data to sql
                mydb = sqltor.connect(
                host="localhost",
                user=sql_username,
                password=sql_password,
                database="xzy132")

                mycursor = mydb.cursor()

                sql = "INSERT INTO customers (name, contact,email,book_name,issue_date,return_date) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (self.text_name.get(),self.text_contact.get(),self.text_email.get(),self.text_book_name.get(),self.entry_issue_date.get(),self.entry_return_date.get())
                mycursor.execute(sql, val)

                mydb.commit()

                messagebox.showinfo("Sucessfuly Saved","Your Data is recorded",parent=self.app)
            

        def reset_function(self):
            self.text_book_name.delete(0,END)
            self.text_contact.delete(0,END)
            self.text_email.delete(0,END)
            self.text_name.delete(0,END)
            self.entry_return_date.delete(0,END)
            self.entry_issue_date.delete(0,END)

        #def show_data(self):
            #text_show()


    def text_show():
     
        
        connection = sqltor.connect(host='localhost',
                                             database='xzy132',
                                             user=sql_username,
                                             password=sql_password)

        sql_select_Query = "select * from customers"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        #row12 = cursor.rowcount()

        print("\n","PRINTING STORED DATA -","\n")
        
        
        for row in records:
             
            print("Name = ", row[0], )
            
            print("Phone Number = ", row[1])
            
            print("Email Adress  = ", row[2])
            
            print("Book Name  = ", row[3])
            
            print("Issue Date  = ", row[4])
            
            print("Returning Date  = ", row[5], "\n")
            

        

    #condition for opening program



    app = Tk()
    obj = database(app)
    app.mainloop

except:
    print("\n","!!! Unexpected Error Read the text file (Help) for more information !!!","\n")
