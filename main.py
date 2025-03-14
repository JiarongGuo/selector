import tkinter as tk
import random as rd

# constant
VER = (1, 0, 2, 1)

# window
w = tk.Tk()

# variables
lrv = tk.StringVar(value='结果为：')


# button commands
def bsc():
    n = int(se.get())
    r = rd.randint(1, n)
    lrv.set('结果为：' + str(r))


# window widgets
w.title('166班抽盲盒')
le = tk.Label(w, text='请输入人数')
se = tk.Entry(w)
bs = tk.Button(w, text='抽取', command=bsc)
lr = tk.Label(w, textvariable=lrv)

# placing
le.pack()
se.pack()
bs.pack()
lr.pack()

# main
if __name__ == '__main__':
    tk.mainloop()
