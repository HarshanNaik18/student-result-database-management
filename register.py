from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql
import re
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Regestration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
# #========bg image====
        self.bg=ImageTk.PhotoImage(file="images/welcome.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,width=800,relwidth=1,relheight=1)

# #====left image====
        self.left=ImageTk.PhotoImage(file="images/logo.jpeg")
        left=Label(self.root,image=self.left).place(x=-800,y=0,width=400,relheight=500)

# register frame====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=580, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        self.var_fname = StringVar()

        f_name = Label(frame1, text="First name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray", textvariable=self.var_fname)
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        contact = Label(frame1, text="Contact number", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
        self.txt_email = StringVar()
        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        question = Label(frame1, text="Security Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)

        self.txt_question = ttk.Combobox(frame1, font=(
            "times new roman", 13), state="readonly", justify=CENTER)
        self.txt_question['values'] = (
            "Select", "Your pet name", "Your best friend name", "Your birth day")
        self.txt_question.place(x=50, y=270, width=250)
        self.txt_question.current(0)

        answer = Label(frame1, text="Security answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        password = Label(frame1, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        cpass = Label(frame1, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpass = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_cpass.place(x=370, y=340, width=250)

        # self.btn_img=ImageTk.PhotoImage(file="")
        btn_register = Button(frame1, text="REGISTER  HERE", font=(
            "times new roman", 20, "bold"), bg="light blue", command=self.register_data).place(x=50, y=420)

        btn_login = Button(self.root, text="Sign in", font=(
            "times new roman", 20, "bold"), command=self.login_again).place(x=200, y=460, width=150)

    def login_again(self):
        self.root.destroy()
        import login

    def clear(self):
        self.txt_fname.delete(0, END),
        self.txt_lname.delete(0, END),
        self.txt_contact.delete(0, END),
        self.txt_email.delete(0, END),
        self.txt_question.current(0),
        self.txt_answer.delete(0, END),
        self.txt_password.delete(0, END),
        self.txt_cpass.delete(0, END)

    def register_data(self):
        emailFormat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        PhonePattern = "^(0|91)?[6-9][0-9]{9}$"
        passwordFormat = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"

        if (self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_answer.get() == "" or self.txt_contact.get() == "" or self.txt_cpass.get() == "" or self.txt_password.get() == "" or self.txt_question.get() == "Select"):
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        elif not re.match('^[a-zA-Z]*$', self.var_fname.get()):
            messagebox.showerror('Error', 'Invalid First name!')
        elif not re.match('^[a-zA-Z]*$', self.txt_lname.get()):
            messagebox.showerror('Error', 'Invalid Last name!')
         # for checking Email
        elif not (re.match(emailFormat, self.txt_email.get())):
            messagebox.showerror('Error', 'Invalid email!', parent=self.root)
        # # for checking Phone Number
        elif not re.match(PhonePattern, self.txt_contact.get()):
            messagebox.showerror(
                'Error', 'Invalid phone number!')
        elif not re.match(passwordFormat, self.txt_password.get()):
            messagebox.showerror(
                'Error', 'Invalid password format!')
        elif self.txt_password.get() != self.txt_cpass.get():
            messagebox.showerror(
                "Error", "Password and confirm password should be same", parent=self.root)

        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="Student_result")
                cur = con.cursor()
                cur.execute(
                    "select * from participants where email=%s", self.txt_email.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "User already exist, please try with another email", parent=self.root)

                cur.execute("insert into participants (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.txt_question.get(),
                                self.txt_answer.get(),
                                self.txt_password.get(),
                                # self.txt_cpass.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo(
                    "Success", "Register Successful", parent=self.root)
                self.clear()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to : {str(es)}", parent=self.root)


root = Tk()

obj = Register(root)
root.mainloop()
