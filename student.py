from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from os import listdir
import time


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #  ========variables=======
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

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

        img3 = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\jit1.JPG")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Student_Management", bg="gray", font=("times new roman", 35, "bold"), fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1500, height=600)

        # left label frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student_Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=550)

        img_left = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\1.jpg")
        img_left = img_left.resize((720, 70), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=70)

        # current course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="course_information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=70, width=720, height=150)
        # Department
        dep_lable = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lable.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 state="read only")
        dep_combo["values"] = ("Select Department", "Computer", "ECE", "Mechanical", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course
        course_lable = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_lable.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), state="read only")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_lable = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_lable.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), state="read only")
        year_combo["values"] = ("Select Year", "i", "ii", "iii", "iv", "v")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_lable = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_lable.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                      font=("times new roman", 12, "bold"), state="read only")
        semester_combo["values"] = ("Select Semester", "Semester I", "Semester II")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student_Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=660, height=580)

        # Class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="course_information",
                                         font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=185, width=720, height=300)

        studentid_lable = Label(class_student_frame, text="Student_ID:", font=("times new roman", 12, "bold"),
                                bg="white")
        studentid_lable.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20,
                                    font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        studentName_lable = Label(class_student_frame, text="Student_Name:", font=("times new roman", 12, "bold"),
                                  bg="white")
        studentName_lable.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20,
                                      font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        studentDiv_lable = Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"),
                                 bg="white")
        studentDiv_lable.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        studentDiv_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20,
                                     font=("times new roman", 12, "bold"))
        studentDiv_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Roll_no_lable = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        Roll_no_lable.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Roll_No_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20,
                                  font=("times new roman", 12, "bold"))
        Roll_No_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        gender_lable = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_lable.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), state="read only")
        gender_combo["values"] = ("Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        dob_lable = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_lable.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        email_lable = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_lable.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20,
                                font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        phoneno_lable = Label(class_student_frame, text="Phone_No:", font=("times new roman", 12, "bold"), bg="white")
        phoneno_lable.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20,
                                font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        adress_lable = Label(class_student_frame, text="Adress:", font=("times new roman", 12, "bold"), bg="white")
        adress_lable.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        adress_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,
                                 font=("times new roman", 12, "bold"))
        adress_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        teacher_lable = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"),
                              bg="white")
        teacher_lable.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20,
                                  font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # Buttons_frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=17, font=("times new roman", 13, "bold"),
                          bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        Update_btn = Button(btn_frame, command=self.update_data, text="Update", width=17,
                            font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        Update_btn.grid(row=0, column=1)

        Delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=17,
                            font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        Delete_btn.grid(row=0, column=2)

        Reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=17,
                           font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        Reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=35,
                                font=("times new roman", 13, "bold"),
                                bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35,
                                  font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1)

        # right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student_Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=585, height=550)

        img_right = Image.open(r"C:\Users\natty\Desktop\Face_Recognition_System\collage_image\1.jpg")
        img_right = img_left.resize((580, 70), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=580, height=70)
        # ======serach system=====
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="course_information",
                                  font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=70, width=580, height=70)
        # Department
        search_lable = Label(search_frame, text="Search by:", font=("times new roman", 12, "bold"), bg="green",
                             fg="white")
        search_lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="read only")
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Search_btn = Button(search_frame, text="Search", width=15, font=("times new roman", 13, "bold"), bg="blue",
                            fg="white")
        Search_btn.grid(row=0, column=2)

        Searchall_btn = Button(search_frame, text="Search All", width=15, font=("times new roman", 13, "bold"),
                               bg="blue", fg="white")
        Searchall_btn.grid(row=0, column=3)

        # ======Table frame======
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=135, width=580, height=150)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div",
                                                               "dob", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone_no")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # =============function declaration=======
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", password="nati5439", database="my_db1")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into my_db1.student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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
                messagebox.showinfo("success", "Student registered successfully", parent=self.root)
            except Exception as es:
                messagebox.showinfo("Error", f"Due To:{str(es)}", parent=self.root)
        # =========fetch data =========

    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="nati5439", database="my_db1")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ========== get cursor ========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

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

    # ======update function=======
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you Want to Update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="nati5439",
                                                   database="my_db1")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name =%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                        (
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
                            self.var_std_id.get()

                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("seccess", "seccessfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # =======delete functiion=====
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="nati5439",
                                                   database="my_db1")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "seccessfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{(es)}", parent=self.root)

    # ======== Reset fincton=======
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # ========== generate dataset =======
    def generate_dataset(self):

        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                messagebox.askyesno("Student Take Photo Page", "Do you want to Picture of this student",
                                    parent=self.root)

                conn = mysql.connector.connect(host="127.0.0.1", user="root", password="nati5439", database="my_db1")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = self.var_std_id.get()
                name = self.var_std_name.get()

                my_cursor.execute(
                    "update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name =%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                    (
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
                        self.var_std_id.get()

                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                directory_roots = "faces"
                root_dir = listdir(directory_roots)
                for directory in root_dir:
                    if directory == ".DS_Store":
                        root_dir.remove(directory)
                directory_root = f"faces/yalefaces/{str(id)}"
                if os.path.exists(directory_root):
                    import shutil
                    shutil.rmtree(directory_root)
                os.makedirs(directory_root)
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.1, 5)
                    for x, y, w, h in faces:
                        face_cropped = gray[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                time.sleep(5)
                im_id = 0

                while True:

                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        im_id = im_id + 1

                    if im_id == 1:
                        text = "DONE"

                        face = cv2.resize(my_frame, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
                        file_name_path = f"{directory_root}/picture" + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)
                        messagebox.showinfo("Result", "Generating data sets completed")

                        if cv2.waitKey(2) & 0xFF == ord('q') or im_id==1:
                            break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
