import random
import tkinter as tk
import time

xlen, ylen = 30, 30
mas = []
cell = 20
window = tk.Tk()

w = tk.Canvas(window, width=cell * xlen, height=cell * ylen)


def drawr():
    w.delete("all")
    for yy in range(ylen):
        for xx in range(xlen):
            if mas[yy][xx] == -3:
                color = "red"
            if mas[yy][xx] == 0:
                color = "green"
            if mas[yy][xx] == -2:
                color = "black"
            if mas[yy][xx] == -1:
                color = "white"
            if mas[yy][xx] > 0:
                color = "grey"
            if mas[yy][xx] <= -999:
                color = "cyan"
            w.create_rectangle(xx * cell, yy * cell, xx * cell + cell, yy * cell + cell, fill=color, outline='white')
            textforlabel = str(mas[yy][xx])
            if mas[yy][xx] <0  and mas[yy][xx]>-999:
                textforlabel = ""
            if mas[yy][xx] <-999:
                textforlabel=str((mas[yy][xx]+999)*-1)
            w.create_text(xx * cell + (cell / 2), yy * cell + (cell / 2), text=textforlabel)
    w.pack()


def drawback():
    color = "cyan"

    xx = xlen - 1
    yy = xlen - 1

    while (xx != 0 or yy != 0):
        a = []
        if xx > 0:
            if mas[yy][xx - 1] >= 0:
                a.append(mas[yy][xx - 1])
        if xx < xlen - 1:
            if mas[yy][xx + 1] >= 0:
                a.append(mas[yy][xx + 1])
        if yy > 0:
            if mas[yy - 1][xx] >= 0:
                a.append(mas[yy - 1][xx])
        if yy < ylen - 1:
            if mas[yy + 1][xx] >= 0:
                a.append(mas[yy + 1][xx])

        # print(a,xx,yy)
        if xx > 0:
            if mas[yy][xx - 1] == min(a):
                xx = xx - 1
                yy = yy
        if xx < xlen - 1:
            if mas[yy][xx + 1] == min(a):
                xx = xx + 1
                yy = yy
        if yy > 0:
            if mas[yy - 1][xx] == min(a):
                xx = xx
                yy = yy - 1
        if yy < ylen - 1:
            if mas[yy + 1][xx] == min(a):
                xx = xx
                yy = yy + 1
        mas[yy][xx] = -999-mas[yy][xx]
    drawr()


# drawr()
# input()
gc = 0


def Reset_map():
    global gc, mas
    mas = []
    for i in range(ylen):
        mas.append([])
        for j in range(xlen):
            mas[i].append(max(-2, round(random.randint(-17, -10) / 10)))
    mas[0][0] = 0
    mas[ylen - 1][xlen - 1] = -3
    gc = 0
    mas[0][1] = -1
    mas[1][0] = -1
    mas[1][1] = -1

    mas[ylen - 2][xlen - 1] = -1
    mas[ylen - 1][xlen - 2] = -1
    mas[ylen - 2][xlen - 2] = -1


Reset_map()
while True:

    gc += 1
    delta = False
    for y in range(ylen):
        for x in range(xlen):
            if mas[y][x] >= 0:
                if y > 0:
                    if mas[y - 1][x] != -2:
                        if mas[y - 1][x] == -1:
                            mas[y - 1][x] = mas[y][x] + 1
                            delta = True
                if y < ylen - 1:
                    if mas[y + 1][x] != -2:
                        if mas[y + 1][x] == -1:
                            mas[y + 1][x] = mas[y][x] + 1
                            delta = True
                if x > 0:
                    if mas[y][x - 1] != -2:
                        if mas[y][x - 1] == -1:
                            mas[y][x - 1] = mas[y][x] + 1
                            delta = True
                if x < xlen - 1:
                    if mas[y][x + 1] != -2:
                        if mas[y][x + 1] == -1:
                            mas[y][x + 1] = mas[y][x] + 1
                            delta = True

    if (mas[ylen - 2][xlen - 1] >= 0) or (mas[ylen - 1][xlen - 2] >= 0):
        print("YES")
        drawback()
        window.update()
        time.sleep(5)
        Reset_map()
        continue

    if delta == False:
        Reset_map()
    if gc % 1==0:
        drawr()
        window.update()
    # print("----")

    # time.sleep(0 )
    if gc > 1000:
        print("No")
        Reset_map()
