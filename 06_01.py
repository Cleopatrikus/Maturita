import tkinter as tk
from random import choice

c = tk.Canvas(width=600, height=400)
c.pack()
text = '5'
odpoved = False
c.create_text(300, 200, font='Arial 50', text=text, tags='time')

kabel = choice(('zlty', 'modry', 'cerveny', 'zeleny'))
print(kabel)


def casovac():
    global text, odpoved
    if text != '0':
        c.itemconfig('time', text=text)
    elif text == '0':
        text = c.itemconfig('time', text='Bomba vybuchla')
        odpoved = True

    if not odpoved:
        text = str(int(text) - 1)
        c.after(1000, casovac)


def zlty():
    global text, odpoved
    if kabel == 'zlty' and text != 'Bomba vybuchla':
        text = 'Spravne'
    elif kabel != 'zlty' and text != 'Spravne':
        text = 'Bomba vybuchla'
    odpoved = True
    casovac()


def modry():
    global text, odpoved
    if kabel == 'modry' and text != 'Bomba vybuchla':
        text = 'Spravne'
    elif kabel != 'modry' and text != 'Spravne':
        text = 'Bomba vybuchla'
    odpoved = True
    casovac()


def cerveny():
    global text, odpoved
    if kabel == 'cerveny' and text != 'Bomba vybuchla':
        text = 'Spravne'
    elif kabel != 'cerveny' and text != 'Spravne':
        text = 'Bomba vybuchla'
    odpoved = True
    casovac()


def zeleny():
    global text, odpoved
    if kabel == 'zeleny' and text != 'Bomba vybuchla':
        text = 'Spravne'
    elif kabel != 'zeleny' and text != 'Spravne':
        text = 'Bomba vybuchla'
    odpoved = True
    casovac()


def restart():
    global text, odpoved, kabel
    text = '60'
    odpoved = False
    kabel = choice(('zlty', 'modry', 'cerveny', 'zeleny'))
    print(kabel)
    casovac()


b1 = tk.Button(text='Zlty', command=zlty)
b1.pack()
b2 = tk.Button(text='Modry', command=modry)
b2.pack()
b3 = tk.Button(text='Cerveny', command=cerveny)
b3.pack()
b4 = tk.Button(text='Zeleny', command=zeleny)
b4.pack()
b5 = tk.Button(text='Restart', command=restart)
b5.pack()


casovac()


tk.mainloop()
