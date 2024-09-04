from tkinter import*
from PIL import Image,ImageTk 
from course import CourseClass
from student import studentsClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3
class RMS:
  def __init__(self, root):
    self.root=root
    self.root.title("Student Result Management System")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="white")
    self.logo_dash=Image.open("images/logo.jpeg")
    self.logo_dash=self.logo_dash.resize((40,40))
    self.logo=ImageTk.PhotoImage(self.logo_dash)
    
    title=Label(self.root,text="Student Result Management System",padx=20,compound=LEFT,image=self.logo,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
    M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",18),bg="white")
    M_Frame.place(x=10,y=70,width=1500,height=80)
    btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=25,y=5,width=200,height=40)
    btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=275,y=5,width=210,height=40)
    btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=525,y=5,width=200,height=40)
    btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=775,y=5,width=200,height=40)
    btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1025,y=5,width=200,height=40)
    btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit).place(x=1275,y=5,width=200,height=40)
      #====content==
    self.bg_img=Image.open("images/bnmit.jpeg")
    self.bg_img=self.bg_img.resize((920,350))
    self.bg_img=ImageTk.PhotoImage(self.bg_img)
    self.lb1_bg=Label(self.root,image=self.bg_img).place(x=400,y=200,width=920,height=300)

    self.lb1_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
    self.lb1_course.place(x=400,y=530,width=300,height=100)
    self.lb2_course=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
    self.lb2_course.place(x=710,y=530,width=300,height=100)
    self.lb3_course=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
    self.lb3_course.place(x=1020,y=530,width=300,height=100)

    footer=Label(self.root,text="BNMIT - Student Result Management System\n\nContact us for any Technical issue",font=("goudy old style",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
    self.update_details()
  def update_details(self):
   con=sqlite3.connect(database="rms.db")
   cur=con.cursor()
   try:
      cur.execute("select * from course")
      cr=cur.fetchall()
      self.lb1_course.config(text=f"Total Courses\n[{str(len(cr))}]")
      

      cur.execute("select * from students")
      cr=cur.fetchall()
      self.lb2_course.config(text=f"Total Students\n[{str(len(cr))}]")
      # self.lb2_course.after(200,self.update_details)

      cur.execute("select * from result")
      cr=cur.fetchall()
      self.lb3_course.config(text=f"Total Results\n[{str(len(cr))}]")
      # self.lb3_course.after(200,self.update_details)

      self.lb1_course.after(200,self.update_details)

   except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}")

  def add_course(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=CourseClass(self.new_win)

  def add_student(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=studentsClass(self.new_win)

  def add_result(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=resultClass(self.new_win)

  def add_report(self):
    self.new_win=Toplevel(self.root)
    self.new_obj=reportClass(self.new_win)
  
  def logout(self):
    op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
    if op==True:
      self.root.destroy()
      os.system("python login.py")

  def exit(self):
    op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
    if op==True:
      self.root.destroy()
    


if __name__=="__main__":
  root=Tk()
  obj=RMS(root)
  root.mainloop()
