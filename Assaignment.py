#bones quiz
from tkinter import *

#Overall GUI

#Main window
main_window=Tk()  #initiate an instance of a window
main_window.title('Bones quiz  Main menu')
main_window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
main_window.iconphoto(True,icon)
main_window.config(bg='#5c5c5c')

#Learn window
learn_window=Toplevel()
learn_window.title('Bones quiz - Learn')
learn_window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
learn_window.iconphoto(True,icon)
learn_window.config(bg='#5c5c5c')
learn_window.withdraw()  #hide the learn window initially

#Functions
def learn_button_clicked():
    learn_window.deiconify()  #show the learn window
    main_window.withdraw()  #hide the main window
def back_button_clicked():
    learn_window.withdraw()  #hide the learn window
    main_window.deiconify()  #show the main window

#Labels
Title_label=Label(main_window, text= 'Bones Quiz', font=('Impact', 40), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
Title_label.pack()

message_label= Label(main_window, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
message_label.place(anchor=CENTER, relx=0.5, rely=0.5)

test_label= Label(learn_window, text='Test your knowledge of the human skeleton', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
test_label.pack()

#Buttons
Learn_button=Button(main_window, text='Learn', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= learn_button_clicked)
Learn_button.pack(pady=20)
back_Learn_button= Button(learn_window, text='Back', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked)
back_Learn_button.pack(pady=20)
#Variables

mainloop()
