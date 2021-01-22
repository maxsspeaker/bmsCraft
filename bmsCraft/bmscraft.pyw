print("загрузка емулятора pyBms кода....")
print("библеотек загруска...")
ErorrONcrean=0
game_end = False
import traceback
import time
import os
import random
from tkinter import *
from tkinter import messagebox as mb
try:
    import pygame
    ErorrONcrean=1
    import json
    import socket
    import requests
    from tkinter import *
    from os import path
    from multiprocessing import Pool


    
    
except:
    print('Erorr code:\n', traceback.format_exc())
    root = Tk()
    root.title("Erorr RedSpark engine")
    mb.showerror(
        "Erorr", 
        traceback.format_exc())
        
    try:root.destroy()
    except:pass
    if(ErorrONcrean==1):
        pygame.init()
        pygame.display.set_caption("bmscraft (произошла ошибка)")
        display = pygame.display.set_mode((800, 600))
        pygame.draw.circle(display,(255,0,0), (400, 500), 50, 30)
        pygame.draw.ellipse(display, (255,0,0), (350, 50, 100, 350))
        pygame.display.update()
        while not game_end:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  display.fill((0, 0, 0))
                  pygame.display.update()
                  game_end = True
                  pygame.quit()
                  exit()
            pygame.draw.circle(display,(255,0,0), (400, 500), 50, 30)
            pygame.draw.ellipse(display, (255,0,0), (350, 50, 100, 350))
            pygame.display.update()

    

video=0
print("")
time.sleep(2)
os.system("cls")
print("загрузка емулятора pyBms кода....")
print("библеотек загруска...")

