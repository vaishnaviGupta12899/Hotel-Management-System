from tkinter import *
from PIL import ImageTk, Image
from Hotel import Cust_Win
from room import Roombooking

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

     #==========================1st image==============================
        img1=Image.open(r"C:\Users\vaish\Downloads\1633410403702hotel-images\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimag1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimag1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

    #==================  logo ======================================
        img2 = Image.open(r"C:\Users\vaish\Downloads\1633410403702hotel-images\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimag2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimag2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

    # ==================  logo ======================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)


    #=================== main frame ==========================================

        main_frame=Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

    # ==================  menu ======================================
        lbl_title = Label(main_frame, text="MENU", font=("times new roman",20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230)

    # =================== btn frame ==========================================

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER", command=self.cust_details ,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

     # ==========================right side image==============================
        img3 = Image.open(r"C:\Users\vaish\Downloads\1633410403702hotel-images\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimag3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimag3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

    # ==========================down image==============================
        img4 = Image.open(r"C:\Users\vaish\Downloads\1633410403702hotel-images\hotel images\slide3.jpg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimag4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimag4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

    # ==========================right side image==============================
        img5 = Image.open(r"C:\Users\vaish\Downloads\1633410403702hotel-images\hotel images\slide3.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimag5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimag5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)






if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
