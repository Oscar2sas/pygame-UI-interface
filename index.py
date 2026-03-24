import pygame as pg 
import sys
from Inputs import *

class Juego():
    def __init__(self):
        pg.init()

        self.ventana = pg.display.set_mode((640,320))
        self.fps = pg.time.Clock()
        self. ejecutando = True
        self.bkgColor = ((44, 62, 80))

        self.opcionesRB = [
            RadioButton(20,20,"Opcion A",1),
            RadioButton(20,50,"Opcion B",2),
            RadioButton(20,80,"Opcion C",3),
            RadioButton(20,110,"Opcion D",4),
            RadioButton(20,140,"Opcion E",5),
            RadioButton(20,170,"Opcion F",6),
            RadioButton(20,200,"Opcion G",7)
        ]

        self.opcionesRB[0].selected = True

    def ScreenUpdate(self):

        self.ventana.fill(self.bkgColor)

        for radiobtn in self.opcionesRB:
            radiobtn.Render(self.ventana)

        pg.display.flip()
  

    def ejecutar(self):
        while self.ejecutando:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.ejecutando = False

                for radiobtn in self.opcionesRB:
                    if radiobtn.checkClick(evento):
                        for rb in self.opcionesRB:
                            rb.selected = False
                        radiobtn.selected = True

            self.ScreenUpdate()
            self.fps.tick(60)

        pg.quit()
        sys.exit()

if __name__ == "__main__":
    game = Juego()
    game.ejecutar()