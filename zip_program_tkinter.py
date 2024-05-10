import os
import zipfile
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import messagebox as mb
 
def create_zip(directory_to_zip : str, zip_file_name : str):
    shutil.make_archive(zip_file_name, 'zip', directory_to_zip)
    mb.showinfo("Success", "Archive file created successfully.")
    mb.askyesno(title="Вопрос",
                         message="Show file?")
    if mb.askyesno:
       os.system("C:\Windows\explorer.exe")
    else:
       pass
    
               
def extract_zip(directory_to_zip : str):
    if shutil.unpack_archive(directory_to_zip):
        mb.showinfo("Success", "Archive file unpacked successfully.")  
    else:
        mb.showerror("Error", "Archive file unpacking failed.")
   
def button_pressed():
    print("Button pressed")
  
def main():
    #parent window
    main_window = Tk()
    main_window.title("Zip packer && extractor")
    main_window.call('tk' , 'scaling' , 1.5)
    main_window.geometry("500x350")
    #main functionality
    button_createZip = Button(main_window, text="Create ZIP", command=create_zip)
    button_createZip.pack()
    button_createZip.place(x = 20 , y = 240 , width = 100 , height = 30)
    #buttons
    button_extractZip = Button(main_window , text = "Extract zip" , command = extract_zip)
    button_extractZip.pack()
    button_extractZip.place(x = 20 , y = 300 , width = 100 , height = 30)
    #filepath(dialogs)
    #button_createZip.bind("<Button-1>", lambda event: button_pressed())
    if button_createZip:
       filepath = filedialog.askdirectory(title="Select Directory to Pack")
       create_zip(filepath , "test")
    if button_extractZip:
       filepath = filedialog.askdirectory(title="Select Directory to Extract")
       extract_zip(filepath)
    
    # print("Selected file: ", filepath)

#main window
if __name__ == "__main__":
    main()
    mainloop()
