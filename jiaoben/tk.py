import tkinter
import turtle
root = tkinter.Tk()
label = tkinter.Label(root, text = '你好')
label.pack()
button1 = tkinter.Button(root, text = '五角星')
button1.pack()
def wjx(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
button1.bind('<Button-1>',wjx)
menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff = 0)
submenu.add_command(label = 'open')
submenu.add_command(label = 'Save')
menu.add_cascade(label = 'file', menu = submenu)
submenu1 = tkinter.Menu(menu, tearoff = 0)
submenu1.add_command(label = 'ou')
menu.add_cascade(label = 'edite', menu = submenu1)
root.config(menu = menu)
root.mainloop()
