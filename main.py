import tkinter as tk
import pyperclip

bgclr = '#b5fffc'

window = tk.Tk()
window.title('Enchantment generator')
window.geometry('315x515+400+300')
window.resizable(False, False)
window.config(bg=bgclr)
window.entrylist = []
window.cbuttlist = []
window.iconbitmap('D:\gen_ico.ico')

res_lvl_mas = []
res_mas = []


def enchwind(chk_ench, ench, txt_ench, lvl_ench, ench_name, row, column):
    chk_ench = tk.BooleanVar()
    chk_ench.set(False)
    ench = tk.Checkbutton(window, text=ench_name, var=chk_ench, bg=bgclr)
    ench.grid(row=row, column=column, sticky='w')
    txt_ench = tk.Entry(window, width=3)
    txt_ench.grid(row=row, column=column + 1)
    window.entrylist.append(txt_ench)
    window.cbuttlist.append(chk_ench)


def resstr(lvl, resmas, item):
    res = ''
    list = ['/give @p ', '{', 'Enchantments:[']
    list.insert(1, item)
    for i in range(len(lvl)):
        list.append('{id:"minecraft:')
        list.append(resmas[i])
        list.append('",lvl:')
        list.append(lvl[i])
        if i != len(lvl) - 1:
            list.append('}, ')
        else:
            list.append('}')
    list.append(']}')
    for i in range(len(list)):
        res += list[i]
    return res


ench_mas = []
name_mas = ['Aqua affinity', 'Bane of arthropods', 'Binding curse', 'Blast protection',
            'Channeling', 'Depth strider', 'Efficiency', 'Feather falling', 'Fire aspect',
            'Fire protection', 'Flame', 'Fortune', 'Frost walker', 'Impaling', 'Infinity',
            'Knockback', 'Looting', 'Loyalty', 'Luck of the sea', 'Lure', 'Mending',
            'Power', 'Projective protection', 'Protection', 'Punch', 'Respiration',
            'Riptide', 'Sharpness', 'Silk touch', 'Smite', 'Sweeping', 'Thorns',
            'Unbreaking', 'Vanishing curse']

for i in range(34):
    ench_mas.append([])
for i in range(34):
    for j in range(7):
        ench_mas[i].append(0)
for i in range(34):
    ench_mas[i][4] = name_mas[i]
for i in range(17):
    ench_mas[i][5] = i + 1
    ench_mas[i][6] = 0
for i in range(17, 34):
    ench_mas[i][5] = i - 16
    ench_mas[i][6] = 2

ench_list = tk.Label(window, text='Choose the enchantments:', bg=bgclr)
ench_list.grid(row=0, column=0, columnspan=4)

result = tk.Label(window, text='', bg=bgclr)
result.grid(row=20, column=0, columnspan=4)

for i in range(34):
    enchwind(ench_mas[i][0], ench_mas[i][1], ench_mas[i][2], ench_mas[i][3],
             ench_mas[i][4], ench_mas[i][5], ench_mas[i][6])


def clicked():
    for k in range(34):
        if window.cbuttlist[k].get():
            res_lvl_mas.append(window.entrylist[k].get())
            res_mas.append(ench_mas[k][4])

    r_item = item.get()
    txt = resstr(res_lvl_mas, res_mas, r_item)
    pyperclip.copy(txt)
    result.configure(text='Success!')
    clean()

def clean():
    global res_lvl_mas
    global res_mas
    global txt
    res_mas = []
    res_lvl_mas = []
    txt = ''

item_label = tk.Label(window, text='Enter Item:', bg=bgclr)
item_label.grid(column=0, row=18, sticky='w')
item = tk.Entry(window)
item.grid(column=0, row=18, columnspan=4)

btn = tk.Button(window, text='Generate!', command=clicked, bg=bgclr)
btn.grid(column=0, row=19, columnspan=4)


window.mainloop()