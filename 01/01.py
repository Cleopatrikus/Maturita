import tkinter as tk

c = tk.Canvas(width=600, height=600)
c.pack()

body = [[300, 300]]
smer = 'n'
pos = 0


def had():
    global pos, smer
    if smer == 'n':
        body.append((body[pos][0], body[pos][1] - 1))
    elif smer == 'w':
        body.append((body[pos][0] - 1, body[pos][1]))
    elif smer == 'e':
        body.append((body[pos][0] + 1, body[pos][1]))
    elif smer == 's':
        body.append((body[pos][0], body[pos][1] + 1))

    c.create_line(body[pos][0], body[pos][1], body[pos + 1][0], body[pos + 1][1], )
    c.update()
    if body[pos + 1] not in body[:-1]:
        c.after(15, had)
    pos += 1
    print(body)

def up(event):
    global smer
    smer = 'n'


def left(event):
    global smer
    smer = 'w'


def right(event):
    global smer
    smer = 'e'


def down(event):
    global smer
    smer = 's'


def restart():
    global body, pos, smer
    body = [(300, 300)]
    pos = 0
    smer = 'n'
    c.delete('all')
    had()


button = tk.Button(text='Restart', command=restart)
button.pack()

c.bind_all('<Up>', up)
c.bind_all('<Left>', left)
c.bind_all('<Right>', right)
c.bind_all('<Down>', down)

had()

tk.mainloop()
