import tkinter as tk

c = tk.Canvas(width=100, height=100, bg='white')
c.pack()

c.create_text(0, 0, text='', tags='t1')

with open('kod.txt','r') as f:
    line = f.readlines()[0]
    if line[-1] == '\n':
        line = line[:-1]
    for i, j in enumerate(line):
        c.create_rectangle(10+(10*i), 10, 10+(10*i)+int(j), 90, fill='black', width=0)

    c.create_rectangle(20, 70, 80, 90, fill='white', width='0')
    c.create_text(50, 80, text=line)

tk.mainloop()
