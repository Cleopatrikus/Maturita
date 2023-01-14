import tkinter as tk
with open('spokojnost.txt', 'r') as file:
    lines = [i.strip() for i in file.readlines()]
    
ano = lines.count('áno')
nie = lines.count('nie')
print(f'Pocet hlasujucich je {len(lines)}')

c = tk.Canvas(width=600, height=600)
c.pack()


