import tkinter as tk
# noinspection SpellCheckingInspection
import tkinter.messagebox as tkms
import random as rd
import os
import datetime as dt

lo = open('log', 'a')  # logging


# functions
def log(level, message):
    lv = ['', 'INFO', 'WARNING', 'ERROR']
    print(dt.datetime.now(), '[' + lv[level] + ']:', message, file=lo)


def init_seed():
    log(1, 'reinitializing seeds')
    with open('seed.txt', 'w') as fi:
        fi.write(str(list(range(0, 101))))
    return list(range(0, 101))


def write(ss):
    log(1, 'writing seeds')
    with open('seed.txt', 'w') as fi:
        fi.write(str(ss))


def read():
    log(1, 'reading seeds')
    if os.path.exists('seed.txt'):
        with open('seed.txt', 'r') as f:
            try:
                s = eval(f.read())
            except PermissionError as e:
                log(3, type(e).__name__ + str(e))
                tkms.showerror('错误', '权限不足')
                return
            except Exception as e:
                log(3, type(e).__name__ + str(e))
                return init_seed()
            if not (type(s) == list and len(s) == 101 and s[0] == 0):
                log(2, 'seed file error')
                return init_seed()
    else:
        return init_seed()
    return s


# window
w = tk.Tk()

# variables
lrv = tk.StringVar(value='结果为：')


# button commands
def bsc():
    log(1, 'started')
    s = read()
    log(1, 'seeds: ' + str(s))
    seed = int(se.get())
    log(1, 'chose No.' + se.get())
    if not 1 <= seed <= 100:
        log(2, 'seed number invalid')
        tkms.showerror('错误', '请输入一个1-100的数字')
        return
    rd.seed(s[seed])
    r = rd.randint(1, 10)
    lrv.set('结果为：' + str(r))
    log(1, 'result: ' + str(r))
    ns = rd.randint(1, 100)
    s[seed] = ns
    log(1, 'new seed:' + str(ns))
    write(s)


# window widgets
w.title('166班抽盲盒')
le = tk.Label(w, text='请输入一个1-100的数字')
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
    log(1, 'program starting')
    tk.mainloop()
