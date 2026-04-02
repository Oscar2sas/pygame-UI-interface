# Interfaces de usuario en Pygame

Ya no hace falta que cada vez que crees un proyecto en pygame tengas que reinventar la rueda, con este kit de componentes gráficos podrás crear menús para tus juegos, pantallas de configuraciones o interfaces de aplicaciones sencillas.

Este es un proyecto personal que aún sigue en desarrollo...

Cuenta con:

## Botones

Podrás crear botones con variedad de estilos posibles, todo depende de tu imaginación 

Un pequeño ejemplo:

```python

import pygame as pg
import sys
from Inputs import *

#definimos la funcion
def update_text():
    print('Hola')

pg.init()
ventana = pg.display.set_mode((150, 100))
fps = pg.time.Clock()
running = True        

bkg_color = (44, 62, 80)

#creamos una istancia del boton
button = Buttons(10,10,'Saludar',padding_W=40,padding_H=20,box_shadow=1,colors=(22, 160, 133))

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        #Hacemos que controle eventos y le pasamos una funcion anterior mente creada
        button.check_event(event,func=update_text)
    
    ventana.fill(bkg_color)

    #renderizamos en la ventana principal
    button.Render(ventana)

    pg.display.flip()
    fps.tick(60)

pg.quit()    
sys.exit()


```

### ¿como utilizar la clase Buttons?

Para crear un botón debemos instancia un objeto de la clase Buttons

```python
button = Buttons(pos_x,pos_y,"Texto Label")
```

pero solo con hacer esto lamentablemente aun no funciona, debemos indicarle que se dibuje dentro del bucle while de pygame y tambien debemos colocarlo dentro del bucle de los eventos para darle funcionalidad

```python
import pygame as pg
screen = pg.display.set_mode((640,320))
run = True

#Creamos el boton
button = Buttons(10,20,"Pulsar")

while run:
  for evento in pg.event.get():
      if evento.type == pg.QUIT:
          self.ejecutando = False

          #Hacemos que controle eventos
          button.check_event(event)

  #Renderizamos el boton, debemos pasarle un "screen".
  button.Render(screen)
```
Esto creará un botón con características simples y un efecto de hover

![base](https://github.com/user-attachments/assets/6ed12f0e-2cae-4934-ac38-a6dd74bf6f93)

para que ejecute una función al hacer clic debemos pasársela de la siguiente manera dentro del bucle de eventos

```python
button button.check_event(event,func=update_text)
```


Este botón es la forma más básica y funcional de este botón, si queremos personalizarlo, debemos utilizar sus propiedades, que las describiremos continuación.

### Propiedades de la clase Buttons:

| Propiedad |  Descripción               |
| :-------- | :------------------------- |
| colors | al establecerlo cambiarás el color de fondo del botón |
| font | puedes elegir la fuente dependiendo de las fuentes del sistema |
| font_size | cambiara el tamaño de la fuente |
| font_color | cambiara el color de la fuente |
| padding_W | creara espacios internos de manera vertical|
| padding_H | creará espacios internos de manera horizontal|
| radius | redondea las esquinas del cuadrado |
| box_shadow | generará una sombra atrás del botón y le dará una pequeña animación al hacer click|
| border_w | establece el ancho del borde |
| border_color | establece el color del borde |

la combinación de estas propiedades no dará de resultados botones muy bonitos

![botones2](https://github.com/user-attachments/assets/d0616940-4618-4912-b175-42c3a6047178)


#Entrada de Texto

#Selector circular

#Sliders
