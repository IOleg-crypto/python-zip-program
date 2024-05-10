import os
import zipfile
from tkinter import *
from tkinter import filedialog
 
def clear():
    pass

def create_zip(directory_to_zip, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for root, dirs, files in os.walk(directory_to_zip):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory_to_zip))
               
def extract_zip(zip_file_name):
    pass
    
def main():
    #parent window
    main_window = Tk()
    main_window.title("Zip packer && extractor")
    main_window.call('tk' , 'scaling' , 1.5)
    main_window.geometry("640x480")
    #main functionality
    button_createZip = Button(main_window, text="Create ZIP", command=create_zip)
    button_createZip.pack()
    button_createZip.place(x = 20 , y = 240 , width = 100 , height = 30)
    #buttons
    button_extractZip = Button(main_window , text = "Extract zip" , command = extract_zip)
    button_extractZip.pack()
    button_extractZip.place(x = 20 , y = 300 , width = 100 , height = 30)
    #textbox
    textbox = Text(main_window , height = 1 , width = 20 , font="Arial" )
    textbox.place(x = 50 , y = 120)
    textbox.pack()
    #filepath(dialogs)
    if button_createZip:
       filepath = filedialog.askdirectory(title="Select Directory to Pack")
       fileName = Label(main_window , text =  "Name : ")
       fileName.place(x = 50 , y = 120)
       create_zip(filepath , "test.zip")
    if button_extractZip:
       filepath = filedialog.askdirectory(title="Select Directory to Extract")
       fileName = Text(main_window , height = 1 , width = 20 , font="Arial" )
       fileName.place(x = 50 , y = 120)
    
    print("Selected file: ", filepath)

#main window
if __name__ == "__main__":
    main()
    mainloop()
