from tkinter import *


ACTIVEBG = '#c5c5c5'
BGROOT = '#c9c9c9'
BGNUM = '#f7f7f7'
BGOPER = '#e1e1e1'
FONT = 'Verdana 17'
BUTTONS = (
           ('%', '√x', 'x²', '¹/x'),
           ('сᴇ', 'с', '⌫', '±'),
           ('7', '8', '9', '×'),
           ('4', '5', '6', '-'),
           ('1', '2', '3', '+'),
           ('=', '0', '.', '÷'),
)


ans = 0
lastOper = '='


def default():
    global ans
    global lastOper
    ans = 0
    lastOper = '='
    return 0

def is_digit(string):
    if string.isdigit():
       return True
    try:
        float(string)
        return True
    except ValueError:
        return False

def calc(lastOper, labelValue):
    global ans
    if lastOper == '=':
        ans = labelValue
    elif lastOper == '+':
        ans += labelValue
    elif lastOper == '-':
         ans -= labelValue
    elif lastOper == '×':
         ans *= labelValue
    elif lastOper == '÷':
        try:
            ans /= labelValue
        except ZeroDivisionError:
            ans = 0
    if str(ans).endswith('.0'):
        ans = int(ans)

def instantOperations(text):
    labelValue = label.cget('text')
    if text == '⌫':
        if labelValue == '':
            default()
        else:
            labelValue = labelValue[:-1]
    else:
        if is_digit(labelValue):
            labelValue = float(labelValue)
            try:
                if text == '%':
                    labelValue = labelValue / 100
                elif text == '√x':
                    if labelValue >= 0:
                        labelValue = labelValue ** 0.5
                elif text == 'x²':
                    labelValue = labelValue ** 2
                elif text == '¹/x':
                    if labelValue != 0:
                        labelValue = 1 / labelValue
                elif text == 'сᴇ' or text == 'с':
                    labelValue = default()
                elif text == '±':
                    labelValue = -labelValue
            except OverflowError:
                labelValue = 'inf'
            if str(labelValue).endswith('.0'):
                labelValue = int(labelValue)
    label['text'] = str(labelValue)

def numbers(text):
    if text.isdigit():
        if label.cget('text') == '0':
            label['text'] = text
        else:
            label['text'] = label.cget("text") + text
    elif text == '.' and label.cget('text').count('.') == 0:
        label['text'] = label.cget("text") + text
    elif text == '=':
        operations(text)


def operations(text):
    global ans
    global lastOper
    try:
        labelValue = float(label.cget("text"))
    except ValueError:
        labelValue = 0
    calc(lastOper, labelValue)
    if text == '=':
        label['text'] = str(ans)
    else:
        label['text'] = ''
    lastOper = text


root = Tk()
root.iconbitmap('calc.ico')
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

root.geometry(f'+{root.x}+{root.y}')


label = Label(text='0', font='Verdana 25', bg=BGROOT, height=3)
label.grid(row=0, column=0, columnspan=4, sticky=E, padx=8)

for row in range(2):
    for column in range(4):
        Button(
            text=BUTTONS[row][column],
            font=FONT,
            bd=0,
            bg=BGOPER,
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
        command=lambda text = BUTTONS[row][3]: operations(text)).grid(
                                                                   row=row + 1,
                                                                   column=3,
                                                                   padx=2,
                                                                   pady=2
                                                                 )


root.mainloop()