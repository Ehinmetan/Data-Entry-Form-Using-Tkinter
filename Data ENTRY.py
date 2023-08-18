import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
window = tk.Tk()
window.title("Data Entry")


# adding widgets..we do this so all the frame will act on window and the window will act on the frame
frame = tk.Frame(window)
frame.pack()

def enter_data():
    accept = accept_var.get()
    if accept == 'Accepted':
        fn = firstname_entry.get()
        ln = lastname_entry.get()


        # validating entry records
        if fn and ln:
            Title = title_combobox.get()
            age = age_spinbox.get()
            Nationality = nationality_combobox.get()

            numcourses= numcourses_spinbox.get()
            numsemester = numsemester_spinbox.get()
        #         to be able to retrieve information from a checkbox,we will bind the checkbox to a variable

            registerInfo = register.get()

            print(fn, '', ln, '', accept)
            print('-'*40)
        else:
            tk.messagebox.showwarning(title="Error", message="Firstname and Lastname are required")
    else:
        tk.messagebox.showwarning(title="Error", message="Terms and condition required")


user_info = tk.LabelFrame(frame,text="User information")
user_info.grid(row=0,column=0)

firstname = tk.Label(user_info, text="Firstname")
firstname.grid(row=0, column=0)

firstname_entry = tk.Entry(user_info)
firstname_entry.grid(row=1, column=0)

lastname = tk.Label(user_info, text="Lastname")
lastname.grid(row=0, column=1)

lastname_entry = tk.Entry(user_info)
lastname_entry.grid(row=1, column=1)

# creating combo box...first is to import ttk from tkinter at the top

title = tk.Label(user_info, text="Title")
title_combobox = ttk.Combobox(user_info, value=["", "Mr", "Mrs", "Miss"])
title.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info, text="Year")
age_spinbox = tk.Spinbox(user_info, from_=1980, to = 2023)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info, text="Nationality")
nationality_combobox = ttk.Combobox(user_info, value=["", "Nigeria", "American", "Ghanain"])

nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

course_frame = tk.LabelFrame(frame, text="courses information",bg="dim gray")
course_frame.grid(row=1, column=0,sticky="news", padx=10, pady=5)

reg_label = tk.Label(course_frame, text="Registration")
reg_label.grid(row=0, column=0)

register = tk.StringVar(value="Not Registered")
reg_check = tk.Checkbutton(course_frame,text="Currently Registered",
                           variable=register, onvalue="Registered", offvalue="Not Registered")
reg_check.grid(row=1, column=0)

numcourses_label = tk.Label(course_frame, text=" # Completed courses")
numcourses_spinbox = tk.Spinbox(course_frame, from_=0, to ="infinity")
numcourses_label.grid(row= 0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemester_label=  tk.Label(course_frame, text="# Semester")
numsemester_spinbox = tk.Spinbox(course_frame, from_=0, to ="infinity")
numsemester_label.grid(row= 0, column=2)
numsemester_spinbox.grid(row=1, column=2)

terms_frame = tk.LabelFrame(frame, text= "Terms and condition")
terms_frame.grid(row =2, column =0, sticky="news", padx=10, pady=5)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame,text="I agree with the Terms and condition",
                           variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

button = tk.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=10, pady=5)

for widget in user_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


window.mainloop()