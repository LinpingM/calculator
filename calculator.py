from tkinter import *


ACTIVEBG = '#c5c5c5'
BGROOT = '#e1e1e1'
BGNUM = '#fafafa'
BGOPER = '#f0f0f0'
FONT = 'Arial 19'
BUTTONS = (
           ('%', '√', 'x²', '¹/x'),
           ('сᴇ', 'с', '<', '±'),
           ('7', '8', '9', '×'),
           ('4', '5', '6', '-'),
           ('1', '2', '3', '+'),
           ('=', '0', '.', '÷'),
)


def is_digit(string):
    if string.isdigit():
       return True
    try:
        float(string)
        return True
    except ValueError:
        return False

def instantOperations(text):
    labelValue = label.cget('text')
    if is_digit(labelValue):
        if text == '%':
            labelValue = float(labelValue) / 100
        elif text == '√' and float(labelValue) >= 0:
            labelValue = float(labelValue) ** 0.5
        elif text == 'x²':
            labelValue = float(labelValue) ** 2
        elif text == '¹/x' and float(labelValue) != 0:
            labelValue = 1 / float(labelValue)
        elif text == 'сᴇ' or text == 'с':
            labelValue = 0
        elif text == '±':
            labelValue = -float(labelValue)
    if text == '<':
        labelValue = labelValue[:-1]
    label['text'] = str(labelValue)

def numbers(text):
    if text.isdigit():
        if label.cget('text') == '0':
            label['text'] = text
        else:
            label['text'] = label.cget("text") + text
    elif text == '.' and label.cget('text').count('.') == 0:
        label['text'] = label.cget("text") + text

def operation(text):
    print(text)


root = Tk()
root.title('Калькулятор')
root.resizable(False, False)
root['bg'] = BGROOT

# root resolution
root.width = 340
root.height = 426

# screen resolution
screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

# root's coordinates
root.x = int(screenW/2 - root.width/2)
root.y = int(screenH/2 - root.height/2)
#root.geometry(f'{root.width}x{root.height}+{root.x}+{root.y}')
root.geometry(f'+{root.x}+{root.y}')


label = Label(text='0', font='Arial 28', bg=BGROOT, height=3)
label.grid(row=0, column=0, columnspan=4, sticky=E, padx=8)

for row in range(2):
    for column in range(4):
        Button(
            text=BUTTONS[row][column],
            font=FONT,
            bd=0, bg=BGOPER,
            width=5,
            activebackground=ACTIVEBG,
            command=lambda text = BUTTONS[row][column]: instantOperations(text)).grid(
                                                                                    row=row + 1,
                                                                                    column=column,
                                                                                    padx=2,
                                                                                    pady=2
                                                                               )

for row in range(2, 6):
    for column in range(3):
        Button(
            text=BUTTONS[row][column],
            font=FONT,
            bd=0,
            bg=BGNUM,
            width=5,
            activebackground=ACTIVEBG,
            command=lambda text = BUTTONS[row][column]: numbers(text)).grid(
                                                                          row=row + 1,
                                                                          column=column,
                                                                          padx=2,
                                                                          pady=2
                                                                     )

for row in range(2, 6):
    Button(
        text=BUTTONS[row][3],
        font=FONT,
        bd=0,
        bg=BGOPER,
        width=5,
        activebackground=ACTIVEBG,
        command=lambda text = BUTTONS[row][3]: operation(text)).grid(
                                                                   row=row + 1,
                                                                   column=3,
                                                                   padx=2,
                                                                   pady=2
                                                              )


root.mainloop()