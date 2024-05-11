import os
import zipfile
import tkinter as tk
#from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox as mb
 
def create_zip(directory : str, zip_name : str):
   """
    Создает zip-архив из содержимого указанной директории.
    
    :param directory: Путь к директории, которую нужно запаковать.
    :param zip_name: Имя для создаваемого zip-файла.
    """
    # Проверяем, существует ли указанная директория
   if not os.path.exists(directory):
        print(f"Директория '{directory}' не существует.")
        mb.showerror("Error", "Directory does not exist.")
        return
    
    # Создаем объект ZipFile для записи в zip-файл
   with zipfile.ZipFile(zip_name, 'w') as zipf:
        # Рекурсивно обходим все файлы и директории в указанной директории
        for root, _, files in os.walk(directory):
            for file in files:
                # Получаем абсолютный путь к текущему файлу
                file_path = os.path.join(root, file)
                # Добавляем файл в zip-архив с относительным путем
                zipf.write(file_path, os.path.relpath(file_path, directory))

   mb.showinfo("Success", "Archive file created successfully.")
    
               
def extract_zip(zip_file : str):
     """
    Распаковывает zip-архив в указанную директорию.
    
    :param zip_file: Путь к zip-файлу, который нужно распаковать.
    :param extract_to: Путь к директории, куда нужно извлечь содержимое zip-архива.
    """
    # Проверяем, существует ли указанный zip-файл
     if not os.path.exists(zip_file):
      print(f"Файл '{zip_file}' не существует.")
      return
    
    # Создаем объект ZipFile для чтения содержимого zip-файла
     with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Извлекаем все файлы и поддиректории из zip-архива
        zip_ref.extractall(zip_file)
   
def zip_press_button():
    print("Zip pressed")

def extract_press_button():
    print("Extract pressed")
def main():
    #parent window
    main_window = tk.Tk()
    main_window.title("Zip packer && extractor")
    main_window.call('tk' , 'scaling' , 1.5)
    main_window.geometry("500x150")
    #main functionality
    button_createZip = tk.Button(main_window, text="Create ZIP")
    button_createZip.pack()
    button_createZip.place(x = 20 , y = 20 , width = 100 , height = 30)
    button_createZip.bind("<Button-1>", lambda event: zip_press_button())
    #buttons
    button_extractZip = tk.Button(main_window , text = "Extract zip")
    button_extractZip.pack()
    button_extractZip.place(x = 20 , y = 60 , width = 100 , height = 30)
    button_extractZip.bind("<Button-1>", lambda event: extract_press_button())
    #filepath(dialogs)
    textbox = tk.Text(main_window , width= 40 , height = 1)
    textbox.pack()
    textbox.place(x = 150 , y = 50, width = 300 , height = 30)
    #string_text = textbox.get()
    #label
    labelText = tk.Label(main_window , text = "Enter the name for zip file")
    labelText.pack()
    labelText.place(x = 150 , y = 20 , width = 300 , height = 30)
    if zip_press_button():
       filepath = filedialog.askdirectory(title="Select Directory to Pack")
       create_zip(filepath , textbox.get(1.0,tk.END))
    if extract_press_button():
       #filepath = filedialog.askdirectory(title="Select Directory to Extract")
       fileNameExtract = filedialog.askopenfilename(title="Select File to Extract")
       extract_zip(fileNameExtract)
    
    # print("Selected file: ", filepath)

#main window
if __name__ == "__main__":
    main()
    tk.mainloop()
