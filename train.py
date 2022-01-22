from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set", bg="white", font=("times new roman", 35, "bold"), fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\3.jpg")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        b2_1 = Button(self.root,command=self.train_classifier, text="Train Data", cursor="hand2", font=("times new roman", 30, "bold"), bg="darkblue", fg="red")
        b2_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\10.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # gray scale image
            imageNP=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ========== train classifier and save =======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets complted!!!")






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()