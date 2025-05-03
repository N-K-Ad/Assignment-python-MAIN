#bones quiz
from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

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

#frame
main_frame= ctk.CTkScrollableFrame(master=learn_window,height=720, width=1980 )
main_frame.place(relx=0.5, rely= 0.5, anchor='center')
main_frame.pack_propagate(False)  #prevent the frame from resizing to fit its contents
main_frame.config(bg='#5c5c5c')

second_frame= ctk.CTkScrollableFrame(master=Quiz_menu_window,height=720, width=1980 )
second_frame.place(relx=0.5, rely= 0.5, anchor='center')

#Variables
score=0

currentq=0

quiz_data = [
    {
        'question': 'What is the longest bone in the human body?',
        'options': ['Femur', 'Tibia', 'Fibula', 'Humerus'],
        'answer': 'Femur'
    },

    {
        'question': 'How many bones are in the adult human body?',
        'options': ['206', '208', '210', '212'],
        'answer': '206'

    },
    {
        'question': 'What bone protects the brain?',
        'options': ['Skull', 'Mandible', 'Maxilla', 'Frontal bone'],
        'answer': 'Skull'
    },

    {
        'question': 'Which bone is known as the collarbone?',
        'options': ['Clavicle', 'Scapula', 'Sternum', 'Humerus'],
        'answer': 'Clavicle'
    },

    {
        'question': 'What is the smallest bone in the human body?',
        'options': ['Stapes', 'Incus', 'Malleus', 'Cochlea'],
        'answer': 'Stapes' 
    },
    {
        "question": 'How many vertebrae are in the human spine?',
        "options": ['24', '26', '30', '32'],
        "answer": '24'
    },
    {
        "question": "what is the function of the ribcage?",
        "options": ['Protects the heart and lungs', 'Supports the head', 'Allows for movement', 'Stores calcium'],
        "answer": 'Protects the heart and lungs'
    },
    {
        "question": "Babies born with more bones than adults?",
        "options": ['True', 'False'],
        "answer": 'True'
    },
    {
        "question": "What is the name of the bone in the upper arm?",
        "options": ['Humerus', 'Radius', 'Ulna', 'Scapula'],
        "answer": 'Humerus'
    },
    {
        "question": "What is the name of the bone in the thigh?",
        "options": ['Femur', 'Tibia', 'Fibula', 'Patella'],
        "answer": 'Femur'
    },


]

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
        feedback.config(text='Quiz completed! Your score is: {}/{}'.format(score, len(quiz_data)), fg='blue') #maybe try wrapping since its in a customtkinter frame
        for button in button_choices:
            button.config(state='disabled')
        next.config(state='disabled')
def show_question():
    question = quiz_data[currentq]
    question_label.config(text=question['question'])

    choices = question['options']
    for i in range(4):
        button_choices[i].config(text=choices[i], state='normal')
    feedback.config(text='', state='disabled')  
    next.config(state='disabled')


main_window.protocol('WM_DELETE_WINDOW', closeall) #WM_DELETE_WINDOW is the X button on the window  
learn_window.protocol("WM_DELETE_WINDOW", closeall)
Quiz_menu_window.protocol('WM_DELETE_WINDOW', closeall) #protocol activates a function based on the window behavior

#Labels
Title_label=Label(main_window, text= 'Bones Quiz', font=('Impact', 40), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
Title_label.pack()

'''message_label= Label(main_window, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
message_label.place(anchor=CENTER, relx=0.5, rely=0.5)'''

question_label=Label(second_frame, anchor=CENTER, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, wraplength=500)
question_label.pack(pady=20)

feedback= Label(second_frame, anchor=CENTER, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)

score_label=Label(second_frame, anchor=CENTER, text='score: 0/{}'.format(len(quiz_data)), font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20)
#Buttons
#Main menu window buttons
Learn_button=Button(main_window, text='Learn', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= learn_button_clicked)
Learn_button.pack(pady=20)

quit_button= Button(main_window, text='Quit', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit)
quit_button.pack(pady=20) #quit button

Quiz_menu_button=Button(main_window, text='Quiz menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quiz_menu_button_clicked)
Quiz_menu_button.pack(pady=20)

#learn window buttons
Main_button= Button(learn_window,anchor= NW, text='Main Menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked, width=30, height=30)
Main_button.config(image=hometk)
Main_button.place(y=10, x=10)

quit_button= Button(learn_window, anchor= NW, text='Quit', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit, width=30, height=30)
quit_button.config(image=quittk)
quit_button.place(y=10, x=70,) #quit button

#Quiz menu window buttons
Learn_button=Button(Quiz_menu_window,anchor= NW, text='Learn', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=10, pady=10, command= learn_button_clicked, width=30, height=30)
Learn_button.config(image=learntk)
Learn_button.place(y=10, x=70)

Main_button= Button(Quiz_menu_window,anchor= NW, text='Main Menu', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= back_button_clicked, width=30, height=30)
Main_button.config(image=hometk)
Main_button.place(y=10, x=10)

quit_button= Button(Quiz_menu_window, anchor= NW, text='Quit', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command= quit, width=30, height=30)
quit_button.config(image=quittk)
quit_button.place(y=10, x=130,) #quit button

button_choices = []
for i in range(4):
    button = Button(second_frame, text='', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, command=lambda i=i: check_answer(i))
    button.pack(pady=10)
    button_choices.append(button)

next = Button(second_frame, text='Next', font=('Comic sans', 20), bg='gray', fg='black', bd=10, relief=RAISED, padx=20, pady=20, state='disabled', command=lambda: next_question())
next.pack(pady=20)

show_question()

import sys
print(len(locals()))

print(len(globals()))
print(sys.getsizeof(locals()))
print(sys.getsizeof(globals()))
mainloop()

'''PLAN
Difficulty levels will be based on the number of questions and number of mistakes tolerated
EASY: 5 questions, inf mistakes
MEDIUM: 10 questions, 3 mistakes
HARD: 15 questions, 5 mistakes

Scroll wheel will be for learn page and maybe quizs
current errors including, window closing does not allow for the code to run again and windows not showing   
'''