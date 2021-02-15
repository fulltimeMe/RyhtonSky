from tkinter import *
from tkinter.ttk import *
import time
import json
import sys
import os

version = '.ALPHA 1.0'

j_file = json.load(open('help.json'))
j_data = j_file['help']

lines = open('help.json', 'r').readlines()

root = Tk()
root.title(f'RythonSky v{version} -- settings')
root.geometry('450x250')
root.resizable(0, 0)
root.iconphoto(True, PhotoImage(file='icon/RythonSky_settings.png'))
m = Menu(root)
root.config(menu=m)

def edit():
    selected_line_i = l1.curselection()
    selected_line = l1.get(selected_line_i)
    top_lvl = Toplevel(root)
    top_lvl.title('Edit')

    def ok():
        global lines
        text = e1.get()
        file_data = ''.join(lines).replace(selected_line, text)
        top_lvl.destroy()

        open('help.json', 'w').write(file_data)

        lines = open('help.json', 'r').readlines()

        l1.delete(0, END)

        data_list()

    e1 = Entry(top_lvl, width=40)
    e1.grid(row=0,column=0)
    e1.insert(END, selected_line)

    Button(top_lvl, text='OK', command=ok).grid(row=0,column=1)

def new_line():
    top_lvl = Toplevel(root)
    top_lvl.title('New Line')

    def ok2():
        global lines
        text = e1.get()
        file_data = ''.join(lines) + '\n' + text
        top_lvl.destroy()

        open('help.json', 'w').write(file_data)

        lines = open('help.json', 'r').readlines()

        l1.delete(0, END)

        data_list()

    e1 = Entry(top_lvl, width=40)
    e1.grid(row=0,column=0)

    Button(top_lvl, text='OK', command=ok2).grid(row=0,column=1)

def deleat():
    selected_line_i = l1.curselection()
    selected_line = l1.get(selected_line_i)
    top_lvl = Toplevel(root)
    top_lvl.title('Del Line') 

    def ok3():
        global lines
        text = ''
        file_data = ''.join(lines).replace(selected_line, text)
        top_lvl.destroy()

        open('help.json', 'w').write(file_data)

        lines = open('help.json', 'r').readlines()

        l1.delete(0, END)

        data_list()

    Button(top_lvl, text='OK', command=ok3).grid(row=0,column=1)

menu = Menu(m)
menu2 = Menu(m)
m.add_cascade(label="Selection", menu=menu)
m.add_cascade(label="New", menu=menu2)
menu.add_command(label='Edit', command=edit)
menu.add_command(label='Del', command=deleat)
menu2.add_command(label='Line', command=new_line)

scrollbar_r = Scrollbar(root, orient="vertical")
l1 = Listbox(root, width=60, height=14, yscrollcommand=scrollbar_r.set, font=('Arial', 10))
l1.grid(row=0,column=1)
scrollbar_r.config(command=l1.yview)
scrollbar_r.grid(row=0,column=0)

def data_list():
    for item in lines:
        l1.insert(END, item)

data_list()

root.mainloop()