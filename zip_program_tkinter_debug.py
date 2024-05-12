import os
import zipfile
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox as mb
from zipfile import ZipFile

def create_zip(zipFileName):
   destination_directory = filedialog.askdirectory(title="Choose directory to save zip")
   if not destination_directory:
        mb.showinfo("Info","No directory selected.")
        return

    # Ask the user to choose files to include in the zip file
   filenames = filedialog.askopenfilenames(title="Choose files to include in zip")
   if not filenames:
        mb.showinfo("Info","No files selected.")
        return

    # Create the zip file in the chosen directory
   zip_name = os.path.join(destination_directory, zipFileName)
   with zipfile.ZipFile(zip_name, mode="w") as archive:
        for filename in filenames:
            arcname = os.path.relpath(filename, destination_directory)
            arcname = arcname.replace(os.path.sep, '/')  # Replace backslashes with forward slashes
            archive.write(filename, arcname=arcname)
   mb.showinfo("Info", f"Zip file '{zip_name}' created successfully.")

               
def extract_zip():
    file_name = filedialog.askopenfilename(title="Choose zip file to extract")
    
    #check if zip file is selected
    if not file_name:
       return
       
    directory = filedialog.askdirectory(title = "Choose directory to extract") 
    #check if directory is selected
    if not directory:
       return
       
    with zipfile.ZipFile(file_name, 'r') as zip_extract:
        zip_extract.extractall(directory)
        
    mb.showinfo("Success", "Zip file extracted to: " + directory)


def main():
    #parent window
    main_window = Tk()
    main_window.title("File archiver")
    main_window.call('tk' , 'scaling' , 1.5)
    main_window.geometry("500x150")
    #main functionality
    button_createZip_launch = Button(main_window, text="Create ZIP")
    button_createZip_launch.pack()
    button_createZip_launch.place(x = 20 , y = 20 , width = 100 , height = 30)
    button_createZip_launch.bind("<Button-1>", lambda event: create_zip(textbox.get(1.0, "end-1c")))
    #buttons
    button_extractZip = Button(main_window , text = "Extract zip")
    button_extractZip.pack()
    button_extractZip.place(x = 20 , y = 60 , width = 100 , height = 30)
    button_extractZip.bind("<Button-1>", lambda event: extract_zip())
    textbox = Text(main_window , width= 40 , height = 1)
    textbox.pack()
    textbox.place(x = 150 , y = 50, width = 300 , height = 30)
    #label
    labelText = Label(main_window , text = "Enter the name for zip file(*.format)")
    labelText.pack()
  

#main window
if __name__ == "__main__":
    main()
    mainloop()
