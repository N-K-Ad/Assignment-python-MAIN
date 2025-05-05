#bones quiz
from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as font
import random

#Overall GUI
#Main window
main_window=Tk()  #initiate an instance of a window
font.families()
main_window.title('Bones quiz  Main menu')
main_window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
main_window.iconphoto(True,icon)
main_window.config(bg='white')
main_window.resizable(False,False) #disables resizing of the window

#Learn window
learn_window=Toplevel()
learn_window.title('Bones quiz - Learn')
learn_window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
learn_window.iconphoto(True,icon)
learn_window.config(bg='white')
learn_window.withdraw()  #hide the learn window initially
learn_window.resizable(False,False) #disables resizing of the window

#Quiz menu window
Quiz_menu_window=Toplevel()
Quiz_menu_window.title('Bones quiz - Quiz menu')
Quiz_menu_window.geometry('1920x1080')
icon = PhotoImage(file='Logo.png')
Quiz_menu_window.iconphoto(True,icon)
Quiz_menu_window.config(bg='white')
Quiz_menu_window.withdraw()  #hide the quiz menu window initially
Quiz_menu_window.resizable(False,False) #disables resizing of the window
# Open the image using Pillow
home_image = Image.open('home.png')

# Resize the image
resize_home = home_image.resize((30, 30))

# Convert the resized image back to a PhotoImage
hometk = ImageTk.PhotoImage(resize_home)

learn_image = Image.open('learn.png')
resize_learn = learn_image.resize((30, 30))
learntk = ImageTk.PhotoImage(resize_learn)

quit_image = Image.open('quit.png')
resize_quit = quit_image.resize((30, 30))
quittk = ImageTk.PhotoImage(resize_quit)

diagram= Image.open('skeleton_diagram.png')
resize_diagram= diagram.resize((300, 300))
diagramtk= ImageTk.PhotoImage(resize_diagram)

quiz_image= Image.open('quizlogo.png')
resize_quiz= quiz_image.resize((30, 30))
quiztk= ImageTk.PhotoImage(resize_quiz)

help_image= Image.open('Help.png')
resize_help= help_image.resize((30, 30))
helptk= ImageTk.PhotoImage(resize_help)

background_image = Image.open('Background.png')
resizebg= background_image.resize((1920, 1080))
backgroundtk= ImageTk.PhotoImage(resizebg)

#frame
main_frame= ctk.CTkScrollableFrame(master=learn_window,height=720, width=1980 )
main_frame.place(relx=0.5, rely= 0.5, anchor='center')

second_frame= ctk.CTkScrollableFrame(master=Quiz_menu_window,height=920, width=1980 )
second_frame.place(relx=0.5, rely= 0.5, anchor='center')

#Variables
score=0

currentq=0

original_quiz_data = [
    {
        'question': 'What is the longest bone in the human body?',
        'options': ['Femur', 'Tibia', 'Fibula', 'Humerus'],
        'answer': 'Femur'
    },

    {
        'question': 'How many bones are in the adult human body?',
        'options': ['208','206', '210', '212'],
        'answer': '206'

    },
    {
        'question': 'What bone protects the brain?',
        'options': ['Mandible', 'Maxilla', 'Skull', 'Frontal bone'],
        'answer': 'Skull'
    },

    {
        'question': 'Which bone is known as the collarbone?',
        'options': ['Clavicle', 'Scapula', 'Sternum', 'Humerus'],
        'answer': 'Clavicle'
    },

    {
        'question': 'What is the smallest bone in the human body?',
        'options': ['Incus', 'Malleus', 'Stapes', 'Cochlea'],
        'answer': 'Stapes' 
    },
    {
        "question": 'How many vertebrae are in the human spine?',
        "options": ['26', '24', '30', '32'],
        "answer": '24'
    },
    {
        "question": "what is the function of the ribcage?",
        "options": ['Protects the heart and lungs', 'Supports the head', 'Allows for movement', 'Stores calcium'],
        "answer": 'Protects the heart and lungs'
    },
    {
        "question": "Who has the most bones at their age",
        "options": ['Teens','Adults','Babies', 'Elderly'],
        "answer": 'Babies'
    },
    {
        "question": "What is the name of the bone in the upper arm?",
        "options": ['Humerus', 'Radius', 'Ulna', 'Scapula'],
        "answer": 'Humerus'
    },
    {
        "question": "What is the name of the bone in the thigh?",
        "options": ['Tibia', 'Femur', 'Fibula', 'Patella'],
        "answer": 'Femur'
    },

]
quiz_data = original_quiz_data.copy()
random.shuffle(quiz_data) #shuffles quiz when program

