import tkinter as tk

c = tk.Canvas(width=600, height=600)
c.pack()

c.create_text(30,20, text = '0', tags = 'vys', anchor = 'w')
prem = []
znak = 0
tmp = []
for i in range(10):
    c.create_rectangle((i*50),50,((i+1)*50),100)
    c.create_text(25+(i*50),75, text = str(i))

c.create_rectangle(0, 100, 50, 150)
c.create_text(25,125,text='C')
c.create_rectangle(50,100,100,150)
c.create_text(75,125,text='+')
c.create_rectangle(100,100,150,150)
c.create_text(125,125,text='-')
c.create_rectangle(150,100,200,150)
c.create_text(175,125,text='=')

def M1(event):
    global prem, znak, str_prem, znak, tmp
    x, y = event.x, event.y
    
    if 50 <= y < 100:
        if x <= 500:
            prem.append(x // 50)
            str_prem = ''.join([str(x) for x in prem])
            c.itemconfig('vys', text = str_prem)
            
    if 100 <= y <= 150:
        if 0 <= x < 50:
            
            c.itemconfig('vys', text = '0')
            prem.clear()
            str_prem = ''
            tmp.clear()
            
        elif 50 <= x < 100:
            znak = 0
            
            tmp.append(int(str_prem))
            
            #tmp = int(str_prem)
            
            #c.itemconfig('vys', text = '+')
            
            prem.clear()
            str_prem = ''
            
        elif 100 <= x < 150:
            znak = 1
            
            tmp.append(int(str_prem))
            
            #tmp = int(str_prem)
            
            #c.itemconfig('vys', text = '-')
            
            prem.clear()
            str_prem = ''
            
        elif 150 <= x <= 200:
            if znak == 0:
                c.itemconfig('vys', text = f'{int(tmp[0]) + int(str_prem)}')
                str_prem = f'{int(tmp[0]) + int(str_prem)}'
                tmp.clear()
            elif znak == 1:
                c.itemconfig('vys', text = f'{int(tmp[0]) - int(str_prem)}')
                str_prem = f'{int(tmp[0]) - int(str_prem)}'
                tmp.clear()
    #print(prem)
    
c.bind('<Button-1>', M1)

tk.mainloop()
        
