from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import os

Hbool = 0
Sbool = 0
Ibool = 0
Hcount = 0
Scount = 0
Icount = 0

root = Tk()
root.title("Параметры HSI")
root.geometry('1400x700')
root["bg"]="#eee"
can = Canvas(width=1400, height=700, bg='#eee')


img = Image.open ("image.jpg")  # загружаем изображение
img.thumbnail((600, 600), resample=0)
imgTk = ImageTk.PhotoImage(img)
centerx = 350 - (img.size[0]//2)
canimg = can.create_image(centerx, 15, anchor=NW, image=imgTk)
text1 = can.create_text(centerx,img.size[1]+20,anchor=NW,text="(image.jpg, размер:" + str(Image.open("image.jpg").size) + ", original)",font =('Arial', 10))

imgHSI = img.convert("HSV")
imgHSI.thumbnail((600, 600), resample=0)
imgTkHSI = ImageTk.PhotoImage(imgHSI)
centerx = 1050 - (img.size[0]//2)
canimgHSI = can.create_image(centerx, 10, anchor=NW, image=imgTkHSI)
text2 = can.create_text(centerx,imgHSI.size[1]+20,anchor=NW,text="(HSI.jpg, размер:" + str(Image.open("image.jpg").size) + ", HSI)",font =('Arial', 10))

text3 = can.create_text(centerx + 400, imgHSI.size[1] + 20, anchor=NW, text="H="+ str(Hcount)+"  S="+ str(Scount)+"  I="+str(Icount), font=('Arial', 10))


def HSIupparametrs():
    global canimgHSI , text3
    global Hcount, Scount, Icount
    can.delete(canimgHSI)
    draw = ImageDraw.Draw(imgHSI)  # Создаем инструмент для рисования.
    width = imgHSI.size[0]  # Определяем ширину.
    height = imgHSI.size[1]  # Определяем высоту.
    pix = imgHSI.load()  # Выгружаем значения пикселей.
    for i in range(width):
        for j in range(height):
            H = pix[i, j][0]
            S = pix[i, j][1]
            I = pix[i, j][2]
            if (Hbool == 1):
                draw.point((i, j), (H+10, S, I))
            elif (Hbool == 2):
                draw.point((i, j), (H-10, S, I))
            elif (Sbool == 1):
                draw.point((i, j), (H, S+10, I))
            elif (Sbool == 2):
                draw.point((i, j), (H, S-10, I))
            elif (Ibool == 1):
                draw.point((i, j), (H, S, I+10))
            elif (Ibool == 2):
                draw.point((i, j), (H, S, I-10))
    if (Hbool == 1):
        Hcount += 10
    elif (Hbool == 2):
        Hcount -= 10
    elif (Sbool == 1):
        Scount += 10
    elif (Sbool == 2):
        Scount -= 10
    elif (Ibool == 1):
        Icount += 10
    elif (Ibool == 2):
        Icount -= 10
    imgTkHSI = ImageTk.PhotoImage(imgHSI)
    can.image = imgTkHSI
    canimgHSI = can.create_image(centerx, 10, anchor=NW, image=imgTkHSI)
    can.itemconfigure(text3, text = "H="+ str(Hcount)+"  S="+ str(Scount)+"  I="+str(Icount))

def HUp():
    global Hbool
    Hbool = 1
    HSIupparametrs()
    Hbool = 0
def HDown():
    global Hbool
    Hbool = 2
    HSIupparametrs()
    Hbool = 0
def SUp():
    global Sbool
    Sbool = 1
    HSIupparametrs()
    Sbool = 0
def SDown():
    global Sbool
    Sbool = 2
    HSIupparametrs()
    Sbool = 0
def IUp():
    global Ibool
    Ibool = 1
    HSIupparametrs()
    Ibool = 0
def IDown():
    global Ibool
    Ibool = 2
    HSIupparametrs()
    Ibool = 0

def Pravilo():
    global canimgHSI, text3
    global Hcount, Scount, Icount
    can.delete(canimgHSI)
    draw = ImageDraw.Draw(imgHSI)  # Создаем инструмент для рисования.
    width = imgHSI.size[0]  # Определяем ширину.
    height = imgHSI.size[1]  # Определяем высоту.
    pix = imgHSI.load()  # Выгружаем значения пикселей.
    for i in range(1, height):
        for j in range(width):
            H = pix[j, i][0]
            S = pix[j, i][1]
            I = pix[j, i-1][2]
            draw.point((j, i), (H, S, I))
    imgTkHSI = ImageTk.PhotoImage(imgHSI)
    can.image = imgTkHSI
    canimgH = can.create_image(centerx, 10, anchor=NW, image=imgTkHSI)
    can.itemconfigure(text3, text="H=" + str(Hcount) + "  S=" + str(Scount) + "  I=" + str(Icount))






btnHUp = Button(text="Тон (UP)", font=('Arial', 12), background="#999", foreground="#111", command=HUp)
btnHUp.place(x=1100, y=450)
btnHDown = Button(text="Тон (Down)", font=('Arial', 12), background="#999", foreground="#111", command=HDown)
btnHDown.place(x=1200, y=450)
btnSUp = Button(text="Насыщ. (UP)", font=('Arial', 12), background="#999", foreground="#111", command=SUp)
btnSUp.place(x=1060, y=500)
btnSDown = Button(text="Насыщ. (Down)", font=('Arial', 12), background="#999", foreground="#111", command=SDown)
btnSDown.place(x=1200, y=500)
btnIUp = Button(text="Яркость (UP)", font=('Arial', 12), background="#999", foreground="#111", command=IUp)
btnIUp.place(x=1055, y=550)
btnIDown = Button(text="Яркость (Down)", font=('Arial', 12), background="#999", foreground="#111", command=IDown)
btnIDown.place(x=1200, y=550)

btnWork = Button(text="Изменение по правилу", font=('Arial', 12), background="#999", foreground="#111", command=Pravilo)
btnWork.place(x=700, y=500)

can.pack()
root.mainloop()