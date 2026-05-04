# 🎮 Pygame UI Interface Kit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-Latest-green.svg)

Una librería modular y ligera diseñada bajo el paradigma de **Programación Orientada a Objetos (POO)** para simplificar la creación de interfaces gráficas (GUI) en Pygame.

---

## 📸 Demo
<img width="672" height="453" alt="image" src="https://github.com/user-attachments/assets/f71aacd7-0f35-49f0-ab41-8953b0469cbf" />

---

## ✨ Elementos Principales

*  **Botones Dinámicos:** Con estados de *hover* automáticos y efectos de sombreado.
*  **Inputs de Texto:** Manejo de enfoque (focus) y captura de eventos de teclado.
*  **Radio Groups:** Sistema de selección única para menús y opciones.
*  **CheckBoxs** Meanejo de estado encendido apagado
*  **Sliders** Control de Valores mediante un deslizador
*  **Labes** Etiquetas de texto actualisables 

---

## 🚀 Instalación y Uso Rápido

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Oscar2sas/pygame-UI-interface.git
   ```

2. **Ejemplo básico de implementación:**

```python
import pygame as pg
import sys
from widgets import *
from Themes import *

pg.init()
screen_size = (400,130)
screen = pg.display.set_mode(screen_size)
fps = pg.time.Clock()
run = True

theme = 'dark'
bg_color = THEMES[theme].get('color')

#variables y componentes
txt = InputText(60,10,'Nombre...',theme=theme)
txt_label = Label(x=10,y=10,font_size=15,text='Nombre:',theme=theme)
btn_aceptar = Buttons(280,45,'Imprimir',theme=theme)
btn_cancelar = Buttons(350,45,'Salir',theme=theme,border_color=(255,0,0))
check_fps = CheckBox(10,90,'Mostrar FPS: ',1,theme=theme)
fps_label = Label(x=10,y=110,font_size=15,text='',theme=theme)
nombre_label = Label(x=165,y=10,font_size=15,text='',theme=theme)

#Lista con todos los elementos de la ventana
components = [txt,txt_label,btn_aceptar,btn_cancelar,check_fps,fps_label,nombre_label]

#Funciones
def MostrarFPS():
    global fps_label,fps

    fps_label.update_text(str(int(fps.get_fps())))
    return

def MostrarNombre():
    nombre_label.update_text(f'tu nombre es: {txt.text}')
    return

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 

        #Chequeamos los eventos
        txt.check_active(event)
        btn_aceptar.check_event(event,MostrarNombre)
        if btn_cancelar.check_event(event):
            run = False
        check_fps.checkEvent(event)

    screen.fill(bg_color)

    #dibijamos los elementos de la lista de a 1
    for com in components:
        com.Render(screen)

    #verificamo el estado del check y segun eso mostramos o no los fps
    if check_fps.state == True:
        MostrarFPS()
    else:
        fps_label.update_text('')


    pg.display.flip()
    fps.tick(60)


pg.quit()
sys.exit()
```

---

## 📖 Documentación de Componentes

### `Button`
La clase base para interactividad táctil/ratón.
- **Parámetros:** `x`, `y`, `width`, `height`, `text`, `color`.
- **Métodos clave:** `draw(surface)`, `check_click(pos)`.

### `InputText`
Cuadro de entrada para capturar texto del usuario.
- **Estado:** Maneja automáticamente el estado de "enfocado" al hacer click.

### `RadioGroup`
Contenedor para múltiples opciones donde solo una puede estar activa.

---

## 📂 Estructura del Proyecto

```text
├── Inputs.py      # Núcleo de la librería (Clases de componentes)
├── index.py       # Archivo de demostración y pruebas
├── LICENSE        # Licencia MIT
└── README.md      # Documentación del proyecto
```

---

## 🛠️ Próximas Mejoras (Roadmap)
- [ ] Implementación de Sliders (Deslizadores).
- [ ] Checkboxes con estados booleanos.
- [ ] Soporte para temas (Dark/Light mode).

---

## 📄 Licencia
Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---
**Desarrollado por [Oscar2sas](https://github.com/Oscar2sas)**
