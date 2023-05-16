import tkinter as tk
from tkinter import filedialog
from datetime import date

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Daily agenda")

        # Create a text widget
        self.text = tk.Text(master)
        self.text.pack(fill=tk.BOTH, expand=1)

        # Create a menu
        self.menu = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        master.config(menu=self.menu)

        # Display the date and serial number
        self.display_date()

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))

    def display_date(self):
        today = date.today()
        date_label = tk.Label(self.master, text=today.strftime("Today's date: %B %d, %Y"))
        date_label.pack(side=tk.LEFT)

root = tk.Tk()
app = TextEditor(root)
root.mainloop()