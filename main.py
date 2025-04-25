import datetime as dt
import random as rd
import tkinter as tk
import tkinter.messagebox as tkms

# debug flag
#################################### WARNING: TURN IT INTO FALSE WHEN VERSION END!! ####################################
_DEBUG_ = False

# constant
VER = (1, 0, 4, 6)
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
    s = dt.datetime.now().timestamp()
    if _DEBUG_:
        tkms.showinfo('DEBUG', 'seed: '+str(s))
    rd.seed(s)
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
    tk.mainloop()
