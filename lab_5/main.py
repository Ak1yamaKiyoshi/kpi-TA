import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime
class HashTableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hash Table App")
        self.geometry("400x400")

        self.students = {
            "lemish maxim": datetime.date(2005, 5, 5),
            "andrii": datetime.date(2004, 9, 6)
        }
        self.table_size = 25
        self.last_hash_function = None

        self.create_widgets()

    def create_widgets(self):
        name_label = ttk.Label(self, text="Name:")
        name_label.pack(pady=5)

        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        date_label = ttk.Label(self, text="Birthdate:")
        date_label.pack(pady=5)

        self.date_picker = DateEntry(self, date_pattern="yyyy-MM-dd")  # Use DateEntry from tkcalendar
        self.date_picker.pack(pady=5)

        saved_button = ttk.Button(self, text="Save", command=self.save_student)
        saved_button.pack(pady=5)

        clear_button = ttk.Button(self, text="Clear", command=self.clear_student)
        clear_button.pack(pady=5)

        linear_button = ttk.Button(self, text="Linear Probing", command=lambda: self.create_hash_table(self.linear_probing))
        linear_button.pack(pady=5)

        quadratic_button = ttk.Button(self, text="Quadratic Probing", command=lambda: self.create_hash_table(self.quadratic_probing))
        quadratic_button.pack(pady=5)

        self.result_text = tk.Text(self, width=40, height=10)
        self.result_text.pack(pady=5)

    def linear_probing(self, index, i, table_size):
        return (abs(index) + i) % table_size

    def quadratic_probing(self, index, i, table_size):
        return (abs(index) + i * i) % table_size

    def save_student(self):
        name = self.name_entry.get()
        if name in self.students:
            messagebox.showerror("Error", "Name already exists!")
            return

        birthdate = self.date_picker.get_date()
        self.students[name] = birthdate
        self.create_hash_table(self.last_hash_function)

    def clear_student(self):
        name = self.name_entry.get()
        if name in self.students:
            del self.students[name]
            self.create_hash_table(self.last_hash_function)
        else:
            messagebox.showerror("Error", "Element not found!")

    def create_hash_table(self, hash_function):
        self.last_hash_function = hash_function
        hash_table = [None] * self.table_size

        for name, birthdate in self.students.items():
            hash_code = hash(name)
            index = abs(hash_code) % self.table_size
            i = 1

            while hash_table[index] is not None:
                index = hash_function(hash_code, i, self.table_size)
                i += 1

                if i > self.table_size:
                    self.table_size += 1
                    new_hash_table = [None] * self.table_size
                    for j, item in enumerate(hash_table):
                        if item is not None:
                            new_hash_code = hash(item[0])
                            new_index = abs(new_hash_code) % self.table_size
                            new_i = 1
                            while new_hash_table[new_index] is not None:
                                new_index = hash_function(new_hash_code, new_i, self.table_size)
                                new_i += 1
                            new_hash_table[new_index] = item
                    hash_table = new_hash_table

            hash_table[index] = (name, birthdate)

        output = "Birthdays after hash table:\n"
        for i, item in enumerate(hash_table):
            if item is not None:
                output += f"{i}: {item[0]}\n"

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, output)

if __name__ == "__main__":
    app = HashTableApp()
    app.mainloop()