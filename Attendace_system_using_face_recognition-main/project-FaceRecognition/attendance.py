from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime 
import cv2
import os
import numpy as np


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")
         
         # first image
        img=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\Smart-attendance.jpg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=800,height=200)

        # second image
        img1=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=800,y=0,width=800,height=200)

        # bg image
        img3=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\bgImage.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lb1=Label(bg_img, text="ATTENDANCE SYSTEM", font=("serif",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=55,width=1480,height=580)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=580)
         
        img_left=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\img1.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,bg="white")
        left_inside_frame.place(x=0,y=135,width=710,height=370)

        #labels entry 
        #attendance id
        attendance_Id_label=Label(left_inside_frame,bg="white",text="Attendance ID:",font=("times new roman",13,"bold"))
        attendance_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        

        # Name
        rolllabel=Label(left_inside_frame, text="Roll:", bg="white", font="comicsansns 11 bold")
        rolllabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame, width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)
        # date
        nameLabel=Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)
        atten_name=ttk. Entry(left_inside_frame,width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

       
        # Department
        deplabel=Label(left_inside_frame,text="Department:", bg="white", font="comicsansns 11 bold")
        deplabel.grid(row=1,column=2)
        atten_dep=ttk.Entry(left_inside_frame,width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)
        # time
        timelabel=Label(left_inside_frame, text="Time:", bg="white",font="comicsansns 11 bold")
        timelabel.grid(row=2,column=0)
        atten_time=ttk.Entry(left_inside_frame,width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)
        # Date
        datelabel=Label(left_inside_frame, text="Date:",bg="white", font="comicsansns 11 bold")
        datelabel.grid(row=2,column=2)
        atten_date=ttk. Entry(left_inside_frame,width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)
        # attendance
        attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20, font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        button_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=300,width=715,height=35)

     
        imprt_button=Button(button_frame,text="Import Csv",font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        imprt_button.grid(row=0,column=0,sticky=W)

        
        exprt_button=Button(button_frame,text="Export Csv",font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        exprt_button.grid(row=0,column=1,sticky=W)

       
        update_button=Button(button_frame,text="Update",font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_button.grid(row=0,column=2,sticky=W)

        # reset button
        reset_button=Button(button_frame,text="Reset",font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_button.grid(row=0,column=3,sticky=W)
        
    
        # Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)
        
        # =============scroll bar table=============
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department", "time", "date","attendance") ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)


        self.AttendaceReportTable.heading("id",text="Attendance ID")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance")

        self.AttendaceReportTable["show"]="headings"

        self.AttendaceReportTable.column ("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department", width=100) 
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendance",width=100)




        self.AttendaceReportTable.pack(fill=BOTH,expand=1)
       



        









if  __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()  