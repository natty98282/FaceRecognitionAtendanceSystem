from tkinter import *
from PIL import Image, ImageTk
from student import Student
from train import Train
import os
from face_recognitions import Face_Recognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1 image
        img = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # 2 image
        img1 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\2.JPG")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # 3 image
        img2 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\3.JPG")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        img3 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\favorite.JPG")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Face_Recognition Attendance System", bg="white", font=("times new roman", 35, "bold"), fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # student button
        img4 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\6.JPG")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Student_Detail",command=self.student_details, cursor="hand2",font=("times new roman", 15, "bold"),bg="darkblue", fg="gray")
        b1_1.place(x=200, y=300, width=220, height=40)

        img5 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\7.JPG")
        img5 = img5.resize((500, 130), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img,command=self.face_rec, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(bg_img,command=self.face_rec, text="Face_Recognition", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b2_1.place(x=500, y=300, width=220, height=40)

        img6 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\6.JPG")
        img6 = img6.resize((500, 130), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b3_1.place(x=800, y=300, width=220, height=40)


        # help desk
        img7 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\8.png")
        img7 = img7.resize((500, 130), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        b4_1 = Button(bg_img, text="Help_Desk", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # train_image
        img8 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\8.jpg")
        img8 = img8.resize((450, 130), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img,command=self.train_data, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=350, width=220, height=200)

        b5_1 = Button(bg_img,command=self.train_data, text="Train_New face", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b5_1.place(x=200, y=500, width=220, height=40)

        img9 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\9.jpg")
        img9 = img9.resize((300, 130), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=1100, y=350, width=220, height=200)

        b6_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b6_1.place(x=1100, y=500, width=220, height=40)

        img10 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\10.jpg")
        img10 = img10.resize((300, 130), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        b7.place(x=500, y=350, width=220, height=200)

        b7_1 = Button(bg_img,command=self.open_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b7_1.place(x=500, y=500, width=220, height=40)

        img11 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\11.jpg")
        img11 = img11.resize((300, 130), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=800, y=350, width=220, height=200)

        b8_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="gray")
        b8_1.place(x=800, y=500, width=220, height=40)

    #======== open img=====
    def open_img(self):
        os.startfile("faces")
    # ==========function buttons======
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