time.sleep(2)
#эта куча и есть движок месте с игрой xD    
blok_datanew = [
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_air", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air", "blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air","blok_air"],
["blok_gras", "blok_land", "blok_land", "blok_land", "blok_land", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras", "blok_gras","blok_gras","blok_gras","blok_gras","blok_gras","blok_gras","blok_gras","blok_gras"],
["blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land", "blok_land","blok_land","blok_land","blok_land","blok_land","blok_land","blok_land","blok_land"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok","blok_air"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_ore_iron", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok", "blok_rok"],
["blok_gras","blok_land","blok_rok","Erorr","blok_ore_iron","blok_ore_diamond","blok_coal_ore","",""]
]


print("загруска мира...")












android=0
print("загруска переменных с адрисом папок")
folder_path = os.path.join(path.dirname(__file__))
if(android==1):
 datafiles="/storage/emulated/0/gamedat/" # андроит версия
 datafiles1=datafiles+"logo/prievzostawca_"
 datafilesloading=datafiles+"animetloading/preview_"
 filesWorld="worlds/"
if(android==0):
 try:                               # boomOS версия
     datafiles=folder_path+"gamedat\\"
     dataFolder = os.listdir(datafiles)
 except:
     datafiles=folder_path+"\\gamedat\\"
     dataFolder = os.listdir(datafiles)
 datafiles1=datafiles+"logo\prievzostawca_"
 datafilesloading=datafiles+"animetloading\preview"
 datafilesSetings=datafiles+"animetsetting\\animetsetting"
 fonmusicmenu=datafiles+"Meanone - Your Favourite Spaceship (Space Rangers LP - Omni064).mp3"
 pygame.display.set_icon(pygame.image.load('boomOS.ico'))










config = [
"ru", #язык
0.5] #0] .5 # громкость

with open(datafiles+"config.txt", 'r') as fr:
                     config = json.load(fr)

print("лакализацыя загруска...")
langeu=config[0]
if("ru"==langeu):
    from ru import *
    
if("en"==langeu):
    from en import *
if("polsk"==langeu):
    from polsk import *


print("лакализацыя: "+langeu)
print("проверка лакализацыи")
try:
    battanplaygame1_1
    battanLoadGame
    battanplaygameONLAIN1_1
    loading_game
    version_name
    exit_battanmenu
    setingsbottan
    battanCreatGame
    ventutsaBattan
except:
    time.sleep(2)
    print("лакализацыя не прошла проверку загружаю стондартную лакализацыю")
    from ru import *
    print("лакализацыя: ru")
    try:
       battanplaygame1_1
       battanLoadGame
       battanplaygameONLAIN1_1
       loading_game
       version_name
       exit_battanmenu
       setingsbottan
       battanCreatGame
       ventutsaBattan
    except:
        print("стондартная лакализацыя не прошла тоже проверку! скачиваю из интернета лакалихацыю")
        r = requests.get("https://github.com/maxsspeaker/bmsCraft/raw/main/bmsCraft/ru.py", stream=True)
        i=0
        with open("ru.py", 'wb') as f:
                   for block in r.iter_content(1024):
                    f.write(block)
                    i+=1
                    if i <= 100:
                        print("скачиваем:",i, end='%\n')
        
    
 






version="alpha 1.9.3"



print("инитилизацыя экрана и статуса в discord")
print("pygame "+version_name+pygame.version.ver)

if(android==0):
 Config="\nClientID=769246787596058635 \nState="+"loading"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_main_menu"
 open("config.ini", 'w').write(Config)
 




     


  
def rus_click():
    config[0]="ru"
    with open(datafiles+"config.txt", 'w') as fw:
          json.dump(config, fw)
def en_click():
    config[0]="en"
    with open(datafiles+"config.txt", 'w') as fw:
          json.dump(config, fw)
def polsk_click():
    config[0]="polsk"
    with open(datafiles+"config.txt", 'w') as fw:
          json.dump(config, fw)
          
def search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return True
    return False





#https://github.com/maxsspeaker/bmsCraft/raw/main/bmsCraft/gamedat/


filesNormal=['17-Excuse-.mp3', '17-Excuse.mp3', 'AMONG_US_ M_T_S.mp3', 'Among_Us_-_M_M_Piano.mp3', 'animetloading', 'animetsetting', 'blok_air.png', 'blok_bedrokpng.png',
             'blok_coal_ore.png', 'blok_gras.png', 'blok_land.png', 'blok_ore_diamond.png', 'blok_ore_iron.png', 'blok_radio_interat.png', 'blok_rok.png', 'config.txt', 'conve.ogg', 'cursor.png',
             'cursor1.png', 'Erorr screan.png', 'Fluxion - En Route net cor.mp3', 'game_Main_Menu.png', 'game_rase_furry.png', 'game_rase_human.png', 'game_rase_none.png', 'gui_inventari.png', 'Hit_Hurt10.wav',
             'Hit_Hurt19.wav', 'icon_worldNONE.png', 'icon_worldsave.png', 'icon_worldsaveSelect.png', 'Late Night Danalog Multirex(loop).mp3', 'logo', 'logo-', 'logo.png', 'logo_engine.png', 'logo_engine2.png',
             'mane_menufon-nofan.png', 'mane_menufon.png', 'mane_menufonOLD.png', 'Meanone - Your Favourite Spaceship (Space Rangers LP - Omni064).mp3',
             'menu_battan.png', 'menu_worlds.png', 'menu_world_battan.png', 'noneblok.png', 'otxhello - depression.mp3', 'razrabi.jpg', 'select.png', 'sky.png', 'splasers.txt', 'testplayer1.png', 'VAX3p9.mp4', 'worlds', 'Безымянный.png']

print("проверка целосность фаилов")

filesto=0
while not len(filesNormal) == filesto:
    if(search(dataFolder,filesNormal[filesto])== True):
        print("файл прошёл проверку на наличее его: ",filesNormal[filesto])
    else:
        print("не найден: ",filesNormal[filesto])
        vopros=str(input("хатите скачать файл которого нету? Y/N "))
        if(vopros=="y") or (vopros=="Y"):
            r = requests.get("https://github.com/maxsspeaker/bmsCraft/raw/main/bmsCraft/gamedat/"+filesNormal[filesto], stream=True)
            i=0
            with open(datafiles+filesNormal[filesto], 'wb') as f:
                   for block in r.iter_content(1024):
                    f.write(block)
                    i+=1
                    if i <= 100:
                        print("скачиваем:",i, end='%\n')

        else:
          vopros=str(input("файлы не прошли проверку на целосность продолжить? Y/N "))
          if(vopros=="y") or (vopros=="Y"):
                   print("продолжить")
          else:
                   exit()
          
    filesto=filesto+1




if(android==0):
    os.startfile("easyrp.exe")


    
print("загрузки музыки чтобы скучно небыло")


time.sleep(2)
animation=1
play=0
x=0
y=0
#os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)






# initialize pygame
pygame.init()

if(video==1):
    pygame.display.set_caption("я пешу с классами игру:")
    clip = VideoFileClip(datafiles+"VAX3p9.mp4")
    clip.preview()
    display = pygame.display.set_mode((1, 1),flags = pygame.NOFRAME)

time.sleep(1)    
pygame.mixer.init(22050, -16, 2, 2048)
pygame.mixer.music.load(fonmusicmenu)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(config[1])


print("потключаем началные фаилы и настройки")
clock = pygame.time.Clock() 


# create display & run update
width = 800
height = 600
#width = 1920
#height = 1080

heightaim=0

pygame.display.set_caption("bmscraft")

display = pygame.display.set_mode((width, height))

while not (height == heightaim)  : 
    display = pygame.display.set_mode((width, heightaim),flags = pygame.NOFRAME) #
    heightaim=heightaim+5
    
    clock.tick(50)


if(android==0):
    pygame.display.set_icon(pygame.image.load('boomOS.ico'))

display = pygame.display.set_mode((width, height),pygame.HWSURFACE) #NOFRAME ,flags = pygame.OPENGL
#pygame.display.update()
def Loadingbardr(progress):
    maxwidth=300
    pygame.draw.rect(display, (255,255,255), pygame.Rect(50,550,progress*3,10))
    pygame.draw.rect(display, (128,128,128), pygame.Rect(50,550,maxwidth,10), 1) 
    pygame.display.update()


Loadingbardr(0)
time.sleep(1)
#pygame.mouse.set_visible(False)

print(loading_game)


Loadingbardr(10)
def ErorrScr():
 if(Erorrsrean==1):
     display.fill((0, 0, 0))
     pygame.display.update()
     time.sleep(1)
     
     font = pygame.font.Font(None, 20)
     menufon_rect = Erorr_surf.get_rect(bottomright=(800, 600)) 
     display.blit(Erorr_surf, menufon_rect)
     
     textfps = font.render("произошла ошибка игры", 1, (250,0, 0))
     placefps = textfps.get_rect(center=(200, 230))
     display.blit(textfps, placefps)
     
     textfps = font.render("код ошибки: "+Erorrcode, 1, (250,0, 0)) 
     placefps = textfps.get_rect(center=(280, 250))
     display.blit(textfps, placefps)
     pygame.display.update()
     time.sleep(2)

#
time.sleep(0.8)
Loadingbardr(25)
def aimsetings():
 if(animation==1):
  imglogoim=0
  while not (100==imglogoim):
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
              game_end = True
   clock.tick(30)
   pygame.display.update()
   if(10>imglogoim):
       imglogoimc=("000"+str(imglogoim))
      
   else:
       if(100>imglogoim):
          imglogoimc=("00"+str(imglogoim))
       else:
           if(1000>imglogoim):
             imglogoimc=("0"+str(imglogoim))
   #print(imglogoimc)
   imglogoim=imglogoim+1
   if(imglogoim<84):
       logoloding_surf = pygame.image.load(datafilesSetings+imglogoimc+".png")
       logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
       display.blit(logoloding_surf, logoloding_rect)
       
     
   else:
      logoloding_surf = pygame.image.load(datafilesSetings+"0084.png")
      logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
      display.blit(logoloding_surf, logoloding_rect)
      font = pygame.font.Font(None, 30)
      textfps = font.render(loading_game, 1, (100, 100, 100))
      placefps = textfps.get_rect(center=(200, 30))
      display.blit(textfps, placefps)



time.sleep(0.8)
Loadingbardr(42)
def loading():
 if(animation==1):
  imglogoim=0
  while not (230==imglogoim):
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
              game_end = True
   clock.tick(30)
   pygame.display.update()
   if(10>imglogoim):
       imglogoimc=("000"+str(imglogoim))
      
   else:
       if(100>imglogoim):
          imglogoimc=("00"+str(imglogoim))
       else:
           if(1000>imglogoim):
             imglogoimc=("0"+str(imglogoim))
   #print(imglogoimc)
   imglogoim=imglogoim+1
   if(imglogoim<121):
       logoloding_surf = pygame.image.load(datafilesloading+imglogoimc+".png")
       logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
       display.blit(logoloding_surf, logoloding_rect)
       
     
   else:
      logoloding_surf = pygame.image.load(datafilesloading+"0120.png")
      logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
      display.blit(logoloding_surf, logoloding_rect)
      font = pygame.font.Font(None, 30)
      textfps = font.render(loading_game, 1, (100, 100, 100))
      placefps = textfps.get_rect(center=(200, 30))
      display.blit(textfps, placefps)







time.sleep(0.8)
Loadingbardr(56)    
print("загружаем курсор мышки которого вы не увидите")
CURSOR_rect = pygame.image.load(datafiles+'cursor.png')
Loadingbardr(62)
time.sleep(0.8)
print("загружаем переменные")
 # 16 блоков на адин экрана влизает

game_end = False
bloksX=0
bloksY=0
Loadingbardr(77)
time.sleep(0.8)
#pygame.mouse.set_visible(False) 
cmd=""
cmd1=""
cmd2=""
cmd3=""
cmd4=""
progress=85 
playSenitngs=0
menuWorld=0
despled=0
Erorrsrean=0
Erorrcode=""
bfcube=""
settings=0
bird_pos=(0,0)
bloksCamX=0
bloksCamY=-1200
findbloks=0
menu=1
clock.tick(60)
Renderbloks=True
inventarim=0
loadworldbattan=-1
Loadingbardr(92)
time.sleep(0.8)
print("заставка")
time.sleep(1)
try:
 if(animation==1):
    
  while not (181==imglogoim):
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
             game_end = True
   clock.tick(30)
   if(10>imglogoim):
      imglogoimc=("000"+str(imglogoim))
      
   else:
      if(100>imglogoim):
         imglogoimc=("00"+str(imglogoim))
      else:
          if(1000>imglogoim):
            imglogoimc=("0"+str(imglogoim))
   #print(imglogoimc)
   imglogoim=imglogoim+1
   if(imglogoim<181):
       logoloding_surf = pygame.image.load(datafiles1+imglogoimc+".png")
       logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
       display.blit(logoloding_surf, logoloding_rect)
       Loadingbardr(96)
      
     
   else:
      logoloding_surf = pygame.image.load(datafiles1+"0180.png")
      logoloding_rect = logoloding_surf.get_rect(bottomright=(800, 600))
      display.blit(logoloding_surf, logoloding_rect)
      font = pygame.font.Font(None, 30)
      textfps = font.render(loading_game, 1, (100, 100, 100))
      placefps = textfps.get_rect(center=(200, 30))
      display.blit(textfps, placefps)
     
   fps = str(int(clock.get_fps()))
   font = pygame.font.Font(None, 30)
   textfps = font.render("fps: "+fps, 1, (100, 100, 100))
   placefps = textfps.get_rect(center=(200, 150))
   display.blit(textfps, placefps)
   pygame.display.update()
except:
    print('Erorr code:\n', traceback.format_exc())
    root = Tk()
    root.title("Ошибка анимаций игры")
    mb.showerror(
        "Erorr: ошибка выполнения анимаций (игра не крашнулась)", 
        traceback.format_exc())
    try:root.destroy()
    except:pass
    

try:
    with open(datafiles+"splasers.txt", 'r') as fr:
        sples = json.load(fr)
except:
    sples = ["зачем удалил сплеши ;-;"]



# 8
worldsFolder = os.listdir(datafiles+"worlds")
print("загрузка кнопак меню")
BattanWorld_surf = pygame.image.load(os.path.join(datafiles+"menu_world_battan.png"))
menuWorlds_surf = pygame.image.load(os.path.join(datafiles+"menu_worlds.png"))
battan_surf = pygame.image.load(os.path.join(datafiles+'menu_battan.png'))
menufon_surf = pygame.image.load(os.path.join(datafiles+'mane_menufon.png'))
icon_worldsave = pygame.image.load(os.path.join(datafiles+'icon_worldsave.png'))
icon_worldsaveSelect = pygame.image.load(os.path.join(datafiles+'icon_worldsaveSelect.png'))


Loadingbardr(100)
time.sleep(2)
splesrandom=sples[random.randint(0,len(sples)-1)]
print("завершаем загрузку")
if(android==0):
 f = open("config.ini", 'w')
 Config="\nClientID=769246787596058635 \nState="+"main menu"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_main_menu"
 f.write(Config)
print(loading_game)
despled=0
print("игра загружена")
try: 
 while not game_end:
  display.fill((0, 0, 0))
  
  pygame.mixer.music.set_volume(config[1])
  for event in pygame.event.get():
     if (settings==0):
        if event.type == pygame.QUIT:
            display.fill((0, 0, 0))
            pygame.display.update()
            time.sleep(1)
            game_end = True


     if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 3:
        bird_pos = event.pos
        if(599>bird_pos[1]):
         if(findbloks==1):
          
          print()
          cmd=("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          print("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          cmd1="camX "+str(bloksCamX)+" camY "+str(bloksCamY)
          print("camX "+str(bloksCamX)+" camY "+str(bloksCamY))
         #print()
         
          blokscvX=((bird_pos[0])/50+((bloksCamX-bloksCamX-bloksCamX)/50))
          blokscvY=((bird_pos[1])/50+(bloksCamY-bloksCamY-bloksCamY)/50)
        # print()
          print("blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1))
          cmd2="blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1)
          cmd3="bloksX "+str(int(blokscvX+1))+" bloksY "+str(int(blokscvY+1))
        
          print("bloksX "+str(int(blokscvX+1)))
          print("bloksY "+str(int(blokscvY+1)))
          try:
           if(blokscvY>67):
              print("none blok!")
           else:
             if((int(blokscvX))<(len(blok_data[int(blokscvY)]))):
              if("blok_rok"==blok_data[int(blokscvY)][int(blokscvX)]):
                  cmd4=""
              else:
                  if("blok_air"==blok_data[int(blokscvY)][int(blokscvX)]):
                      print(blok_data[67][inventarim])
                      if not(""==blok_data[67][inventarim]):
                        Playnbr.play()
                        cmd4="clik is "+blok_data[int(blokscvY)][int(blokscvX)]
                        blok_data[int(blokscvY)][int(blokscvX)]=blok_data[67][inventarim]
          except:
               print("блок был не нейден или какойта збой не кретичный ")
        
       
          
      if event.button == 1:  #  левая кнопка мыши
        bird_pos = event.pos

        if(menu==1):
           print("x "+str(bird_pos[0])+" y "+str(bird_pos[1]))
           if(Erorrsrean==1):
                Erorrsrean=0
                settings=0
                menufon_surf = pygame.image.load(os.path.join(datafiles+'mane_menufon.png'))
           if(Erorrsrean==0):
            if(settings==0):   
            #bird_pos 187, 293
            # потсказка для идеотов как я
            # bird_pos[0]это x
            # bird_pos[1]это y 
            
             if(bird_pos[0]<188) and (bird_pos[0]>188-150):
                if(bird_pos[1]<293) and (bird_pos[1]>293-50):
                    if(findbloks==0):
                      if(menuWorld==0):  
                        menuWorld=1
                        print(worldsFolder)
                      if(menuWorld==1):
                        print()
                        if(menuWorld==1):
                          if(loadworldbattan>-1):  
                            font = pygame.font.Font(None, 30)
                            textfps = font.render(loading_game, 1, (100, 100, 100))
                            placefps = textfps.get_rect(center=(200, 30))
                            display.blit(textfps, placefps)
                            Loadingbardr(3)
                            time.sleep(0.8)

                            Loadingbardr(10)
                            time.sleep(0.8)
                            Loadingbardr(23)
                            #loading()
                            Loadingbardr(30)
                            time.sleep(0.8)
                            Loadingbardr(46)
                            time.sleep(0.8)
                            try:
                               with open(datafiles+"worlds\\"+worldsFolder[loadworldbattan], 'r') as fr:
                                  blok_data = json.load(fr)
                            except:
                                print("Erorr")
                                break
                            
                            Loadingbardr(52)
                            time.sleep(0.8)
                            x_plaer=500
                            y_plaer=1000
                            fly=0
                            y_speed=0
                            x_speed=0
                            Loadingbardr(56)
                            time.sleep(0.8)
                            menu=0
                            #datafiles+"worlds"
                            Loadingbardr(76)
                            time.sleep(0.8)
                            
                            breac=pygame.mixer.Sound(datafiles+"Hit_Hurt10.wav")
                            Playnbr=pygame.mixer.Sound(datafiles+"Hit_Hurt19.wav")
                            
                            Loadingbardr(85)
                            time.sleep(0.8)
                            noneblok=pygame.image.load(os.path.join(datafiles+"noneblok.png"))
                            blok_land = pygame.image.load(os.path.join(datafiles+"blok_land.png"))
                            blok_rok = pygame.image.load(os.path.join(datafiles+"blok_rok.png"))
                            blok_coal_ore = pygame.image.load(os.path.join(datafiles+"blok_coal_ore.png"))
                            blok_ore_iron = pygame.image.load(os.path.join(datafiles+"blok_ore_iron.png"))
                            inventarigui_surf = pygame.image.load(os.path.join(datafiles+"gui_inventari.png"))
                            inventariguiselect_surf = pygame.image.load(os.path.join(datafiles+"select.png"))
                            plaer_surf = pygame.image.load(os.path.join(datafiles+"testplayer1.png"))
                            sky_surf = pygame.image.load(os.path.join(datafiles+'sky.png'))
                            print("загрузка мира завершина")
                            findbloks=1
                            time.sleep(2)
                            pygame.mixer.music.load(datafiles+"17-Excuse.mp3")
                            despled=0
                            pygame.mixer.music.play(-1)
                            Loadingbardr(100)
                            time.sleep(3)
             if(bird_pos[0]<188) and (bird_pos[0]>188-150):
                if(bird_pos[1]<100+406) and (bird_pos[1]>100+406-50):
                    if(menuWorld==0):  
                      display.fill((0, 0, 0))
                      pygame.display.update()
                      time.sleep(1)
                      game_end = True
                    if(menuWorld==1):
                        splesrandom=sples[random.randint(0,len(sples)-1)]
                        display.fill((0, 0, 0))
                        pygame.display.update()
                        menuWorld=0
                        loadworldbattan=-1
                        time.sleep(1)

             if(bird_pos[0]<184) and (bird_pos[0]>184-150):
                if(bird_pos[1]<364+50) and (bird_pos[1]>364-50+50):
                    if(menuWorld==0):
                      menufon_surf = pygame.image.load(os.path.join(datafilesSetings+'0084.png'))
                      print("test")
                     # aimsetings()
                      settings=1
             if(bird_pos[0]<188) and (bird_pos[0]>188-150):
                if(bird_pos[1]<293+55) and (bird_pos[1]>293-50+55):
                    if(menuWorld==0):  
                      print("test")
             if(menuWorld==1):
              leniwabattanworld=-60
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=0
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=1
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=2
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=3
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=4
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=5
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=6
             if(menuWorld==1):
              leniwabattanworld=leniwabattanworld+60
              if(bird_pos[0]<769) and (bird_pos[0]>341): 
                if(bird_pos[1]<133+leniwabattanworld) and (bird_pos[1]>64+leniwabattanworld):
                    loadworldbattan=7
              print(loadworldbattan)
                     
             
             
      
                    
                      
                
        
        
        
        if(599>bird_pos[1]):
         if(findbloks==1):
          
          print()
          cmd=("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          print("x "+str(bird_pos[0]+(bloksCamX-bloksCamX-bloksCamX))+" y "+str(bird_pos[1]+(bloksCamY)))
          cmd1="camX "+str(bloksCamX)+" camY "+str(bloksCamY)
          print("camX "+str(bloksCamX)+" camY "+str(bloksCamY))
         #print()
         
          blokscvX=((bird_pos[0])/50+((bloksCamX-bloksCamX-bloksCamX)/50))
          blokscvY=((bird_pos[1])/50+(bloksCamY-bloksCamY-bloksCamY)/50)
        # print()
          print("blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1))
          cmd2="blokX "+str(blokscvX+1)+" blokY "+str(blokscvY+1)
          cmd3="bloksX "+str(int(blokscvX+1))+" bloksY "+str(int(blokscvY+1))
        
          print("bloksX "+str(int(blokscvX+1)))
          print("bloksY "+str(int(blokscvY+1)))
          try:
           if(blokscvY>67):
              print("none blok!")
           else:
             if((int(blokscvX))<(len(blok_data[int(blokscvY)]))):
              if("blok_air"==blok_data[int(blokscvY)][int(blokscvX)]):
                  cmd4=""
              else:
                   breac.play()
                   cmd4="clik is "+blok_data[int(blokscvY)][int(blokscvX)]
                   blok_data[int(blokscvY)][int(blokscvX)]="blok_air"
          except:
              print("блок был не нейден или какойта збой не кретичный ")
              
       # if
      if event.button == 4:
          print("прокручивания вперед")
          if not(inventarim==0):
              inventarim=inventarim-1
         # =0 # 8
          

      if event.button == 5:
          print("прокручивания назад")
          if not(inventarim==8):
              inventarim=inventarim+1
          
  #  elif event.type == pygame.KEYDOWN:

  keys = pygame.key.get_pressed()       
  if keys[pygame.K_a]:
                # move left
                 print("лево")
                 if(findbloks==1):
                   bloksCamX=bloksCamX+10
 
  if keys[pygame.K_d]:
                # move right
                 print("право")
                 if(findbloks==1):
                  bloksCamX=bloksCamX-10
                

 #
  if keys[pygame.K_w]:
                # move up
                 print("верх")
                 if(findbloks==1):
                  bloksCamY=bloksCamY+10

 
  if keys[pygame.K_s]:
                # move down
                 print("низ")
                 if(findbloks==1):
                  bloksCamY=bloksCamY-10
  if keys[pygame.K_u]:
               # if pygame.key == pygame.K_i:
                   # if pygame.key == pygame.K_o:
                        Erorr_surf = pygame.image.load(os.path.join(datafiles+'Erorr screan.png'))
                        Erorrcode=("робота игры была завершина")
                        Renderbloks=False
                        pygame.mixer.music.load(fonmusicmenu)
                        pygame.mixer.music.play(-1)
                        findbloks=0
                        menu=1
                        Erorrsrean=1
                        menuWorld=0
                        loadworldbattan=-1
                        splesrandom=sples[random.randint(0,len(sples)-1)]
                        if(android==0):
                          f = open("config.ini", 'w')
                          Config="\nClientID=769246787596058635 \nState="+"main menu"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_main_menu"
                          f.write(Config)
                        ErorrScr()
  if keys[pygame.K_o]:
    if(findbloks==1):
      with open(datafiles+"worlds\\"+worldsFolder[loadworldbattan], 'w') as fw:
          json.dump(blok_data, fw)
          cmd4="game save!"
          
  if keys[pygame.K_LEFT]:
   if(findbloks==1):
    if(blok_data[round(y_plaer/50-1)][int(x_plaer/50)]=="blok_air"):
               if(blok_data[round(y_plaer/50-2)][int(x_plaer/50)]=="blok_air"):
                          x_plaer=x_plaer-5
    print(blok_data[round(y_plaer/50-1)][int(x_plaer/50)])
    print(blok_data[round(y_plaer/50-2)][int(x_plaer/50)])
    print("лево игрок")
    
  if keys[pygame.K_RIGHT]:
   if(findbloks==1):
    if(blok_data[round(y_plaer/50-1)][int(x_plaer/50+1)]=="blok_air"):
               if(blok_data[round(y_plaer/50-2)][int(x_plaer/50+1)]=="blok_air"):
                          x_plaer=x_plaer+5
    print(blok_data[int(y_plaer/50-1)][int(x_plaer/50+1)])
    print(blok_data[int(y_plaer/50-2)][int(x_plaer/50+1)])
    print("вправо игрок")
    
  if keys[pygame.K_UP]:
   if(findbloks==1):
    if(fly==0):
        ster=5
        while not (50==ster):   
             #if(blok_data[int(y_plaer/50)][int((x_plaer+ster)/50)]=="blok_air"):
             if(blok_data[int(y_plaer/50)-2][int((x_plaer+ster)/50)]=="blok_air"):
                    if(blok_data[int(y_plaer/50)-3][int((x_plaer+ster)/50)]=="blok_air"):
                           flyplar=1
                    else:
                       flyplar=0
                       break 
             else:
                   flyplar=0
                   break 
             #else:
                # flyplar=0
                # break
             ster=ster+1
               
                   
                
        if(flyplar==1):
               y_plaer=y_plaer-50
    # if(blok_data[int(y_plaer/50)-2][int(x_plaer/50)]=="blok_air"):
         #fly=1
         #print("верх игрок")
         
            #if(blok_data[int(y_plaer/50+2)][int(x_plaer/50)]=="blok_air"):
       
       
    
       
    print(blok_data[int(y_plaer/50)-2][int(x_plaer/50)])
               
             
                            
            

        
  if(menu==1):
    
    font = pygame.font.Font(None, 30)
    menufon_rect = menufon_surf.get_rect(bottomright=(800, 600)) 
    display.blit(menufon_surf, menufon_rect)

    
    if(settings==0 and menuWorld==0):   
     menufon_rect = battan_surf.get_rect(bottomright=(184, 293)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(battanplaygame1_1, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 266))
     display.blit(textfps, placefps)

     menufon_rect = battan_surf.get_rect(bottomright=(184, 293+55)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(battanplaygameONLAIN1_1, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 266+55))
     display.blit(textfps, placefps)

     
     menufon_rect = battan_surf.get_rect(bottomright=(184, 364+50)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(setingsbottan, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 100+290))
     display.blit(textfps, placefps)
     

     menufon_rect = battan_surf.get_rect(bottomright=(184, 100+406)) 
     display.blit(battan_surf, menufon_rect)
     textfps = font.render(exit_battanmenu, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 100+380))
     display.blit(textfps, placefps)
     
     
     

     textfps = font.render(battanplaygame1_1, 1, (100, 100, 100))
     placefps = textfps.get_rect(center=(105, 266))
     display.blit(textfps, placefps)

     

    textfps = font.render(version_name+version, 1, (250, 250, 250))
    placefps = textfps.get_rect(center=(800-100, 600-30))
    display.blit(textfps, placefps)
    if(settings==1):
        if(playSenitngs==1):
            display = pygame.display.set_mode((1, 1),flags = pygame.NOFRAME)
        if(playSenitngs==3):
           root = Tk()
           root.title(setingsbottan+" RedSpark engine")
           root.iconbitmap('boomOS.ico')
           root.geometry("400x300")
           
            
           root.resizable(False, False)
           
           main_menu = Menu()
           localization_menu = Menu(font=("Verdana", 8, "bold"), tearoff=0)
           main_menu.add_cascade(label=localization, menu=localization_menu)

           localization_menu.add_command(label="rus",command=rus_click)
           localization_menu.add_command(label="en",command=en_click) 
           localization_menu.add_command(label="polsk",command=polsk_click)
           #localization_menu.add_separator()

           
           
           
           root.config(menu=main_menu)
           root.mainloop()
           display = pygame.display.set_mode((width, height))
           menufon_surf = pygame.image.load(os.path.join(datafiles+'mane_menufon.png'))
           playSenitngs=0
           settings=0
        playSenitngs=playSenitngs+1
 
        
    if(menuWorld==1):
        test43634=0
        
        menufon_rect = battan_surf.get_rect(bottomright=(184, 100+406)) 
        display.blit(battan_surf, menufon_rect)
        textfps = font.render(ventutsaBattan, 1, (100, 100, 100))
        placefps = textfps.get_rect(center=(105, 100+380))
        display.blit(textfps, placefps)
        
        menufon_rect = battan_surf.get_rect(bottomright=(184, 293)) 
        display.blit(battan_surf, menufon_rect)
        
        textfps = font.render(battanLoadGame, 1, (100, 100, 100))
        placefps = textfps.get_rect(center=(105, 266))
        display.blit(textfps, placefps)

        menufon_rect = battan_surf.get_rect(bottomright=(184, 293+55)) 
        display.blit(battan_surf, menufon_rect)
        textfps = font.render(battanCreatGame, 1, (100, 100, 100))
        placefps = textfps.get_rect(center=(105, 266+55))
        display.blit(textfps, placefps)
        
        menuWorlds_rect = menuWorlds_surf.get_rect(bottomright=(800, 600)) 
        display.blit(menuWorlds_surf, menuWorlds_rect)
        #print()
        dlinaworlds=0
        while not (len(worldsFolder)==dlinaworlds): 
         if(8==dlinaworlds):
             break
         BattanWorld_rect = BattanWorld_surf.get_rect(bottomright=(769, 133+(60*dlinaworlds))) 
         display.blit(BattanWorld_surf, BattanWorld_rect)
         try:
           if(worldsFolder[dlinaworlds].split('.')[1]=="wrld"):
             if(loadworldbattan==dlinaworlds):
                 icon_worldsaveSelect_rect = icon_worldsaveSelect.get_rect(bottomright=(395, 123+(60*dlinaworlds)))
                 display.blit(icon_worldsaveSelect, icon_worldsave_rect)
             #else:
             icon_worldsave_rect = icon_worldsave.get_rect(bottomright=(395, 123+(60*dlinaworlds)))
             display.blit(icon_worldsave, icon_worldsave_rect)
               
             textNameWorld = font.render(worldsFolder[dlinaworlds].split('.')[0], 1, (255, 255, 255))
             placeNameWorld = textfps.get_rect(center=(490,89+(60*dlinaworlds)))
             display.blit(textNameWorld, placeNameWorld)
           else:
             textNameWorld = font.render(worldsFolder[dlinaworlds], 1, (255, 255, 255))
             placeNameWorld = textfps.get_rect(center=(490,89+(60*dlinaworlds)))
             display.blit(textNameWorld, placeNameWorld)
         except:
             textNameWorld = font.render(worldsFolder[dlinaworlds], 1, (255, 255, 255))
             placeNameWorld = textfps.get_rect(center=(490,89+(60*dlinaworlds)))
             display.blit(textNameWorld, placeNameWorld)
         dlinaworlds=dlinaworlds+1
         
         #icon_worldsaveSelect #8
    textsples = pygame.font.Font(None, 20)
    textfps = textsples .render(splesrandom, 1, (210, 217, 11))
    placefps = textfps.get_rect(center=(241, 583))
    display.blit(textfps, placefps)
     
     
     
  if(findbloks==1):
   Renderbloks=True
   sky_rect = sky_surf.get_rect(bottomright=(800, 600))
   display.blit(sky_surf, sky_rect)
  # try:
   if(1==1):
    while Renderbloks:
      if not ((bloksX+1)*50+bloksCamX<1):
       if not ((bloksX)*50+bloksCamX>801):
        if not ((bloksY)*50+bloksCamY>601):
         if not ((bloksY+1)*50+bloksCamY<1):
          if not (blok_data[bloksY][bloksX]=="blok_air"):
           if not (bfcube==blok_data[bloksY][bloksX]):
             try:
                 if("blok_land"==blok_data[bloksY][bloksX]):
                     blokimg_surf = blok_land
                 elif("blok_rok"==blok_data[bloksY][bloksX]):
                     blokimg_surf = blok_rok
                 elif("blok_ore_iron"==blok_data[bloksY][bloksX]):
                     blokimg_surf = blok_ore_iron
                 elif("blok_coal_ore"==blok_data[bloksY][bloksX]):
                     blokimg_surf = blok_coal_ore
                 else: 
                     blokimg_surf = pygame.image.load(os.path.join(datafiles+blok_data[bloksY][bloksX]+".png"))
             except:
                 blokimg_surf = noneblok
           blokimg_rect = blokimg_surf.get_rect(bottomright=((bloksX+1)*50+bloksCamX, (bloksY+1)*50+bloksCamY))
           display.blit(blokimg_surf, blokimg_rect)
           bfcube=blok_data[bloksY][bloksX]
        
       #print(blok_data[bloksY][bloksX]+" кордината Y:"+str(bloksY)+" X:"+str(bloksX))
      bloksX=bloksX+1
      if(len(blok_data[bloksY]) == bloksX):
         bloksY=bloksY+1
         bloksX=0
      if(67==bloksY):          
           font = pygame.font.Font(None, 30)
           textfps = font.render("cmd: "+cmd, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 30))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd1, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 45))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd2, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 65))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd3, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 85))
           display.blit(textfps, placefps)
          
           font = pygame.font.Font(None, 30)
           textfps = font.render(""+cmd4, 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 100))
           display.blit(textfps, placefps)


          
           #y_speed=0
          # x_speed=0
           
           plaer_rect = plaer_surf.get_rect(bottomright=(x_plaer+bloksCamX+53.5, y_plaer+bloksCamY))
           display.blit(plaer_surf, plaer_rect)
          

           ster=5
           try:
               
            while not (50==ster):   
             if(blok_data[int(y_plaer/50)][int((x_plaer+ster)/50)]=="blok_air"):
                if(blok_data[int(y_plaer/50-1)][int((x_plaer+ster)/50)]=="blok_air"):
                    fly=1
                else:
                   fly=0
                   break
             else:
                 fly=0
                 break
             ster=ster+1
           except:
               fly=0
                                  
           if(fly==1):
               y_plaer=y_plaer+5
         #  if not(blok_data[int((y_plaer-5)/50)][int((x_plaer+ster)/50)]=="blok_air"):
            #   y_plaer=y_plaer-5
           font = pygame.font.Font(None, 30)
           textfps = font.render("x_plaer: "+str(x_plaer/50)+"y_plaer: "+str(y_plaer/50), 1, (100, 100, 100))
           placefps = textfps.get_rect(center=(200, 125))
           display.blit(textfps, placefps)
           
           inventarigui_rect = inventarigui_surf.get_rect(bottomright=(550, 600))
           display.blit(inventarigui_surf, inventarigui_rect)
           RenderInventari=0
           while not RenderInventari==8:
            if not(blok_data[67][RenderInventari]==""):
             try:
                 blokimginv_surf = pygame.image.load(os.path.join(datafiles+blok_data[67][RenderInventari]+".png"))
             except:
                 blokimginv_surf = pygame.image.load(os.path.join(datafiles+"noneblok.png"))
             blokinventari = pygame.transform.scale(blokimginv_surf, (30, 30))
             inventariguiselect_surf_rect = inventarigui_surf.get_rect(bottomright=(550+4+(36.5*RenderInventari), 600+4))
             display.blit(blokinventari, inventariguiselect_surf_rect)
            RenderInventari=RenderInventari+1
             
               
               
           inventariguiselect_surf_rect = inventarigui_surf.get_rect(bottomright=(550+(36.5*inventarim), 600))
           display.blit(inventariguiselect_surf, inventariguiselect_surf_rect)
           
           pygame.draw.rect(display, (255, 255, 255), (bird_pos[0]-3, bird_pos[1]-3, 10, 10)) 
           pygame.draw.rect(display, (0,0,0), (0,600, 800, 800))
           
           bloksX=0
           bloksY=0
          
           Renderbloks=False
   #except:
     # Erorr_surf = pygame.image.load(os.path.join(datafiles+'Erorr screan.png'))
      #Erorrcode=("произошла ошибка рендера блока!")
      #Renderbloks=False
      #pygame.mixer.music.load(datafiles+"Among_Us_-_M_M_Piano.mp3")
      #pygame.mixer.music.play(-1)
     # findbloks=0
     # menu=1
     # Erorrsrean=1
     # ErorrScr()

  if(Erorrsrean==1):
     font = pygame.font.Font(None, 20)
     menufon_rect = Erorr_surf.get_rect(bottomright=(800, 600)) 
     display.blit(Erorr_surf, menufon_rect)
     
     textfps = font.render("произошла ошибка игры", 1, (250,0, 0))
     placefps = textfps.get_rect(center=(200, 230))
     display.blit(textfps, placefps)
     
     textfps = font.render("код ошибки: "+Erorrcode, 1, (250,0, 0)) 
     placefps = textfps.get_rect(center=(280, 250))
     display.blit(textfps, placefps)


     
  fps = str(int(clock.get_fps()))
  font = pygame.font.Font(None, 30)
  textfps = font.render("fps: "+fps, 1, (250,0, 0))
  placefps = textfps.get_rect(center=(200, 150))
  display.blit(textfps, placefps)
 
