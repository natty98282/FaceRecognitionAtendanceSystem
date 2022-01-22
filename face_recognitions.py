from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import cv2
import os
import face_recognition


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", bg="white", font=("times new roman", 35, "bold"),
                          fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\7.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\8.jpg")
        img_bottom = img_bottom.resize((680, 680), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=650, y=55, width=680, height=680)

        b2_1 = Button(f_lb2, command=self.face_recog, text="Face Recognition", cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="green", fg="white")
        b2_1.place(x=280, y=570, width=200, height=40)

    # =============attendance=========
    def mark_attendance(self, i, n, s, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (s not in name_list) and (s not in name_list) and (
                    n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{s},{d},{dtString},{d1},Present")

    # ======== face_recognition =======
    def face_recog(self):
        KNOWN_FACES_DIR = "faces/yalefaces"
        TOLERANCE = 0.5
        FRAME_THICKNESS = 3
        FONT_THICKNESS = 2
        MODEL = 'hog'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model

        # Returns (R, G, B) from name
        def name_to_color(name):
            color = [(ord(c.lower()) - 97) * 8 for c in name[:3]]
            return color

        print('Loading known faces...')
        known_faces = []
        known_names = []

        for name in os.listdir(KNOWN_FACES_DIR):

            for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
                # Load an image
                image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')

                encoding = face_recognition.face_encodings(image)[0]

                # Append encodings and name
                known_faces.append(encoding)
                known_names.append(name)
        print('Processing unknown faces...')
        video = cv2.VideoCapture(0)
        # Now let's loop over a folder of faces we want to label

        while True:


            ret, image = video.read()

            locations = face_recognition.face_locations(image, model=MODEL)

            encodings = face_recognition.face_encodings(image, locations)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            print(f', found {len(encodings)} face(s)')
            for face_encoding, face_location in zip(encodings, locations):

                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)

                match = None
                if True in results:  # If at least one is true, get a name of first of found labels
                    match = known_names[results.index(True)]
                    print(f' - {match} from {results}')

                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="nati5439",
                                                   database="my_db1")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Name from student where Student_id=" + str(match))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("select Roll from student where Student_id=" + str(match))
                    s = my_cursor.fetchone()
                    s = "+".join(s)

                    my_cursor.execute("select Dep from student where Student_id=" + str(match))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    my_cursor.execute("select Student_id from student where Student_id=" + str(match))
                    i = my_cursor.fetchone()
                    i = "+".join(i)

                    # Each location contains positions in order: top, right, bottom, left
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    # Get color by name using our fancy function
                    color = name_to_color(match)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    # Now we need smaller, filled grame below for a name
                    # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                    cv2.putText(image, f"ID:{i}", (face_location[3] + 10, face_location[2] + 15),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(image, f"Roll:{s}", (face_location[3] + 40, face_location[2] + 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(image, f"Name:{n}", (face_location[3] + 70, face_location[2] + 85),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(image, f"Department:{d}", (face_location[3] + 100, face_location[2] + 115),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, n, s, d)

                    # Wite a name
                    cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (200, 200, 200), FONT_THICKNESS)
                else:
                    # Each location contains positions in order: top, right, bottom, left
                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    # Get color by name using our fancy function
                    color = name_to_color("Unknown_Face")

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                    # Now we need smaller, filled grame below for a name
                    # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    # Paint frame
                    cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)

                    # Wite a name
                    cv2.putText(image, "Unknown_ face", (face_location[3] + 10, face_location[2] + 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

                # Show image
            cv2.imshow(filename, image)
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
