from tkinter import *
from tkinter import ttk, filedialog, messagebox

def cal():
    try:
        num1 = float(kal1.get())
        num2 = float(kal2.get())
        operacia = op.get()
        if operacia == '+':
            result = num1 + num2
        elif operacia == '-':
            result = num1 - num2
        elif operacia == '*':
            result = num1 * num2
        elif operacia == '/':
            if num2 == 0:
                messagebox.showerror("WARNING","Ошибка при делении на 0")
            result = num1 / num2
        messagebox.showinfo("Результат", result)
    except ValueError:
        messagebox.showerror("НЕПРАВИЛЬНО!", "Калькулятор для чисел")

def check():
    box = []
    if v1.get() == 1:
        box.append("Первый вариант")
    if v2.get() == 1:
        box.append("Второй вариант")
    if v3.get() == 1:
        box.append("Третий вариант")
    if box:
        messagebox.showinfo("Выбор", "Вы выбрали: " + ", ".join(box))
    else:
        messagebox.showerror("Ошибка выбора", "Не выбрано.")

def text():
    file = filedialog.askopenfilename()
    if file != "":
        with open(file, "r", encoding="utf-8") as file1:
            text1 = file1.read()
            text_area.delete("1.0", END)
            text_area.insert(END,text1)

seed = Tk()
seed.title('Горохов Алексей Владимирович')
seed.geometry("480x360")
seed.resizable(False, False)

torr = ttk.Notebook()
torr.pack()

vklad = Frame(torr)

kal1 = ttk.Entry(vklad)
kal1.pack(anchor=E)
kal2 = ttk.Entry(vklad)
kal2.pack(anchor=E)
operat = ["+", "-", "*", "/"]
op = StringVar()
op.set(operat[0])
deystv = OptionMenu(vklad, op, *operat)
deystv.pack(anchor=E)
resultirov = Button(vklad, text="=", command=cal, width=2, bg="green", fg="black")
resultirov.pack(anchor=E)

vklad2 = Frame(torr)

v1 = IntVar()
ch1 = Checkbutton(vklad2, text="Первый", variable=v1) # создает первый чекбокс
ch1.pack(anchor=W) # размещает первый чекбокс
v2 = IntVar()
ch2 = Checkbutton(vklad2, text="Второй", variable=v2) # создает второй чекбокс
ch2.pack(anchor=CENTER) # размещает второй чекбокс
v3 = IntVar()
ch3 = Checkbutton(vklad2, text="Третий", variable=v3) # создает третий чекбокс
ch3.pack(anchor=E)
button_show = Button(vklad2, text="Показать выбор", command=check, bg="red", fg="black")
button_show.pack(pady=10)

vklad3 = Frame(torr)

button_text1=Button(vklad3, text="Загрузить", command=text, bg="red", fg="black")
text_area = Text(vklad3, wrap=WORD)
button_text1.pack()
text_area.pack()
torr.pack()
torr.add(vklad, text='Калькулятор')
torr.add(vklad2, text='Checkbox')
torr.add(vklad3, text='Текст')

seed.mainloop()
