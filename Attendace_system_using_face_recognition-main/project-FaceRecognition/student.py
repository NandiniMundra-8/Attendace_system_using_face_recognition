from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class  Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Manage Employee Department")
        
        # ============ variable ===========

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        
        # first image
        img=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\face-recognition.png")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\smart-attendance.jpg")
        img1=img1.resize((550,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=550,height=130)

        # third image
        img2=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((478,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimage2)
        f_label.place(x=1050,y=0,width=478,height=130)

        # bg image
        img3=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\bgImage.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lb1=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("serif",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=55,width=1500,height=600)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=740,height=580)
         
        img_left=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\img1.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=8,y=0,width=720,height=130)

        # current course frame
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=5,y=130,width=720,height=115)

        # Department
        dep_label=Label(current_course_frame,bg="white",text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,bg="white",text="Course",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year
        year_label=Label(current_course_frame,bg="white",text="Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,bg="white",text="Semester",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class  student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=5,y=130+115,width=720,height=300)

        # student ID
        student_Id_label=Label(class_student_frame,bg="white",text="Student ID:",font=("times new roman",13,"bold"))
        student_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        student_name_label=Label(class_student_frame,bg="white",text="Student Name:",font=("times new roman",13,"bold"))
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_division_label=Label(class_student_frame,bg="white",text="Class Division",font=("times new roman",13,"bold"))
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=17,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no
        roll_no_label=Label(class_student_frame,bg="white",text="Roll No:",font=("times new roman",13,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,bg="white",text="Gender:",font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date of birth
        date_of_birth_label=Label(class_student_frame,bg="white",text="Date of Birth:",font=("times new roman",13,"bold"))
        date_of_birth_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_of_birth_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        date_of_birth_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # email
        email_label=Label(class_student_frame,bg="white",text="Email:",font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone no
        phone_no_label=Label(class_student_frame,bg="white",text="Phone No:",font=("times new roman",13,"bold"))
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label=Label(class_student_frame,bg="white",text="Address:",font=("times new roman",13,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher name
        teacher_name_label=Label(class_student_frame,bg="white",text="Teacher Name:",font=("times new roman",13,"bold"))
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radiobutton1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=5,column=1)

        #buttons frame
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=205,width=715,height=35)

        # save button
        save_button=Button(button_frame,text="Save",command=self.add_data,font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_button.grid(row=0,column=0,sticky=W)

        # update button
        update_button=Button(button_frame,text="Update",command=self.update_data,font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_button.grid(row=0,column=1,sticky=W)

        # delet button
        delete_button=Button(button_frame,text="Delete",command=self.delete_data,font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_button.grid(row=0,column=2,sticky=W)

        # reset button
        reset_button=Button(button_frame,text="Reset",command=self.reset_data,font=("time new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_button.grid(row=0,column=3,sticky=W)
        
        #buttons frame
        button_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=0,y=240,width=715,height=35)

        
        # take photo sample
        take_photo_sample_button=Button(button_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("time new roman",13,"bold"),bg="blue",fg="white",width=34)
        take_photo_sample_button.grid(row=0,column=0,sticky=W)

        # update photo sample
        update_photo_sample_button=Button(button_frame1,text="Update Photo Sample",font=("time new roman",13,"bold"),bg="blue",fg="white",width=34)
        update_photo_sample_button.grid(row=0,column=1,sticky=W)

        
        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=720,height=580)

        img_right=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\student.jpg")
        img_right=img_right.resize((700,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_label=Label(right_frame,image=self.photoimg_right)
        f_label.place(x=8,y=0,width=700,height=130)

        # ==== search System =======

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=705,height=70)

        # search label
        search_label=Label(search_frame,bg="red",fg="white",text="Search By:",font=("times new roman",13,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        # search button
        search_button=Button(search_frame,text="Search",font=("time new roman",12,"bold"),bg="blue",fg="white",width=12)
        search_button.grid(row=0,column=3,sticky=W,padx=4)

        # showall button
        show_all_button=Button(search_frame,text="Show All",font=("time new roman",12,"bold"),bg="blue",fg="white",width=12)
        show_all_button.grid(row=0,column=4,sticky=W,padx=4)

        # table farme
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=705,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ====== function decration =========

    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="hr",password="hr",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()

                ))
                
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   
  
    # ==================fetch data=================
    def fetch_data(self):                
        conn=mysql.connector.connect(host="localhost",username="hr",password="hr",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    #======================get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #========== update function======
    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="hr",password="hr",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update Student set dep=%s,course=%s,year=%s,name=%s,semester=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get(),

                         ))
                
                else:
                    if not update:
                        return
                 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root) 
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
    #====delete function======
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student ",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="hr",password="hr",database="face_recognition")
                    my_cursor=conn.cursor()

                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
    #==== reset function====
    def reset_data(self):
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #====================Generated data set or take photo samples===============
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="hr",password="hr",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0 
                name=self.var_std_name
                for x in myresult:
                    id+=1
                    my_cursor.execute("update Student set dep=%s,course=%s,year=%s,name=%s,semester=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1,
                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #=========== Load predefiend data on face frontals from opencv=============
                face_classifier=cv2.CascadeClassifier(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #sacling factor=1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                       img_id+=1
                       face=cv2.resize(face_cropped(my_frame),(450,450))
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       
                       file_name_path="D:/Attendace_system_using_face_recognition-main/Attendace_system_using_face_recognition-main/project-FaceRecognition/dataset/"+str(name)+"."+str(id)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name_path,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                       break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data dets compled!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)








                
                    



            









    
            
            
            
            








        
        
        
        
        
        
        



        




        



    


        







    



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()