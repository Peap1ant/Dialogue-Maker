# ------ import module ------

import tkinter
import tkinter.font
import os
import sys


# ------ main code -------

# Window
win = tkinter.Tk()

# Title
win.title('Dialogue Maker')

# Resolution
win.geometry('600x400+0+0')
win.resizable(False, False)

# Font
font = tkinter.font.Font(family="Arial", size=10)

# Title
title_text = tkinter.Label(win, text='Dialogue Maker')
title_text.pack(side='top')

# Maker
maker = tkinter.Label(win, text='by Peaplant')
maker.place(x=500, y=30)

# File path
if getattr(sys, "frozen", False):
    path = os.path.dirname(sys.executable)
else:
    path = sys.path[0]


# ------ Main Code ------

'''
# Copy-paste for easy making!

# Label & entry

_label = tkinter.Label(win, text='')

_entry = tkinter.Entry(win, width=20)

# Label & dropbox

_label = tkinter.Label(win, text = '')

 = tkinter.StringVar()

.set(_options[0])
_drop = tkinter.OptionMenu(win, , *_options)

'''

# Header
header_label = tkinter.Label(win, text='Header : ')

header_entry = tkinter.Entry(win, width=20)

# Options
with open(f"{path}/action options.txt", "r") as file:
    action_options = file.read().split(", ")

with open(f"{path}/npc options.txt", "r") as file:
    npc_options = file.read().split(", ")

# Actions
action_label = tkinter.Label(win, text='Action :')

action = tkinter.StringVar()

action.set(action_options[0])
action_drop = tkinter.OptionMenu(win, action, *action_options)

# Select NPC

npc_label = tkinter.Label(win, text='NPC : ')

npc = tkinter.StringVar()

npc.set(npc_options[0])
npc_drop = tkinter.OptionMenu(win, npc, *npc_options)

# Message

message_label = tkinter.Label(win, text='Message : ')

message_entry = tkinter.Entry(win, width=60)


# ------ Commands ------

class Commands ():

    def __init__(self):

        # For "Saved!" message
        self.use_count = 0

        # For Code
        self.code = ''
        self.code_list = []

        # Actions list
        self.action_list = []

        # Actions num
        self.action_num = 0

        # Lines
        self.lines = 1

        # Said
        self.say = 0

        # Errors
        self.say_error = tkinter.Label(
            win, text='!Error! : you can`t add two say in one line')
        self.say_error_count = 0

        self.len_over_90 = tkinter.Label(
            win, text='!Error! : message is too long!, reduce until 90 characters')
        self.len_over_90_count = 0

    # For
    def add_new_action(self):
        self.action = action.get()
        self.npc = npc.get()
        self.message = message_entry.get()

        if self.action in ['NPC_ENTER', 'NPC_EXIT']:
            if self.action_num == 0:
                self.action_list.append(f'					"{{{self.action}:{self.npc}}} ')
                self.action_num = 1
            else:
                self.action_list.append(f'{{{self.action}:{self.npc}}} ')
        elif self.action == 'START_DIALOG_MUSIC':
            if self.action_num == 0:
                self.action_list.append('					"{START_DIALOG_MUSIC} ')
                self.action_num = 1
            else:
                self.action_list.append('{START_DIALOG_MUSIC} ')
        else:
            self.message_len = len(self.message)
            if self.message_len > 90:
                self.len_over_90.place(x=50, y=300)
                self.len_over_90_count = 1
            else:
                if self.say == 0:
                    if self.action_num == 0:
                        self.action_list.append(
                            f'					"{{{self.action}:{self.npc}}}{self.message}",\n')
                        self.action_num = 1
                    else:
                        self.action_list.append(
                            f'{{{self.action}:{self.npc}}}{self.message}",\n')
                    self.say = 1
                    if self.say_error_count == 1:
                        self.say_error_count = 0
                        self.say_error.place_forget()
                    if self.len_over_90_count == 1:
                        self.len_over_90_count = 0
                        self.len_over_90.place_forget()
                else:
                    self.say_error.place(x=50, y=300)
                    self.say_error_count = 1
                    if self.len_over_90_count == 1:
                        self.len_over_90_count = 0
                        self.len_over_90.place_forget()

    # For making code
    def making_code(self):
        if self.use_count == 1:
            self.save.place_forget()
        self.header = header_entry.get()
        self.code_list.append(
            f'					"NARRATIVE_{self.header}_{self.lines}",\n')
        self.code_list = self.code_list + self.action_list
        self.code = ''.join(self.code_list)

        self.file_name = f'{path}/Dialogue.json'

        # Make json file & Write Code
        with open(self.file_name, "w") as out_file:
            out_file.write(str(self.code))

        # Place "Saved!" message
        self.save = tkinter.Label(win, text='Saved!')
        self.save.place(x=450, y=355)

        self.use_count = 1

        # Reset all
        self.action_num = 0
        self.action_list = []
        self.say = 0

        # Add 1 lines
        self.lines = self.lines + 1


c = Commands()


# ------ Place all -------

header_label.place(x=50, y=50)
header_entry.place(x=50, y=70)
action_label.place(x=50, y=100)
action_drop.place(x=50, y=130)
npc_label.place(x=220, y=100)
npc_drop.place(x=220, y=130)
message_label.place(x=50, y=200)
message_entry.place(x=50, y=235)


# ------ Button ------

# Button for add action
make_file_btn = tkinter.Button(text="add action", width=10)
make_file_btn.config(command=c.add_new_action)
make_file_btn.place(x=500, y=320)

# Button for make json file
make_file_btn = tkinter.Button(text="make file", width=10)
make_file_btn.config(command=c.making_code)
make_file_btn.place(x=500, y=350)


# ------ Open Window ------

win.mainloop()
