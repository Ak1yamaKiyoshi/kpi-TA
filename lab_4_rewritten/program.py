import tkinter as tk
from tkinter import filedialog
import random
from main import SingleLinkedList

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Queue")
        self.linked_list1 = []
        self.linked_list2 = []
        self.current_student1 = None
        self.current_student2 = None
        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self)

        # input from file
        file_input_frame = tk.Frame(main_frame)
        file_input_label = tk.Label(file_input_frame, text="Load students from file:")
        self.file_input_button = tk.Button(file_input_frame, text="Browse", command=self.load_students)
        file_input_label.pack(side=tk.LEFT)
        self.file_input_button.pack(side=tk.LEFT)
        file_input_frame.pack()

        # student first list
        student_info_frame1 = tk.Frame(main_frame)
        student_name_label1 = tk.Label(student_info_frame1, text="Student Name (List 1):")
        self.student_name_text1 = tk.Label(student_info_frame1, text="")
        student_score_label1 = tk.Label(student_info_frame1, text="Student Score:")
        self.student_score_text1 = tk.Label(student_info_frame1, text="")
        student_name_label1.pack(side=tk.LEFT)
        self.student_name_text1.pack(side=tk.LEFT)
        student_score_label1.pack(side=tk.LEFT)
        self.student_score_text1.pack(side=tk.LEFT)
        student_info_frame1.pack()

        # students second list
        buttons_frame1 = tk.Frame(main_frame)
        self.pass_button1 = tk.Button(buttons_frame1, text="Pass", command=lambda: self.process_student(self.linked_list1, True))
        self.fail_button1 = tk.Button(buttons_frame1, text="Fail", command=lambda: self.process_student(self.linked_list1, False))
        self.pass_button1.pack(side=tk.LEFT)
        self.fail_button1.pack(side=tk.LEFT)
        buttons_frame1.pack()

        student_info_frame2 = tk.Frame(main_frame)
        student_name_label2 = tk.Label(student_info_frame2, text="Student Name (List 2):")
        self.student_name_text2 = tk.Label(student_info_frame2, text="")
        student_score_label2 = tk.Label(student_info_frame2, text="Student Score:")
        self.student_score_text2 = tk.Label(student_info_frame2, text="")
        student_name_label2.pack(side=tk.LEFT)
        self.student_name_text2.pack(side=tk.LEFT)
        student_score_label2.pack(side=tk.LEFT)
        self.student_score_text2.pack(side=tk.LEFT)
        student_info_frame2.pack()

        buttons_frame2 = tk.Frame(main_frame)
        self.pass_button2 = tk.Button(buttons_frame2, text="Pass", command=lambda: self.process_student(self.linked_list2, True))
        self.fail_button2 = tk.Button(buttons_frame2, text="Fail", command=lambda: self.process_student(self.linked_list2, False))
        self.pass_button2.pack(side=tk.LEFT)
        self.fail_button2.pack(side=tk.LEFT)
        buttons_frame2.pack()

        report_lists_frame = tk.Frame(main_frame)
        report_list_label = tk.Label(report_lists_frame, text="Report Lists:")
        self.report_list1 = tk.Listbox(report_lists_frame)
        self.score_list1 = tk.Listbox(report_lists_frame)
        self.result_list1 = tk.Listbox(report_lists_frame)
        self.report_list2 = tk.Listbox(report_lists_frame)
        self.score_list2 = tk.Listbox(report_lists_frame)
        self.result_list2 = tk.Listbox(report_lists_frame)
        report_list_label.pack(side=tk.LEFT)
        self.report_list1.pack(side=tk.LEFT)
        self.score_list1.pack(side=tk.LEFT)
        self.result_list1.pack(side=tk.LEFT)
        self.report_list2.pack(side=tk.LEFT)
        self.score_list2.pack(side=tk.LEFT)
        self.result_list2.pack(side=tk.LEFT)
        report_lists_frame.pack()

        main_frame.pack()

    def load_students(self):
        file_name = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    num_students = len(lines)
                    for i in range(num_students):
                        self.linked_list1.append(lines[i].strip())
                    for i in range(num_students):
                        self.linked_list2.append(lines[i].strip())
                self.update_student_info(self.linked_list1)
                self.update_student_info(self.linked_list2)
            except (IOError, OSError) as e:
                print(f"Error opening file: {e}")

    def update_student_info(self, linked_list):
        if not linked_list:
            if linked_list == self.linked_list1:
                self.student_name_text1.config(text="")
                self.student_score_text1.config(text="")
                self.pass_button1.config(state=tk.DISABLED)
                self.fail_button1.config(state=tk.DISABLED)
            else:
                self.student_name_text2.config(text="")
                self.student_score_text2.config(text="")
                self.pass_button2.config(state=tk.DISABLED)
                self.fail_button2.config(state=tk.DISABLED)
        else:
            current_student = linked_list.pop(0)
            random_score = random.randint(1, 100)
            if linked_list == self.linked_list1:
                self.student_name_text1.config(text=current_student)
                self.student_score_text1.config(text=str(random_score))
                self.pass_button1.config(state=tk.NORMAL)
                self.fail_button1.config(state=tk.NORMAL)
            else:
                self.student_name_text2.config(text=current_student)
                self.student_score_text2.config(text=str(random_score))
                self.pass_button2.config(state=tk.NORMAL)
                self.fail_button2.config(state=tk.NORMAL)

    def process_student(self, linked_list, passed):
        if not linked_list:
            self.update_student_info(linked_list)
            return

        student_name = self.student_name_text1.cget("text") if linked_list == self.linked_list1 else self.student_name_text2.cget("text")
        student_score = self.student_score_text1.cget("text") if linked_list == self.linked_list1 else self.student_score_text2.cget("text")
        if linked_list == self.linked_list1:
            self.report_list1.insert(tk.END, student_name)
            self.score_list1.insert(tk.END, student_score)
            if passed:
                self.result_list1.insert(tk.END, "Passed")
            else:
                self.result_list1.insert(tk.END, "Failed")
        else:
            self.report_list2.insert(tk.END, student_name)
            self.score_list2.insert(tk.END, student_score)
            if passed:
                self.result_list2.insert(tk.END, "Passed")
            else:
                self.result_list2.insert(tk.END, "Failed")

        self.update_student_info(linked_list)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
