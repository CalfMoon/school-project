import customtkinter as tk
from tkinter import filedialog
import os


directory = os.getcwd()

def openFile():
    global directory 
    directory = filedialog.askdirectory()
    if(directory == () or directory == ""):
        directory = os.getcwd()
    file_dir_display.configure(text=directory)

def checkForEmpty():
    inp_box_arr = [file_name_box, file_title_box, file_content_box]
    for item in inp_box_arr:
        if(item.get() == ""):
            item.configure(placeholder_text_color="#ff4444")
            empty = True
        else:
            item.configure(placeholder_text_color="gray")
            empty = False
    if(empty):
        return True

def createFile():
    if checkForEmpty():
        return
    name = file_name_box.get()
    title = file_title_box.get()
    content = file_content_box.get()
    with open(os.path.join(directory, f"{name}.vbs"), "w") as f:
        f.write(f'box=msgbox("{content}",16,"{title}")')


root = tk.CTk()

tk.set_appearance_mode("dark")
root.title("Popup File Generarator - Kritagya Bhattarai")
root.geometry("410x300")

file_name_box = tk.CTkEntry(root, width=400, height=40,
placeholder_text="Enter File Name",
placeholder_text_color="gray")
file_name_box.pack(pady=5, padx=5)

file_title_box = tk.CTkEntry(root, width=400, height=40,
placeholder_text="Enter File Title",
placeholder_text_color="gray")
file_title_box.pack(padx=5, pady=5)

file_content_box = tk.CTkEntry(root, width=400, height=40,
placeholder_text="Enter Content of File Here",
placeholder_text_color="gray")
file_content_box.pack(pady=5,padx=5)

file_dir_frame = tk.CTkFrame(root)
file_dir_frame.pack(padx=5,pady=5)

file_dir_display = tk.CTkLabel(file_dir_frame, width=300, height=40, text=directory)
file_dir_display.grid(row=0,column=0)

file_dir_inp = tk.CTkButton(file_dir_frame, width=100, height=40,command=openFile, text="Browse")
file_dir_inp.grid(row=0, column=1)

create = tk.CTkButton(root, width=400, height=40, command=createFile, text="Create")
create.pack(pady=30,padx=5)

root.mainloop()