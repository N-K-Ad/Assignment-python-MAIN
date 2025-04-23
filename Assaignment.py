#bones quiz
from tkinter import *

#Overall GUI
window=Tk()  #initiate an instance of a window
window.title('Bones quiz')
window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
window.iconphoto(True,icon)
window.config(bg='gray')

#Functions
def learn_button_clicked():
    message_label.config(text='Learn button clicked')

#Labels
Title_label=Label(window, text= 'Bones Quiz', font=('Impact', 40), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
Title_label.pack()
message_label= Label(window, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
message_label.place(anchor=CENTER, relx=0.5, rely=0.5)

#Buttons
Learn_button=Button(window, text='Learn', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= learn_button_clicked)
Learn_button.pack(pady=20)

#Variables

mainloop()
