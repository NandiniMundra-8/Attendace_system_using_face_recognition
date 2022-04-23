
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os 
from student import Student
from train import Train  
from face_recognition import Face_recognition

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # first image
        img=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimage)
        f_label.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\facialrecognition.png")
        img1=img1.resize((550,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimage1)
        f_label.place(x=500,y=0,width=550,height=130)

        # third image
        img2=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\images.jpg")
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

        title_lb1=Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=("serif",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # student button
        img4=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
 
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("serif",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
 
        # Detect Face button
        img5=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
 
        b2=Button(bg_img,image=self.photoimage5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)
 
        b2_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("serif",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=500,y=300,width=220,height=40)

        # Attendance button
        self.photoimage1=ImageTk.PhotoImage(img1)
        self.photoimage1=ImageTk.PhotoImage(img1)
        img6=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimage6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
 
        b3_3=Button(bg_img,text="Attendance",cursor="hand2",font=("serif",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=800,y=300,width=220,height=40)

        # help button
        img7=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\HelpDesk.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimage7,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
 
        b4_4=Button(bg_img,text="Help Desk",cursor="hand2",font=("serif",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height=40)

        # train button
        img8=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)
 
        b5_5=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("serif",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=200,y=580,width=220,height=40)

        # Photo button
        img9=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)
 
        b6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("serif",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=500,y=580,width=220,height=40)

        # Developer button
        img10=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimage10,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)
 
        b7_7=Button(bg_img,text="Developer",cursor="hand2",font=("serif",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=800,y=580,width=220,height=40)

        # Exit button
        img11=Image.open(r"D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS) 
        self.photoimage11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimage11,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)
 
        b8_8=Button(bg_img,text="Exit",cursor="hand2",font=("serif",15,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1100,y=580,width=220,height=40)
    


    def open_img(self):
        os.startfile("D:\Attendace_system_using_face_recognition-main\Attendace_system_using_face_recognition-main\project-FaceRecognition\dataset")



        
    # ============functions buttons===============

    def student_details(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)


    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)
    

    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_recognition(self.new_window)

 
     


if __name__ == "__main__" :
    root=Tk()
    object=Face_recognition_system(root)
    root.mainloop()


