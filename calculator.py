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
           ('=', '0', ',', '÷'),
)

ans = 0
entry = '0'

# not finished

def instantOperations(str):
    pass
    '''
    global ans
    global entry
    if str == '%':
        ans /= 100
        print(ans)
    elif str == '√':
        ans **= 0.5
        print(ans)
    elif str == 'x²':
        ans **= 2
        print(ans)
    elif str == '¹/x' and ans != 0:
        ans = 1 / ans
        print(ans)
    elif str == 'сᴇ':
        ans = 0
        print(ans)
    elif str == 'с':
        ans = 0
        print(ans)
    elif str == '<':
        ans = ans[:-1]
        print(ans)
    elif str == '±':
        ans *= -1
        print(ans)
    print(str)
'''
def numbers(str):
    if str.isdigit():
        if label.cget('text') == '0':
            label['text'] = str
        else:
            label['text'] = label.cget("text") + str
    elif str == ',' and label.cget('text').count(',') == 0:
        label['text'] = label.cget("text") + str


def operation(str):
    print(str)


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
root.geometry(f'{root.width}x{root.height}+{root.x}+{root.y}')


label = Label(text=entry, font='Arial 28', bg=BGROOT, height=3)
label.grid(row=0, column=0, columnspan=4, sticky=E, padx=8)

for row in range(2):
    for column in range(4):
        Button(
            text=BUTTONS[row][column],
            font=FONT,
            bd=0, bg=BGOPER,
            width=5,
            activebackground=ACTIVEBG,
            command=lambda str = BUTTONS[row][column]: instantOperations(str)).grid(
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
            command=lambda str = BUTTONS[row][column]: numbers(str)).grid(
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
        command=lambda str = BUTTONS[row][3]: operation(str)).grid(
                                                                   row=row + 1,
                                                                   column=3,
                                                                   padx=2,
                                                                   pady=2
                                                              )


root.mainloop()