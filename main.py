from tkinter import *

root = Tk()
root.title("Показания электросчетчика")
root.geometry("700x350")

d = {}


def button1_click():
    d.update({entry1.get(): entry2.get()})

def button2_click():
    print(d.items())


label1 = Label(root, text="Введите дату снятия показаний в формате: 01.01.2000")
label1.place(relx=0.09, rely=0.08)

label1 = Label(root, text="Введите показания счетчика в формате: 123.7")
label1.place(relx=0.6, rely=0.08)

entry1 = Entry(root)
entry1.place(relheight=0.07, relwidth=0.2, relx=0.2, rely=0.2)

entry2 = Entry(root)
entry2.place(relheight=0.07, relwidth=0.2, relx=0.7, rely=0.2)

button1 = Button(root, text="Добавить запись", command=button1_click)
button1.place(relheight=0.07, relwidth=0.2, relx=0.45, rely=0.3)

button2 = Button(root, text="Посмотреть историю записей", command=button2_click)
button2.place(relheight=0.07, relwidth=0.25, relx=0.43, rely=0.4)

root.mainloop()
