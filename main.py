import customtkinter as tk
from tkinter import filedialog
import os


def openFile():
    fileLocation = filedialog.askdirectory()

def checkForError():
    inp_box_arr = [file_name_box, file_title_box, file_content_box]
    for item in inp_box_arr:
        if(item.get() == ""):
            item.configure(placeholder_text_color="#ff4444")
            empty = True
        else:
            item.configure(placeholder_text_color="gray")
            empty = False
    if(empty):
        return 1
    return 0


def createFile():
    if checkForError() == 1:
        return
    name = file_name_box.get()
    title = file_title_box.get()
    content = file_content_box.get()

    fp = open(f'')
    print(fileLocation)


root = tk.CTk()

tk.set_appearance_mode("dark")
root.title("Popup File Generarator - Kritagya Bhattarai")
root.geometry("410x350")

file_name_box = tk.CTkEntry(root, width=400, height=40,
placeholder_text="Enter File Name",
placeholder_text_color="gray")
file_name_box.grid(row=0, column=0, pady=5, padx=5)

file_title_box = tk.CTkEntry(root, width=400, height=40,
placeholder_text="Enter File Title",
placeholder_text_color="gray")
file_title_box.grid(row=1, column=0,padx=5, pady=5)

file_content_box = tk.CTkEntry(root, width=400, height=40,
placeholder_text="Enter Content of File Here",
placeholder_text_color="gray",
)
file_content_box.grid(row=2, column=0, pady=5,padx=5)

file_dir_box = tk.CTkButton(root, width=100, height=40,command=openFile, text="Browse")
file_dir_box.grid(row=3,column=0,pady=5,padx=0)

create = tk.CTkButton(root, width=100, height=40, command=createFile, text="Create")
create.grid(row=3,column=1, pady=5,padx=0)

root.mainloop()


