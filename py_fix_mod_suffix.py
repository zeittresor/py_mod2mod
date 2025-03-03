import os
import tkinter as tk
from tkinter import filedialog

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    label_var.set(f"Selected Folder:\n{folder_path}")

def rename_files():
    if not folder_path:
        label_var.set("Please select a folder first.")
        return

    renamed_count = 0
    for filename in os.listdir(folder_path):
        if filename.startswith("mod."):
            old_path = os.path.join(folder_path, filename)
            new_name = filename[4:] + ".mod"
            new_path = os.path.join(folder_path, new_name)
            try:
                os.rename(old_path, new_path)
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming {old_path} --> {new_path}\n{e}")

    label_var.set(f"Rename completed. {renamed_count} file(s) changed.")

root = tk.Tk()
root.title("Fix Protracker mod suffix")

folder_path = ""
label_var = tk.StringVar()
label_var.set("No folder selected yet.")

select_button = tk.Button(root, text="Select mod2mod folder", command=select_folder)
select_button.pack(pady=10)

change_button = tk.Button(root, text="Change", command=rename_files)
change_button.pack(pady=10)

status_label = tk.Label(root, textvariable=label_var, wraplength=300)
status_label.pack(pady=10)

root.mainloop()
