from tkinter import *
import time

# from tkinter import ttk

root = Tk()

root.title('Название')
root.iconbitmap('favicon.ico')
root.geometry('400x400+2000+400')
root.resizable(True, False)
root.config(bg='#5aa')

# root['bg'] = '#5aa'


# button counter
clicks = 0


def clicked():
    global clicks
    clicks += 1
    root.title(f'Counter: {clicks}')


btn1 = Button(root, text='Счетчик', command=clicked, width=10, font=('Arial', 16, 'bold'))
# btn1.config(width=10, height=6)
btn1.pack()


# button time
def check_time():
    label_time['text'] = time.strftime('%H:%M:%S')


label_time = Label(root, text='?', width=10, bg='#499', fg='#ccc')
label_time.pack()

btn2 = Button(root, text='Узнать время', command=check_time, width=10)
btn2.pack()

# img
img = PhotoImage(file='1.png')
print(img)
l_img = Label(root, image=img, width=100, height=100)
l_img.pack()


# input
def add_str():
    e.insert(END, ' Add')


def del_str():
    e.delete(0, END)


def get_str():
    l_entry_output['text'] = e.get()


l_entry = Label(root, text='Поле ввода')
l_entry.pack()

e = Entry(root)
e.insert(0, 'Hello')
e.insert(END, ', Brother')
e.pack()

l_entry_output = Label(root)
l_entry_output.pack(fill=X)

Button(root, text='Вставить строку в конец', command=add_str).pack()

Button(root, text='очистить поле ввода', command=del_str).pack()

Button(root, text='вывести в лейбл', command=get_str).pack()


root.mainloop()
