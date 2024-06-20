import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
def new_window():
    window = tk.Tk()
    window.title("Password Protected Notepad")
    window.geometry("1100x700")
    window.configure(background="pink")
    window.resizable(False, False)
    
    submit_input_text = Text(window, height=41, width=132,)
    submit_input_text.place(x=20, y=25)
    
    scrollbar = Scrollbar(window, orient=VERTICAL, command=submit_input_text.yview)
    scrollbar.place(x=1080, y=25, height=660)
    
    tk.Label(window, fg="White", bg="pink", text="Enter your Sentence:").pack()

    def save_input():
        entered_input = submit_input_text.get("1.0", "end-1c")
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        
        if file_path:
         with open(file_path, "wb") as file:
            file.write(entered_input.encode("utf-8"))
            file.flush()
            print("Document saved")
            file.close()
                
    submit_input_button = tk.Button(window, text="Submit", command=save_input)
    submit_input_button.place(x=445, y=0)
    
    def clear_text():
        submit_input_text.delete('1.0', 'end-1c')
        
    clear_button = tk.Button(window, text="Clear", command=clear_text)
    clear_button.place(x=610, y=0)

    return window
window = tk.Tk()
window.title("Password Notepad")
window.geometry("250x250")
window.configure(background="black")
window.resizable(False, False)
Password = StringVar()
password_entry = Entry(window, textvariable=Password).place(x=65,y=100)
tk.Label(window, fg="White",bg="Black", text="Enter your password:").place(x=70,y=70)

def submit_password():
        entered_password = Password.get()
        if entered_password == "Blank":
            print("correct")
            window.destroy()
            return new_window()

        else:
            print("incorrect")
                   
submit_button = tk.Button(window, text="Submit", command=submit_password)
submit_button.place(x=100, y=125)

window.mainloop()