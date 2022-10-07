# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import random

ALL_COFFEES = [
    'Espresso','Americano','Colombia','Veranda','Lungo',
    'Latte','Latte Macchiatto','Cappuccino'
]

BLACK_COFFEES = ALL_COFFEES[:5]
WHITE_COFFEES = ALL_COFFEES[5:]

root = tk.Tk()
root.geometry('1024x768')

vars = [tk.IntVar() for _ in range(len(ALL_COFFEES))]

def draw():
    cafelist = []
    for i, _ in enumerate(cb):
        if vars[i].get():
            cafelist.append(ALL_COFFEES[i])
    if len(cafelist):
        lb2['text'] = cafelist[random.randint(0,len(cafelist)-1)]
    else:
        lb2['text'] ='请至少勾选1项！'

def draw_black():
    lb2['text'] = BLACK_COFFEES[random.randint(0,len(BLACK_COFFEES)-1)]

def draw_white():
    lb2['text'] = WHITE_COFFEES[random.randint(0,len(WHITE_COFFEES)-1)]

btn1 = tk.Button(root, command=draw)
btn1['text'] = '抽签'
btn1['font'] = ('Microsoft YaHei', 24)
btn1.place(relx=0.1, rely=0.35, anchor='nw', relwidth=0.35, relheight=0.15)

btn2 = tk.Button(root, command=draw_black)
btn2['text'] = '快速抽取黑咖'
btn2['font'] = ('Microsoft YaHei', 24)
btn2.place(relx=0.1, rely=0.55, anchor='nw', relwidth=0.35, relheight=0.15)

btn3 = tk.Button(root, command=draw_white)
btn3['text'] = '快速抽取花式咖啡'
btn3['font'] = ('Microsoft YaHei', 24)
btn3.place(relx=0.1, rely=0.75, anchor='nw', relwidth=0.35, relheight=0.15)

lb1 = tk.Label(root)
lb1['text'] = '咖啡胶囊抽取程序\nv0.1.0'
lb1['font'] = ('Microsoft YaHei', 24)
lb1.place(relx=0.1, rely=0.1, anchor='nw', relwidth=0.35, relheight=0.2)

lb2 = tk.Label(root)
lb2['font'] = ('Microsoft YaHei', 24)
lb2['relief'] = tk.RIDGE
lb2.place(relx=0.55, rely=0.1, anchor='nw', relwidth=0.35, relheight=0.35)

lb3 = tk.Label(root)
lb3['text'] = '在此选择要抽签的咖啡胶囊种类'
lb3['font'] = ('Microsoft YaHei', 18)
lb3.place(relx=0.55, rely=0.5, anchor='nw', relwidth=0.35, relheight=0.1)

cb = [tk.Checkbutton(root, variable=vars[i], onvalue=1, offvalue=0, font=('Microsoft YaHei', 12), anchor='w', justify='left') for i in range(len(vars))]
for i, c in enumerate(cb):
    c['text'] = ALL_COFFEES[i]

for i, c in enumerate(cb[:5]):
    c.place(relx=0.55, rely=0.6+i*0.05, anchor='nw', relwidth=0.15, relheight=0.05)

for i, c in enumerate(cb[5:]):
    c.place(relx=0.75, rely=0.6+i*0.05, anchor='nw', relwidth=0.15, relheight=0.05)

root.mainloop()
