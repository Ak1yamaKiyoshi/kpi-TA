import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit, QWidget

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_head(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

class SingleLinkedListArray:
    def __init__(self):
        self.array = []

    def append(self, data):
        self.array.append(data)

    def remove_head(self):
        if len(self.array) == 0:
            return None
        removed_data = self.array[0]
        del self.array[0]
        return removed_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Queue")
        self.linked_list1 = SingleLinkedList()
        self.linked_list2 = SingleLinkedList()
        self.current_student1 = None
        self.current_student2 = None
        self.setup_ui()

    def setup_ui(self):
        
        main_layout = QVBoxLayout()

        # input from file
        file_input_layout = QHBoxLayout()
        file_input_label = QLabel("Load students from file:")
        self.file_input_button = QPushButton("Browse")
        self.file_input_button.clicked.connect(self.load_students)
        file_input_layout.addWidget(file_input_label)
        file_input_layout.addWidget(self.file_input_button)
        main_layout.addLayout(file_input_layout)

        # student first list
        student_info_layout1 = QHBoxLayout()
        student_name_label1 = QLabel("Student Name (List 1):")
        self.student_name_text1 = QLabel("")
        student_score_label1 = QLabel("Student Score:")
        self.student_score_text1 = QLabel("")
        student_info_layout1.addWidget(student_name_label1)
        student_info_layout1.addWidget(self.student_name_text1)
        student_info_layout1.addWidget(student_score_label1)
        student_info_layout1.addWidget(self.student_score_text1)
        main_layout.addLayout(student_info_layout1)

        # students second list
        buttons_layout1 = QHBoxLayout()
        self.pass_button1 = QPushButton("Pass")
        self.pass_button1.clicked.connect(lambda: self.process_student(self.linked_list1, True))
        self.fail_button1 = QPushButton("Fail")
        self.fail_button1.clicked.connect(lambda: self.process_student(self.linked_list1, False))
        buttons_layout1.addWidget(self.pass_button1)
        buttons_layout1.addWidget(self.fail_button1)
        main_layout.addLayout(buttons_layout1)

    
        student_info_layout2 = QHBoxLayout()
        student_name_label2 = QLabel("Student Name (List 2):")
        self.student_name_text2 = QLabel("")
        student_score_label2 = QLabel("Student Score:")
        self.student_score_text2 = QLabel("")
        student_info_layout2.addWidget(student_name_label2)
        student_info_layout2.addWidget(self.student_name_text2)
        student_info_layout2.addWidget(student_score_label2)
        student_info_layout2.addWidget(self.student_score_text2)
        main_layout.addLayout(student_info_layout2)


        buttons_layout2 = QHBoxLayout()
        self.pass_button2 = QPushButton("Pass")
        self.pass_button2.clicked.connect(lambda: self.process_student(self.linked_list2, True))
        self.fail_button2 = QPushButton("Fail")
        self.fail_button2.clicked.connect(lambda: self.process_student(self.linked_list2, False))
        buttons_layout2.addWidget(self.pass_button2)
        buttons_layout2.addWidget(self.fail_button2)
        main_layout.addLayout(buttons_layout2)

        report_lists_layout = QHBoxLayout()
        report_list_label = QLabel("Report Lists:")
        self.report_list1 = QListWidget()
        self.score_list1 = QListWidget()
        self.result_list1 = QListWidget()
        self.report_list2 = QListWidget()
        self.score_list2 = QListWidget()
        self.result_list2 = QListWidget()
        report_lists_layout.addWidget(report_list_label)
        report_lists_layout.addWidget(self.report_list1)
        report_lists_layout.addWidget(self.score_list1)
        report_lists_layout.addWidget(self.result_list1)
        report_lists_layout.addWidget(self.report_list2)
        report_lists_layout.addWidget(self.score_list2)
        report_lists_layout.addWidget(self.result_list2)
        main_layout.addLayout(report_lists_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def load_students(self):
        file_dialog = QFileDialog()
        file_name, _ = file_dialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
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
        if linked_list.head is None:
        
            if linked_list == self.linked_list1:
                self.student_name_text1.setText("")
                self.student_score_text1.setText("")
                self.pass_button1.setEnabled(False)
                self.fail_button1.setEnabled(False)
            else:
                self.student_name_text2.setText("")
                self.student_score_text2.setText("")
                self.pass_button2.setEnabled(False)
                self.fail_button2.setEnabled(False)
        else:
            current_student = linked_list.remove_head()
            random_score = random.randint(1, 100)
            if linked_list == self.linked_list1:
                self.student_name_text1.setText(current_student)
                self.student_score_text1.setText(str(random_score))
                self.pass_button1.setEnabled(True)
                self.fail_button1.setEnabled(True)
            else:
                self.student_name_text2.setText(current_student)
                self.student_score_text2.setText(str(random_score))
                self.pass_button2.setEnabled(True)
                self.fail_button2.setEnabled(True)

    def process_student(self, linked_list, passed):
        if linked_list.head is None:
            self.update_student_info(linked_list)
            return

        student_name = self.student_name_text1.text() if linked_list == self.linked_list1 else self.student_name_text2.text()
        student_score = self.student_score_text1.text() if linked_list == self.linked_list1 else self.student_score_text2.text()
        if linked_list == self.linked_list1:
            self.report_list1.addItem(student_name)
            self.score_list1.addItem(student_score)
            if passed:
                self.result_list1.addItem("Passed")
            else:
                self.result_list1.addItem("Failed")
        else:
            self.report_list2.addItem(student_name)
            self.score_list2.addItem(student_score)
            if passed:
                self.result_list2.addItem("Passed")
            else:
                self.result_list2.addItem("Failed")

        self.update_student_info(linked_list)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()