#Functions
def reset_quiz():
    global score, currentq
    score = 0
    currentq = 0
    score_label.config(text='score: 0/{}'.format(len(quiz_data)))
    show_question()

   
#learn button
def help_button_clickedmain():
    messagebox.showinfo(title='help',message='This is the Main Menu! here you can navigate the app through the buttons on the screen!' \
    ' Click "Quiz" to take you to the quiz, or "Learn" to learn about the bones of the human body.' \
    ' Click "Quit" to exit the app.')

def help_button_clickedlearn():
    messagebox.showinfo(title='help',message='This is the Learn page! Learn about the bones of the Human body here in order to prepare for the quiz. ' \
    'A diagram and paragraph of information is included. You can navigate the app through the buttons on the top left.' \
    ' The home icon takes you to the main menu, the clock icon takes you to the quiz, and the X icon closes the app.')

def help_button_clickedquiz():
    messagebox.showinfo(title='help',message='This is the Quiz page! Test yourself on the bones of the Human body! ' \
    'A question is given to you which you must answer via the multiple choice options. Your score will be displayed above and you will be told if the answer was correct or not.' \
    ' Then a final score given at the end of the quiz. You can navigate the app through the buttons on the top left.' \
    'The home icon takes you to the main menu, the book takes you to the Learn page, clicking the clock restarts the quiz and the X icon closes the app.')

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
    reset_quiz()

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

def check_answer(choice):
    question = quiz_data[currentq]
    selected_option = button_choices[choice].cget('text')
    if selected_option == question['answer']:
        global score
        score +=1
        score_label.config(text='score: {}/{}'.format(score, len(quiz_data)))
        feedback.config(text='Correct!', fg='green')
    else:
        feedback.config(text='Incorrect! The correct answer is: {}'.format(question['answer']), fg='red')
    for button in button_choices:
        button.config(state='disabled')
        next.config(state='normal')  #enable the next button after answering the question
    
def next_question():
    global currentq
    currentq += 1
    if currentq < len(quiz_data):
        show_question()
    else:
        feedback.config(text='Quiz completed! Your score is: {}/{}. Navigate to the home or learn page, restart the quiz or quit via the icons on the top left :)'.format(score, len(quiz_data)), fg='blue') 
        for button in button_choices:
            button.config(state='disabled')
        next.config(state='disabled')
def show_question():
    question = quiz_data[currentq]
    question_label.config(text=question['question'])

    choices = question['options']
    for i in range(4):
        button_choices[i].config(text=choices[i], state='normal')
    feedback.config(text='')  
    next.config(state='disabled')


main_window.protocol('WM_DELETE_WINDOW', closeall) #WM_DELETE_WINDOW is the X button on the window  
learn_window.protocol("WM_DELETE_WINDOW", closeall)
Quiz_menu_window.protocol('WM_DELETE_WINDOW', closeall) #protocol activates a function based on the window behavior

#Labels
Background = Label(main_window, image=backgroundtk)
Background.place(relwidth=1, relheight=1)
Background = Label(learn_window, image=backgroundtk)
Background.place(relwidth=1, relheight=1)
Background = Label(Quiz_menu_window, image=backgroundtk)
Background.place(relwidth=1, relheight=1)

