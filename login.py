from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install Pillow
# from datatime import *
import time
from math import *
import pymysql
import os
from tkinter import messagebox,ttk
class Login_window:
 def __init__(self,root):
    self.root=root
    self.root.title("Login System")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="#021e2f")
	
 	#bg colors==
    left_lbl=Label(self.root,bg="#08A3D2",bd=0)
    left_lbl.place(x=0,y=0,relheight=1,width=800)
	
    right_lbl=Label(self.root,bg="#031F3C",bd=0)
    right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
	
	#frames
    login_frame=Frame(self.root,bg="white")
    login_frame.place(x=250,y=100,width=800,height=500)

    title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
    email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
    self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")	
    
    self.txt_email.place(x=250,y=180,width=350,height=35)

    pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
    self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")	
    self.txt_pass_.place(x=250,y=280,width=350,height=35)

    btn_reg=Button(login_frame,cursor="hand2",text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#800857",command=self.register_again).place(x=250,y=320)

   #  btn_forget=Button(login_frame,cursor="hand2",text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red",command=self.forget_password).place(x=450,y=320)

   #  btn_change_password=Button(self.root2,text="Reset Password",bg="green",fg="white",font=("times new roman",15,"bold"),command=self.forget_password).place(x=90,y=340)

    btn_login=Button(login_frame,text="Login",font=("times  new roman",20,"bold"),fg="white",bd=0,bg="#800857",cursor="hand2",command=self.login).place(x=250,y=380,width=180,height=40)

 def register_again(self):
    self.root.destroy()
    import register

 def login(self):
    if(self.txt_email.get()=="" or self.txt_pass_.get()==""):
       messagebox.showerror("Error","All Fields are required",parent=self.root)
    else:
       try:
          con=pymysql.connect(host="localhost",user="root",password="",database="Student_result")
          cur=con.cursor()
          cur.execute("select * from participants where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror("Error","Invalid username or password",parent=self.root) 
            
          else:
            messagebox.showinfo("Successs","Welcome to BNMIT Student Result Management System",parent=self.root)
            self.root.destroy()
            os.system("python dashboard.py")
            con.close()
       except Exception as ex:
          messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

	#clock==
    # self.lbl=label(self.root,text="\nWebcode clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
    # self.lbl=place(x=90,y=120,height=450,width=350)
    # self.working()
 def forget_password(self):
    if  self.txt_email.get()=="":
        messagebox.showerror("Error","please enter the valid email address to reset your password",parent=self.root)
    else:
        self.root2=Toplevel()
        self.root2.title("Forget Password")
        self.root2.geometry("350x495+450+150")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.root2.grab_set()
        t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

        #forget password
        question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)

        self.txt_question=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
        self.txt_question['values']=("Select","Your pet name","Your best friend name","Your birth day")
        self.txt_question.place(x=50,y=130,width=250)
        self.txt_question.current(0)

        answer=Label(self.root2,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
        self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=50,y=210,width=250)

        new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
        self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
        self.txt_new_pass.place(x=50,y=290,width=250)

        btn_change_password=Button(self.root2,text="Reset Password",bg="green",fg="white",font=("times new roman",15,"bold")).place(x=50,y=340)



root=Tk()
obj=Login_window(root)
root.mainloop()
