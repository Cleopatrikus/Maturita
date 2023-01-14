import tkinter as tk

c = tk.Canvas(width=400, height=300, bg='white')
c.pack()
for i in range(5):
    c.create_line(0, 10+(i*10), 400, 10+(i*10))

with open('noty.txt') as f:
    line = f.readlines()[0].strip()
    for i, j in enumerate(line):
        if 10+((i+1)*10) <= 400:
            if j == 'c':
                c.create_oval(10+(i*10), 56, 10+((i+1)*10), 64)
            elif j == 'd':
                c.create_oval(10+(i*10), 51, 10+((i+1)*10), 59)
            elif j == 'e':
                c.create_oval(10+(i*10), 47, 10+((i+1)*10), 53)
            elif j == 'f':
                c.create_oval(10+(i*10), 41, 10+((i+1)*10), 49)
            elif j == 'g':
                c.create_oval(10+(i*10), 37, 10+((i+1)*10), 43)
            elif j == 'a':
                c.create_oval(10+(i*10), 31, 10+((i+1)*10), 39)
            elif j == 'h':
                c.create_oval(10+(i*10), 27, 10+((i+1)*10), 33)


tk.mainloop()
