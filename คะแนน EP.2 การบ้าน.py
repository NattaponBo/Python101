from tkinter import *

def show_score(subject):
    max_score = 50
    result_label.config(text=f"คะแนนเต็มของ {subject} คือ {max_score} คะแนน")

GUI = Tk()
GUI.title("แสดงคะแนนเต็มของวิชาเรียน")
GUI.geometry("600x500")
GUI.config(bg="#0F4C81")

subject_frame = Frame(GUI, bg="#F6F6F6")
subject_frame.place(relx=0.5, rely=0.5, anchor="center")

# สร้าง Label หัวข้อ
title_label = Label(subject_frame, text="แสดงคะแนนเต็มของวิชาเรียน", font=("Helvetica", 18), pady=10, bg="#F6F6F6")
title_label.grid(row=0, column=0, columnspan=2)

subjects = ["ภาษาไทย", "คณิตศาสตร์", "วิทยาศาสตร์", "ภาษาอังกฤษ", "ศิลปะ", "ดนตรี", "การงานอาชีพ", "ภูมิศาสตร์", "ประวัติศาสตร์", "สุขศึกษา"]
for i, subject in enumerate(subjects):
    subject_button = Button(subject_frame, text=f"{subject} ({50} คะแนน)", font=("Helvetica", 14), padx=10, pady=5, bg="#EAEAEA", activebackground="#D0D0D0", fg="#000000", command=lambda s=subject: show_score(s))
    subject_button.grid(row=i//2+1, column=i%2, padx=5, pady=5, sticky="nsew")

result_label = Label(GUI, text="กรุณาเลือกวิชา", font=("Helvetica", 16), fg="#FFFFFF", bg="#0F4C81")
result_label.place(relx=0.5, rely=0.9, anchor="center")

GUI.mainloop()
