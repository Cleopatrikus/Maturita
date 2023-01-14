import tkinter as tk
from random import randint

c = tk.Canvas(width=600, height=600)
c.pack()

hody = []
pocty_hodov = []
c.create_line(20, 0, 20, 555)
c.create_line(20, 555, 600, 555)

for i in range(2, 13):
    c.create_text(40 + (i - 2) * 50, 570, text=str(i), tags='text')
# c.create_rectangle(30, 50, 50, 555)
# c.create_rectangle(80, 50, 100, 555)

e = input('Pocet hodov')

try:
    int(e)
except ValueError:
    print('Zly format cisla')
else:
    for i in range(int(e)):
        hody.append(randint(1, 6) + randint(1, 6))
    print(hody)

mozne_hody = [i for i in range(2, 13)]
for i in mozne_hody:
    pocty_hodov.append(hody.count(i))

for i, j in enumerate(pocty_hodov):
    print(i + 2, j)
    if j != 0:
        c.create_rectangle(30 + (50 * i), 555 - (j * 45), 50 + 50 * i, 555)
tk.mainloop()
