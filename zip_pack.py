import tkinter as tk
from tkinter import filedialog
import zipfile
import os

class FileZipperApp:
    def __init__(self, master):
        self.master = master
        master.title("File Zipper")
        master.geometry("400x300")

        self.file_path = None
        self.zip_file_path = None

        self.choose_file_button = tk.Button(master, text="Choose File", command=self.choose_file)
        self.choose_file_button.pack(pady=10)

        self.file_path_label = tk.Label(master, text="")
        self.file_path_label.pack()

        self.create_zip_button = tk.Button(master, text="Create Zip", command=self.create_zip, state=tk.DISABLED)
        self.create_zip_button.pack(pady=5)

        self.zip_created_label = tk.Label(master, text="")
        self.zip_created_label.pack()

        self.extract_zip_button = tk.Button(master, text="Extract Zip", command=self.extract_zip, state=tk.NORMAL)
        self.extract_zip_button.pack(pady=5)
        
        #self.extract_zip_button_2 = tk.Button(master, text="Extract Zip", command=self.extract_zip_file)
       # self.extract_zip_button.pack(pady = 0)
       # self.extract_zip_button_2.pack()
        
        

        self.extraction_label = tk.Label(master, text="")
        self.extraction_label.pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.file_path_label.config(text="Chosen file: " + self.file_path)
            self.create_zip_button.config(state=tk.NORMAL)

    def create_zip(self):
        if self.file_path:
            zip_file_path = self.file_path + ".zip"
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                zipf.write(self.file_path, os.path.basename(self.file_path))
            self.zip_file_path = zip_file_path
            self.zip_created_label.config(text="Zip file created: " + self.zip_file_path)
            self.extract_zip_button.config(state=tk.NORMAL)

    def extract_zip(self):
        if self.zip_file_path:
            extract_dir = filedialog.askdirectory()
            if extract_dir:
                with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)
                self.extraction_label.config(text="Zip file extracted to: " + extract_dir)
                
def main():
    root = tk.Tk()
    app = FileZipperApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
