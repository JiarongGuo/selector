import datetime as dt
import os.path
import random as rd
import sys
import tkinter as tk
import tkinter.messagebox as tkms

# constant
VER = (1, 0, 2, 3)
seed: int

# window
w = tk.Tk()

# variables
lrv = tk.StringVar(value='结果为：')


# button commands
def bsc():
    try:
        n = int(se.get())
        assert n > 0
    except (AssertionError, ValueError):
        tkms.showerror('错误', '请输入正整数')
        return
    r = rd.randint(1, n)
    lrv.set('结果为：' + str(r))


# window widgets
w.title('166班点名器')
le = tk.Label(w, text='请输入人数')
se = tk.Entry(w)
bs = tk.Button(w, text='抽取', command=bsc)
lr = tk.Label(w, textvariable=lrv)
lv = tk.Label(w, text=f'v{VER[0]}.{VER[1]}.{VER[2]} build {VER[3]}')
bc = tk.Button(w, text='   ', relief=tk.FLAT,
               command=lambda: tkms.showinfo('版权信息',
                                             f'Copyright (c) {dt.date.today().year} Guo Jiarong\r\nAlright reserved.'))

# placing
le.pack()
se.pack()
bs.pack()
lr.pack()
lv.pack()
bc.pack()

# main
if __name__ == '__main__':
    try:
        if not os.path.exists(r'seed'):
            open(r"seed", 'w').close()
        with open(r"seed", 'r') as f:
            try:
                seed = eval(f.read())
            except SyntaxError:
                seed = 166
    except PermissionError:
        tkms.showerror('错误', '权限不足')
        sys.exit()
    rd.seed(seed)
    tk.mainloop()
    with open(r"seed", 'w') as f:
        f.write(str(rd.randint(1, 65535)))
