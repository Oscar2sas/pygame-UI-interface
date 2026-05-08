import pygame as pg
import sys
from widgets import *
from Themes import *

#variables de inicio de pygame
pg.init()
screen_size = (400,85)
screen = pg.display.set_mode(screen_size)
fps = pg.time.Clock()
run = True

color = (200,200,200)



#variables y componentes
txt = InputText(70,10,'Nombre...')#Entrada de Texto
txt_label = Label(x=10,y=10,font_size=15,text='Nombre:')#El texto por encima del Input
btn_imprimir = Buttons(270,45,'Imprimir')#Boton para imprimir un mensaje
btn_salir = Buttons(345,45,'Salir',border_color=(255,0,0))#Boton para salir
nombre_label = Label(x=175,y=10,font_size=15,text='')#El Texto que contiene el nombre Introducido en el Input

#Lista con todos los elementos de la ventana
components = [txt,txt_label,btn_imprimir,btn_salir,nombre_label]

#Funciones
def MostrarNombre():
    nombre_label.update_text(f'tu nombre es: {txt.text}')
    return

#bucle principal o "GameLoop"
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 

        #Chequeamos los eventos
        txt.check_active(event)
        btn_imprimir.check_event(event,MostrarNombre)
        if btn_salir.check_event(event):
            run = False

    screen.fill(color)

    #dibijamos los elementos de la lista de a 1
    for com in components:
        com.Render(screen)

    pg.display.flip()
    fps.tick(60)


pg.quit()
sys.exit()