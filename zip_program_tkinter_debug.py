import os
import zipfile
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from tkinter.simpledialog import askstring
from zipfile import ZipFile

#compression library
import zlib
import lzma
import bz2

def create_zip(zipFileName):
   destination_directory = filedialog.askdirectory(title="Choose directory to save *.format")
   if not destination_directory:
        mb.showinfo("Info","No directory selected.")
        return

    # Ask the user to choose files to include in the zip file
   filenames = filedialog.askopenfilenames(title="Choose files to include in *.format")
   if not filenames:
        mb.showinfo("Info","No files selected.")
        return
        
   answer = sd.askstring("Input", "Choose compression type(zipfile.ZIP_DEFLATED , zipfile.ZIP_BZIP2 , zipfile.ZIP_LZMA)", parent=None)
   if not answer:
      mb.showinfo("Info", "No compression type selected.")
   if answer:
      mb.showinfo("Info", f"Compression type: {answer}")
                                
    # Create the zip file in the chosen directory
   zip_name = os.path.join(destination_directory, zipFileName)
   with zipfile.ZipFile(zip_name, mode="w" , compression=zipfile.ZIP_DEFLATED) as archive:
        for filename in filenames:
            arcname = os.path.relpath(filename, destination_directory)
            arcname = arcname.replace(os.path.sep, '/')  # Replace backslashes with forward slashes
            archive.write(filename, arcname=arcname)
   mb.showinfo("Info", f"File '{zip_name}' created successfully.")

               
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
        
    mb.showinfo("Success", "File extracted to: " + directory)


def main():
    #parent window
    main_window = Tk()
    main_window.title("File archiver")
    main_window.call('tk' , 'scaling' , 2)
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
    textbox.place(x = 150 , y = 30, width = 300 , height = 30)
    #label
    labelText = Label(main_window , text = "Enter the name for(*.format)" , font= "Arial 10")
    labelText.place(x = 150 , y = 100 , width = 500 , height = 30)
    labelText.pack()
    
    #spinbox(has compression)
    """""
    spinbox_var = StringVar()
    compresssion_levels = ["ZIP_DEFLATED" , "ZIP_BZIP2" , "ZIP_LZMA"]
    spinbox_compression = Spinbox(main_window , textvariable = spinbox_var , values = compresssion_levels , state = "readonly")
    #spinbox_compression.place()
    spinbox_compression.pack(anchor="s")
    """""
#main window
if __name__ == "__main__":
    main()
    mainloop()
