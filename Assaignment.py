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

#Quiz menu window
Quiz_menu_window=Toplevel()
Quiz_menu_window.title('Bones quiz - Quiz menu')
Quiz_menu_window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
Quiz_menu_window.iconphoto(True,icon)
Quiz_menu_window.config(bg='#5c5c5c')
Quiz_menu_window.withdraw()  #hide the quiz menu window initially

#Functions
#learn button
def learn_button_clicked():
    learn_window.deiconify()  #show the learn window
    main_window.withdraw()  #hide the main window
    Quiz_menu_window.withdraw()  #hide the quiz menu window

#quit button
def back_button_clicked():
    learn_window.withdraw() 
    main_window.deiconify()  
    Quiz_menu_window.withdraw() 

#quiz menu button
def quiz_menu_button_clicked():
    Quiz_menu_window.deiconify()  #show the quiz menu window
    learn_window.withdraw()  #hide the learn window
    main_window.withdraw()  #hide the main window

#close all windows
def closeall():
    try:
        main_window.destroy()
    except:pass
    try:
        learn_window.destroy()
    except:pass
    try:
        Quiz_menu_window.destroy()
    except:pass

#close everything when the x is clicked
main_window.protocol('WM_DELETE_WINDOW', closeall) #WM_DELETE_WINDOW is the X button on the window
learn_window.protocol("WM_DELETE_WINDOW", closeall)
Quiz_menu_window.protocol('WM_DELETE_WINDOW', closeall) #protocol activates a function based on the window behavior

#Labels
Title_label=Label(main_window, text= 'Bones Quiz', font=('Impact', 40), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
Title_label.pack()

'''message_label= Label(main_window, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
message_label.place(anchor=CENTER, relx=0.5, rely=0.5)'''

#Buttons

#Main menu window buttons
Learn_button=Button(main_window, text='Learn', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= learn_button_clicked)
Learn_button.pack(pady=20)

quit_button= Button(main_window, text='Quit', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit)
quit_button.pack(pady=20) #quit button

Quiz_menu_button=Button(main_window, text='Quiz menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quiz_menu_button_clicked)
Quiz_menu_button.pack(pady=20)

#learn window buttons
Main_button= Button(learn_window, text='Main Menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked)
Main_button.pack(pady=20)

quit_button= Button(learn_window, text='Quit', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit)
quit_button.pack(pady=20) #quit button

Quiz_menu_button=Button(learn_window, text='Quiz menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quiz_menu_button_clicked)
Quiz_menu_button.pack(pady=20)

#Quiz menu window buttons
Learn_button=Button(Quiz_menu_window, text='Learn', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= learn_button_clicked)
Learn_button.pack(pady=20)

Main_button= Button(learn_window, text='Main Menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked)
Main_button.pack(pady=20)

quit_button= Button(Quiz_menu_window, text='Quit', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit)
quit_button.pack(pady=20) #quit button

#Variables

mainloop()