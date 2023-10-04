import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

def register_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    student = Student(name, age, grade)
    messagebox.showinfo("Registration Successful", f"Student {student.name} registered successfully!")

def create_student_form():
    student_form = tk.Toplevel(root)
    student_form.title("Student Form")

    name_label = tk.Label(student_form, text="Name:", font=("Arial", 12, "bold"))
    name_label.pack()
    name_entry = tk.Entry(student_form, font=("Arial", 12))
    name_entry.pack()

    age_label = tk.Label(student_form, text="Age:", font=("Arial", 12, "bold"))
    age_label.pack()
    age_entry = tk.Entry(student_form, font=("Arial", 12))
    age_entry.pack()

    grade_label = tk.Label(student_form, text="Grade:", font=("Arial", 12, "bold"))
    grade_label.pack()
    grade_entry = tk.Entry(student_form, font=("Arial", 12))
    grade_entry.pack()

    register_button = tk.Button(student_form, text="Register", command=register_student, font=("Arial", 12))
    register_button.pack()

def create_teacher_form():
    teacher_form = tk.Toplevel(root)
    teacher_form.title("Teacher Form")

    name_label = tk.Label(teacher_form, text="Name:", font=("Arial", 12, "bold"))
    name_label.pack()
    name_entry = tk.Entry(teacher_form, font=("Arial", 12))
    name_entry.pack()

    subject_label = tk.Label(teacher_form, text="Subject:", font=("Arial", 12, "bold"))
    subject_label.pack()
    subject_entry = tk.Entry(teacher_form, font=("Arial", 12))
    subject_entry.pack()

    save_button = tk.Button(teacher_form, text="Save", command=save_teacher, font=("Arial", 12))
    save_button.pack()

def save_teacher():
    name = name_entry.get()
    subject = subject_entry.get()

    teacher = Teacher(name, subject)
    messagebox.showinfo("Save Successful", f"Teacher {teacher.name} saved successfully!")

# Create the main window
root = tk.Tk()
root.title("School Management System-for developer zack")

# Configure the window background color
root.configure(background="#f0f0f0")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create menu options
home_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=home_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)

contact_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# Configure the menu bar background color
menu_bar.configure(bg="red")

# Create student registration button
register_button = tk.Button(root, text="Student Registration", command=create_student_form, font=("Arial", 14, "bold"))
register_button.pack(pady=10)

# Create teacher form button
teacher_button = tk.Button(root, text="Teacher Form", command=create_teacher_form, font=("Arial", 14, "bold"))
teacher_button.pack(pady=10)

# Create welcome description
welcome_label = tk.Label(root, text="Welcome to the School Management System", font=("Arial", 16, "bold"), bg="#f0f0f0")
welcome_label.pack(pady=50)

# Create additional descriptions
description_label = tk.Label(root, text="This system allows you to manage students and teachers in your school.", font=("Arial", 12), bg="#f0f0f0")
description_label.pack(pady=10)

description_label = tk.Label(root, text="Click 'Student Registration' to register a new student.", font=("Arial", 12), bg="#f0f0f0")
description_label.pack(pady=5)

description_label = tk.Label(root, text="Click 'Teacher Form' to save information about a teacher.", font=("Arial", 12), bg="#f0f0f0")
description_label.pack(pady=5)

description_label = tk.Label(root, text="Click 'admin Registration' to register a new student.", font=("Arial", 12), bg="#f0f0f0")
description_label.pack(pady=5)

# Create footer
footer_label = tk.Label(root, text="© 2023 School Management System. zack daahir.", font=("Arial", 10), bg="#f0f0f0")
footer_label.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()