Title_label = Label(main_window, text='Bones Quiz', font=('Impact', 40), bg='yellow', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
Title_label.pack()

Title_label.lift()

'''message_label= Label(main_window, text='', font=('Comic sans', 20), bg='yellow', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
message_label.place(anchor=CENTER, relx=0.5, rely=0.5)'''

question_label=Label(second_frame, anchor=CENTER, text='', font=('Times New Roman', 20), bg='yellow', fg='black', bd=10, relief=RAISED, padx=20, pady=20, wraplength=500)
question_label.pack(pady=20)

feedback= Label(second_frame, anchor=CENTER, text='', font=('Times New Roman', 20), bg='yellow', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
feedback.pack(pady=20)

score_label=Label(second_frame, anchor=CENTER, text='score: 0/{}'.format(len(quiz_data)), font=('Times New Roman', 20), bg='yellow', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
score_label.pack(pady=20)

info = Label(main_frame, text='In adult humans, the body contains 206 bones. Infants have a higher count which later fuses together in the course of growing up. ' \
'Femur, also called thigh bone, is the longest bone in the body while stapes, located in the middle ear, is the smallest. ' \
'Skull is the bone enclosing the brain and as a vital organ it needs additional protection. Ribs are also bones that, in addition to being skeletal in nature,' \
' encase and guard other core muscles such as heart and lungs. Arm is joined to the torso by a bone referred to as collarbone or clavicle . ' \
'Humerus is the corresponding bone in upper arm while vertebrae, collectively termed as spine, comprise 24 units that balance the figure while guarding the spinal cord.' \
' All these bones coordinate to shape the structure of the body, help in mobility, and protect vital organs.' \
,
 anchor=E,font=('Times New Roman', 20), bg='yellow', fg='black', bd=10, relief=RAISED, padx=20, pady=20, wraplength=1000)
info.pack(pady=20)

diagram = PhotoImage(file='skeleton_diagram.png')
info.config(image=diagram, compound='bottom')  # Set the image and text to be displayed together
info.image = diagram  # Keep a reference to avoid garbage collection

#Buttons
#help button
help = Button(main_window, text='help', font=('Comic sans', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=5, pady=5, command= help_button_clickedmain)
help.config(image=helptk)
help.place( y=10, x=1800)

help2 = Button(learn_window, text='help', font=('Comic sans', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=5, pady=5, command= help_button_clickedlearn)
help2.config(image=helptk)
help2.place( y=10, x=1800)

help3 = Button(Quiz_menu_window, text='help', font=('Comic sans', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=5, pady=5, command= help_button_clickedquiz)
help3.config(image=helptk)
help3.place( y=10, x=1800)
#Main menu window buttons
Learn_button=Button(main_window, text='Learn', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= learn_button_clicked)
Learn_button.pack(pady=20)

Quiz_menu_button=Button(main_window, text='Quiz', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quiz_menu_button_clicked)
Quiz_menu_button.pack(pady=20)

quit_button= Button(main_window, text='Quit', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit)
quit_button.pack(pady=20) #quit button

#learn window buttons
Main_button= Button(learn_window,anchor= NW, text='Main Menu', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked, width=30, height=30)
Main_button.config(image=hometk)
Main_button.place(y=10, x=10)

Quiz_menu_button= Button(learn_window, text='Quit', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quiz_menu_button_clicked, width=30, height=30)
Quiz_menu_button.config(image=quiztk)
Quiz_menu_button.place(y=10, x=70) #quiz button

quit_button= Button(learn_window, anchor= NW, text='Quit', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit, width=30, height=30)
quit_button.config(image=quittk)
quit_button.place(y=10, x=130,) #quit button

#Quiz menu window buttons
Learn_button=Button(Quiz_menu_window,anchor= NW, text='Learn', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=10, pady=10, command= learn_button_clicked, width=30, height=30)
Learn_button.config(image=learntk)
Learn_button.place(y=10, x=70)

Main_button= Button(Quiz_menu_window,anchor= NW, text='Main Menu', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked, width=30, height=30)
Main_button.config(image=hometk)
Main_button.place(y=10, x=10)

Quiz_menu_button= Button(Quiz_menu_window, text='Quit', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quiz_menu_button_clicked, width=30, height=30)
Quiz_menu_button.config(image=quiztk)
Quiz_menu_button.place(y=10, x=130) #quiz button

quit_button= Button(Quiz_menu_window, anchor= NW, text='Quit', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit, width=30, height=30)
quit_button.config(image=quittk)
quit_button.place(y=10, x=190,) #quit button
button_choices = []
for i in range(4):
    button = Button(second_frame, text='', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command=lambda i=i: check_answer(i))
    button.pack(pady=10)
    button_choices.append(button)

next = Button(second_frame, text='Next', font=('Gothic', 20), bg='orange', fg='black', bd=10, relief=RAISED, padx=20, pady=20, state='disabled', command=lambda: next_question())
next.pack(pady=20)

second_frame.lift()
main_frame.lift()

show_question()

import sys
print(len(locals()))

print(len(globals()))
print(sys.getsizeof(locals()))
print(sys.getsizeof(globals()))
mainloop()