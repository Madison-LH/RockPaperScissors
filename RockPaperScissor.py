rom tkinter import *
import random

choices = ['rock', 'paper', 'scissors']


def decidewinner():
    user = choices[var.get()]
    computer = random.choice(choices)
    result_string = ''
    if user == computer:
        result_string = 'Tie'
    else:
        if user == 'paper' and computer == 'rock':
            result_string = 'User won'
        if user == 'rock' and computer == 'scissors':
            result_string = 'User won'
        if user == 'scissors' and computer == 'paper':
            result_string = 'User won'

        if user == 'rock' and computer == 'paper':
            result_string = 'Computer won'
        if user == 'scissors' and computer == 'rock':
            result_string = 'Computer won'
        if user == 'paper' and computer == 'scissors':
            result_string = 'Computer won'

    user_choice.config(text='User choice:' + user.upper())
    computer_choice.config(text='Computer choice:' + computer.upper())
    result.config(text='Result:' + result_string.upper(), fg='Green')


root = Tk()
root.title("Rock,Paper,Scissors")
var = IntVar()

r1 = Radiobutton(root, text="Rock", variable=var, value=0, command=decidewinner)
r1.pack(anchor=W)
r2 = Radiobutton(root, text="Paper", variable=var, value=1, command=decidewinner)
r2.pack(anchor=W)
r3 = Radiobutton(root, text="Scissors", variable=var, value=2, command=decidewinner)
r3.pack(anchor=W)

user_choice = Label(root)
user_choice.pack(anchor=W)
computer_choice = Label(root)
computer_choice.pack(anchor=W)
result = Label(root)
result.pack(anchor=W)

root.geometry('300x150')
root.resizable(False, False)
root.mainloop()
