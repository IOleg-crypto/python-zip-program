import tkinter as tk
from tkinter import filedialog
import zipfile
import os

def pack_directory():
    directory_path = filedialog.askdirectory(title="Select Directory to Pack")
    if directory_path:
        zip_file_name = os.path.basename(directory_path) + ".zip"
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory_path))
        print("Directory packed successfully.")

root = tk.Tk()
root.title("Zip Packer")

button = tk.Button(root, text="Select Directory", command=pack_directory)
button.pack(pady=20)

root.mainloop()
