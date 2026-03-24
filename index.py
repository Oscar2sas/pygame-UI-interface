import pygame as pg
import sys
from Inputs import Buttons, InputText, RadioGroup

class EjemploIntegracion:
    def __init__(self):
        pg.init()
        self.ventana = pg.display.set_mode((800, 600))
        pg.display.set_caption("Catálogo de Componentes UI")
        self.fps = pg.time.Clock()
        self.ejecutando = True
        
        # Colores y fuentes
        self.bkgColor = (44, 62, 80)
        self.fuente_titulos = pg.font.SysFont("arial", 24, bold=True)

        # 1. Ejemplo de RadioGroup (Dificultad)
        opciones_diff = [("Fácil", "easy"), ("Normal", "normal"), ("Experto", "hard")]
        self.grupo_dif = RadioGroup(50, 80, opciones_diff, radio=12, defaul=1)

        # 2. Ejemplo de InputText (Nombre de Usuario)
        self.input_nombre = InputText(50, 250, fontSize=25, placeholder="Tu nombre aquí...")

        # 3. Ejemplo de Buttons (Acciones)
        self.btn_guardar = Buttons(50, 350, text="Guardar Configuración", paddingW=20, radius=8)
        self.btn_salir = Buttons(50, 420, text="Salir", colorDC=(192, 57, 43), colorAc=(231, 76, 60), radius=8)

        # Estado para mostrar resultados
        self.mensaje_consola = "Esperando acción..."

    def manejar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.ejecutando = False

            # Eventos del RadioGroup
            if self.grupo_dif.checkEvent(evento):
                self.mensaje_consola = f"Dificultad cambiada a: {self.grupo_dif.ObtenerSeleccion()}"

            # Eventos del InputText
            # La función lambda se ejecuta al presionar ENTER
            self.input_nombre.check_active(evento, func=lambda: print(f"Nombre ingresado: {self.input_nombre.text}"))

            # Eventos de los Botones
            self.btn_guardar.Selecction(evento, func=self.accion_guardar)
            self.btn_salir.Selecction(evento, func=sys.exit)

    def accion_guardar(self):
        nombre = self.input_nombre.text if self.input_nombre.text else "Anónimo"
        dificultad = self.grupo_dif.ObtenerSeleccion()
        self.mensaje_consola = f"Guardado: {nombre} | Nivel: {dificultad}"
        print(self.mensaje_consola)

    def dibujar(self):
        self.ventana.fill(self.bkgColor)

        # Dibujar etiquetas de ayuda
        lbl_rb = self.fuente_titulos.render("Seleccione Dificultad:", True, "white")
        self.ventana.blit(lbl_rb, (50, 40))

        lbl_it = self.fuente_titulos.render("Ingrese Nombre:", True, "white")
        self.ventana.blit(lbl_it, (50, 210))

        # Renderizar componentes
        self.grupo_dif.Render(self.ventana)
        self.input_nombre.Render(self.ventana)
        self.btn_guardar.Render(self.ventana)
        self.btn_salir.Render(self.ventana)

        # Mostrar estado actual en pantalla
        txt_estado = pg.font.SysFont("arial", 18).render(self.mensaje_consola, True, (241, 196, 15))
        self.ventana.blit(txt_estado, (50, 520))

        pg.display.flip()

    def ejecutar(self):
        while self.ejecutando:
            self.manejar_eventos()
            self.dibujar()
            self.fps.tick(60)
        pg.quit()

if __name__ == "__main__":
    EjemploIntegracion().ejecutar()