"""                                     
Що важливо:
Обидва ці хешування використовують відкриті під капотом.
Закрите хешування потрібно щоб хендлити колізії.
Це і є його основною проблемою.

Hopscotch хешування дивиться на n елементів поруч, щоб закинути елемент куди треба.
Cok шось там намагається натомість засейвити елемент у інші, допоміжні таблиці.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

class HashTableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hash Table App")
        self.geometry("400x400")

        self.students = {}
        self.table_size = 2500
        # Separate hash tables for each hashing technique
        self.cuckoo_hash_table1 = [None] * self.table_size
        self.cuckoo_hash_table2 = [None] * self.table_size
        self.hopscotch_hash_table = [None] * self.table_size
        self.create_widgets()

    def create_widgets(self):
        name_label = ttk.Label(self, text="Name:")
        name_label.pack(pady=5)

        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        date_label = ttk.Label(self, text="Birthdate:")
        date_label.pack(pady=5)

        self.date_picker = DateEntry(self, date_pattern="yyyy-MM-dd")  
        self.date_picker.pack(pady=5)

        save_button = ttk.Button(self, text="Save", command=self.save_student)
        save_button.pack(pady=5)

        clear_button = ttk.Button(self, text="Clear", command=self.clear_student)
        clear_button.pack(pady=5)

        cuckoo_button = ttk.Button(self, text="Cuckoo Hashing", command=self.display_cuckoo_hashing)
        cuckoo_button.pack(pady=5)

        hopscotch_button = ttk.Button(self, text="Hopscotch Hashing", command=self.display_hopscotch_hashing)
        hopscotch_button.pack(pady=5)

        search_button = ttk.Button(self, text="Search", command=self.search_student)
        search_button.pack(pady=5)

        self.result_text = tk.Text(self, width=40, height=10)
        self.result_text.pack(pady=5)

        self.last_action_label = ttk.Label(self, text="Last action: None")
        self.last_action_label.pack(pady=5)

    def update_last_action(self, action):
        self.last_action_label.config(text=f"Last action: {action}")


    def hash1(self, key):
        return abs(hash(key)) % self.table_size

    def hash2(self, key):
        return (abs(hash(key)) * 5) % self.table_size

    def save_student(self, send_messagebox=True):
        name = self.name_entry.get().lower()
        birthdate = self.date_picker.get_date()
        #if name in self.students:
        #    messagebox.showerror("Error", "Name already exists!")
        #    return
        self.students[name] = birthdate
        
        if not self.insert_cuckoo(name, birthdate, send_messagebox):
            if send_messagebox:
                messagebox.showerror("Error", "Failed to insert in Cuckoo Hashing, rehashing needed!")
            return
        if not self.insert_hopscotch(name, birthdate, send_messagebox):
            if send_messagebox:
                messagebox.showerror("Error", "Failed to insert in Hopscotch Hashing, table might be full!")
            return
        if send_messagebox:
            messagebox.showinfo("Success", "Student saved successfully!")
            self.update_last_action("Saved student")


    def clear_student(self, send_messagebox=False):
        name = self.name_entry.get().lower()
        if name in self.students:
            del self.students[name]
            # Remove from cuckoo hash tables
            hash_index1 = self.hash1(name)
            if self.cuckoo_hash_table1[hash_index1] and self.cuckoo_hash_table1[hash_index1][0] == name:
                self.cuckoo_hash_table1[hash_index1] = None
            hash_index2 = self.hash2(name)
            if self.cuckoo_hash_table2[hash_index2] and self.cuckoo_hash_table2[hash_index2][0] == name:
                self.cuckoo_hash_table2[hash_index2] = None

            # Remove from hopscotch hash table
            hash_index = self.hash1(name)
            for i in range(5):  # Check current and next 4 slots for hopscotch
                new_index = (hash_index + i) % self.table_size
                if self.hopscotch_hash_table[new_index] and self.hopscotch_hash_table[new_index][0] == name:
                    self.hopscotch_hash_table[new_index] = None
                    messagebox.showinfo("Success", "Student cleared successfully!")
                    break
        else: 
            if send_messagebox:
                messagebox.showerror("Error", "Failed to remove due student is not exitsting!")
        if send_messagebox:
            self.update_last_action("Cleared student")


    def insert_cuckoo(self, key, value, count=0, table=1, send_messagebox=True):
        if count > self.table_size:
            return False
        if table == 1:
            # Перехешування
            hash_index = self.hash1(key)
            if self.cuckoo_hash_table1[hash_index] is None:
                self.cuckoo_hash_table1[hash_index] = (key, value)
                return True
            else:
                displaced_key, displaced_value = self.cuckoo_hash_table1[hash_index]
                self.cuckoo_hash_table1[hash_index] = (key, value)
                return self.insert_cuckoo(displaced_key, displaced_value, count + 1, 2)
        else:
            # Перехешування
            hash_index = self.hash2(key)
            if self.cuckoo_hash_table2[hash_index] is None:
                self.cuckoo_hash_table2[hash_index] = (key, value)
                return True
            else:
                displaced_key, displaced_value = self.cuckoo_hash_table2[hash_index]
                self.cuckoo_hash_table2[hash_index] = (key, value)
                return self.insert_cuckoo(displaced_key, displaced_value, count + 1, 1)

    def insert_hopscotch(self, key, value ,send_messagebox=True):
        hash_index = self.hash1(key)
        if self.hopscotch_hash_table[hash_index] is None:
            self.hopscotch_hash_table[hash_index] = (key, value)
            return True
        else:
            for i in range(1, self.table_size):
                new_index = (hash_index + i) % self.table_size
                if self.hopscotch_hash_table[new_index] is None:
                    self.hopscotch_hash_table[new_index] = (key, value)
                    return True
        return False 

    def search_student(self, send_messagebox=True):
        name = self.name_entry.get().lower()
        if name not in self.students:
            if send_messagebox:
                messagebox.showinfo("Search Result", "Student not found!")
            return
        birthdate = self.students[name]
        found_in_cuckoo = self.search_cuckoo(name)
        found_in_hopscotch = self.search_hopscotch(name)
        if found_in_cuckoo and send_messagebox:
            messagebox.showinfo("Search Result", f"Student found in Cuckoo Hashing: {name}, {birthdate}")
        elif found_in_hopscotch and send_messagebox:
            messagebox.showinfo("Search Result", f"Student found in Hopscotch Hashing: {name}, {birthdate}")
        elif send_messagebox:
            messagebox.showinfo("Search Result", "Student not found in any hashing method!")

        name = self.name_entry.get().lower()
        if name not in self.students and send_messagebox:
            self.update_last_action("Search: Student not found")
        elif send_messagebox:
            self.update_last_action(f"Search: Found {name}")



    def search_cuckoo(self, key, send_messagebox=True):
        hash_index1 = self.hash1(key)
        if self.cuckoo_hash_table1[hash_index1] and self.cuckoo_hash_table1[hash_index1][0] == key:
            return True
        hash_index2 = self.hash2(key)
        if self.cuckoo_hash_table2[hash_index2] and self.cuckoo_hash_table2[hash_index2][0] == key:
            
            return True
        if send_messagebox:
            self.update_last_action("Failed search in cuckoo")
        return False

    def search_hopscotch(self, key, send_messagebox=True):
        hash_index = self.hash1(key)
        for i in range(5):  # Check current and next 4 slots
            new_index = (hash_index + i) % self.table_size
            if self.hopscotch_hash_table[new_index] and self.hopscotch_hash_table[new_index][0] == key:
                if send_messagebox:
                    self.update_last_action("Success search in hopscotch")
                return True
        if send_messagebox:
            self.update_last_action("Failed search in hopscotch")
        return False

    def display_cuckoo_hashing(self):
        output = "Cuckoo Hashing:\n"
        for i, item in enumerate(self.cuckoo_hash_table1):
            if item is not None:
                output += f"Table 1 - {i}: {item[0]}, {item[1]}\n"
        for i, item in enumerate(self.cuckoo_hash_table2):
            if item is not None:
                output += f"Table 2 - {i}: {item[0]}, {item[1]}\n"
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, output)
        self.update_last_action("Displayed Hopscotch Hashing")

    def display_hopscotch_hashing(self):
        output = "Hopscotch Hashing:\n"
        for i, item in enumerate(self.hopscotch_hash_table):
            if item is not None:
                hop_info = self.calculate_hop_information(i, self.hash1(item[0]))
                output += f"Table - {i} [Hop: {hop_info}]: {item[0]}, {item[1]}\n"
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, output)
        self.update_last_action("Displayed Cuckoo Hashing")


    def calculate_hop_information(self, current_index, original_hash):
        return abs(current_index - original_hash)
    
if __name__ == "__main__":
    app = HashTableApp()
    app.mainloop()