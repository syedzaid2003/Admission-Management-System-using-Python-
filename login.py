from tkinter import*
from tkinter import ttk
from tkinter import Frame as TkFrame
from PIL import Image,ImageTk
from tkinter import messagebox
from student3 import admission


class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("face recognition system")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hk699\OneDrive\Desktop\python pictures\thumb-1920-1350425.png") 
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        TkFrame=Frame(self.root,bg="black")
        TkFrame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\hk699\OneDrive\Desktop\python pictures\f3.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(TkFrame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #lable
        username_lable=Label(TkFrame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lable.place(x=70,y=155)

        self.txtuser=ttk.Entry(TkFrame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lable=Label(TkFrame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lable.place(x=70,y=225)

        self.txtpass=ttk.Entry(TkFrame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #================= Icon Images===============
        img2=Image.open(r"C:\Users\hk699\OneDrive\Desktop\python pictures\exit-button.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\hk699\OneDrive\Desktop\python pictures\exit-button.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=393,width=25,height=25)

        # loginbutton
        loginbtn=Button(TkFrame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        ## registerbutton
        #registerbtn=Button(TkFrame,text="New User register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        #registerbtn.place(x=45,y=350,width=120)

        ## forgetpasswordbutton 
        #forgetbtn=Button(TkFrame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        #forgetbtn.place(x=20,y=370,width=160)



    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="itachi" and self.txtpass.get()=="007":
             messagebox.showinfo("Success","Welcome to Admission Management System")
             self.root.destroy()  # Close the login window
             root = Tk()
             ap=admission(root)  # Create an instance of the admission class
             root.mainloop()
        else:
            messagebox.showerror("Error","Invalid username or password")

if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()