
def set_wallpaper(path):
    import ctypes
    cs = ctypes.c_buffer(path.encode())
    SPI_SETDESKWALLPAPER = 0x14
    return ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, cs, 0)
import os
import datetime
import time
from PIL import Image, ImageEnhance


points = Image.open('points.png')
colour = Image.open('colour.png')

###Считывает параметры из файла settings.txt###
f = open('settings.txt', 'r')
str_x = str(f.readline())
str_y = str(f.readline())
str_t = str(f.readline())
timet=''
x=''
y=''
s=0
while s < int(len(str_x)):
    w=str(str_x[s])
    if w.isdigit():
        x = x + str(w)
        s += 1
    else:
        s += 1
s=0
while s < int(len(str_y)):
    w=str(str_y[s])
    if w.isdigit():
        y = y + str(w)
        s += 1
    else:
        s += 1
s=0
while s < int(len(str_t)):
    w=str(str_t[s])
    if w.isdigit():
        timet = timet + str(w)
        s += 1
    else:
        s += 1
x=int(x)
y=int(y)


##Цикл обновляющий время##
while True:
    now = str(datetime.datetime.now())
    d_hour = Image.open(now[11]+'.png')
    e_hour = Image.open(now[12]+'.png')
    d_minute = Image.open(now[14]+'.png')
    e_minute = Image.open(now[15]+'.png')

    img = Image.open('clock_fon.png')
    img.paste(d_hour, (0, 0),  d_hour)
    img.paste(e_hour, (92, 0),  e_hour)
    img.paste(points, (182, 0),  points)
    img.paste(d_minute, (276, 0),  d_minute)
    img.paste(e_minute, (368, 0),  e_minute)

    fon = Image.open('fon.png')
    fon.paste(colour, (x,y), img)
    img.save("clock.png")
    fon.save('fon_fin.png')
    set_wallpaper (str(os.getcwd())+'/fon_fin.png')
    time.sleep(int(timet))