# CURSOR_surf=CURSOR_rect.get_rect(bottomright=())
 #display.blit(CURSOR_rect,pygame.mouse.get_pos()) 
  pygame.display.update()
  if(android==0):
     if(despled==0):
      f = open("config.ini", 'w')
      Config="\nClientID=769246787596058635 \nState="+"game rase none"+" \nDetails="+version+" \nStartTimestamp= \nEndTimestamp= \nLargeImage=game_rase_none"
      f.write(Config)
      despled=1
         



# pygame.display.flip()
# fps = str(int(get_fps()))
# print("fps "+fps)
 

 #menufon_rect = battan_surf.get_rect(bottomright=(184, 406)) 
# display.blit(battan_surf, menufon_rect)
  clock.tick(100)

except:
    print('Erorr code:\n', traceback.format_exc())
    pygame.draw.circle(display,(255,0,0), (400, 500), 50, 30)
    pygame.draw.ellipse(display, (255,0,0), (350, 50, 100, 350))
    pygame.display.update()
    root = Tk()
    root.title("Erorr RedSpark engine")
    mb.showerror(
        "Erorr Code", 
        traceback.format_exc())
    
os.system("TASKKILL /F /IM easyrp.exe")
display.fill((0, 0, 0))
pygame.display.update()
time.sleep(1)

pygame.quit()

    
  # boomos_surf = pygame.image.load('c806f63ed34bf4f0f50a0b90f8dd6d60.png')
  # boomos_rect = boomos_surf.get_rect(bottomright=(1130, 800))
  
    #display.blit(boomos_surf, boomos_rect)
