import pygame as pg
from Themes import *

class Label:
    def __init__(self, theme = None, **kwargs):
        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.color_bg = thme.get("color")
            self.ftn = thme.get("font")
            self.ftn_color = kwargs.get("font_color") or thme.get("font_color")
        else:
            self.color_bg = kwargs.get("color",(189, 195, 199))
            self.ftn = kwargs.get("font","Franklin Gothic Medium")
            self.ftn_color = kwargs.get("font_color","black")
        
        self.pos_x = kwargs.get("x")
        self.pos_y = kwargs.get("y")
        self.font_size = kwargs.get("font_size")
        self.text = kwargs.get("text")
        self.font = pg.font.SysFont(self.ftn,self.font_size)
        self.textRender = self.font.render(self.text,True,self.ftn_color)

    def update_text(self,value,**kwargs):
        self.text = value
        ftn_color = kwargs.get('font_color') or self.ftn_color
        self.textRender = self.font.render(self.text,True,ftn_color)
        return self.textRender
    
    def Render(self,screen):
        screen.blit(self.textRender, (self.pos_x,self.pos_y))      
class Buttons:
    def __init__(self,pos_X,pos_Y,text = "Button",theme = None, **kwargs):

        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.color_bg = kwargs.get("color") or thme.get("color")
            self.color_hover = kwargs.get("color_hover") or thme.get("color_hover")
            self.color_shadow = thme.get("color_shadow")
            self.color_border = kwargs.get("border_color") or thme.get("border_color")
            self.box_shadow = thme.get("box_shadow")
            self.padding_width = kwargs.get("padding_w") or thme.get("padding_w")
            self.padding_hight = kwargs.get("padding_h") or thme.get("padding_h")
            self.radius = kwargs.get("radius") or thme.get("radius")
            self.border_width = kwargs.get("border_w") or thme.get("border_w")
            self.ftn = kwargs.get("font") or thme.get("font")
            self.ftn_size = kwargs.get("font_size") or thme.get("font_size")
            self.ftn_color = kwargs.get("font_color") or thme.get("font_color")
        else:
            self.color_bg = kwargs.get("color",(180,180,180))
            self.color_hover = kwargs.get("color_hover",(200,200,200))
            self.color_shadow = kwargs.get("color_shadow",(80,80,80))
            self.color_border = kwargs.get("color_border",(70,70,70))
            self.box_shadow = kwargs.get("box_shadow",1)
            self.padding_width = kwargs.get("padding_w",10)
            self.padding_hight = kwargs.get("padding_h",10)
            self.radius = kwargs.get("radius",2)
            self.border_width = kwargs.get("border_w",1)
            self.ftn = kwargs.get("font",'Franklin Gothic Medium')
            self.ftn_size = kwargs.get("font_size",15)
            self.ftn_color = kwargs.get("font_color",(20,20,20))

        self.posX = pos_X
        self.posY = pos_Y

        self.pressed = False
        self.hover = False

        #Para el texto del boton
        self.label = Label(theme ,font = self.ftn,font_size = self.ftn_size, text = text ,font_color= self.ftn_color)
        self.label_render = self.label.update_text(text)

        

        self.color = self.color_bg

        self.resize()

    def check_event(self,event,func = lambda : None,param = None):
       # 1. Actualizamos el hover siempre que el mouse se mueva
        if event.type == pg.MOUSEMOTION:
            self.hover = self.btnBox.collidepoint(event.pos)
        
        # 2. Lógica de colores basada en el hover (fuera del tipo de evento)
        self.color = self.color_hover if self.hover else self.color_bg

        # 3. Lógica de click
        if self.hover:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.pressed = True
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                if self.pressed:
                    if param is not None:
                        func(param)
                    else:
                        func()
                    self.pressed = False
                    return True 
        
        # Si el mouse sale del botón mientras estaba presionado, cancelamos
        if not self.hover and event.type == pg.MOUSEMOTION:
            self.pressed = False
            
        return False

    def resize(self):
        #El ancho y el alto auta-ajustable del boton
        width = max(10,self.label_render.get_width())+self.padding_width 
        height = max(10,self.label_render.get_height())+self.padding_hight

        self.btnBox = pg.Rect(self.posX,self.posY,width,height)
        self.btnbox_shadow = pg.Rect(self.posX+self.box_shadow,self.posY+self.box_shadow,width,height)

        self.textPos = (
            self.btnBox.x + (self.btnBox.w - self.label_render.get_width())//2,
            self.btnBox.y + (self.btnBox.h - self.label_render.get_height())//2
        )    

    def Render(self,screen):
        # Si está presionado, desplazamos el dibujo hacia la posición de la sombra 
        offset = self.box_shadow if self.pressed else 0
        
        # Creamos una copia temporal del rect para el dibujo actual
        draw_rect = self.btnBox.move(offset, offset)

        # 1. Dibujar Sombra (solo si no está presionado para dar efecto de profundidad)
        if self.box_shadow > 0 and not self.pressed:
            pg.draw.rect(screen, self.color_shadow, self.btnbox_shadow, 0, self.radius)
        
        # 2. Cuerpo del Botón
        pg.draw.rect(screen, self.color, draw_rect, 0, self.radius)
        
        # 3. Borde (ahora sí usamos self.color_border que antes faltaba)
        if self.border_width > 0:
            pg.draw.rect(screen, self.color_border, draw_rect, self.border_width, self.radius)
        
        # 4. Texto (ajustado al offset del botón)
        screen.blit(self.label_render, (self.textPos[0] + offset, self.textPos[1] + offset))
class InputText:
    def __init__(self,posX,posY,placeholder = "Escribe Aqui...",theme = None, **kwargs):
        self.thm = theme

        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.color_hover = thme.get("color_txt_on")
            self.colorDesactivo = thme.get("color_txt_off")
            self.backgraud_color = thme.get("color_bg_txt")
            self.radius = thme.get("radius")
            self.place_holder_color = (80,80,80)
        else:
            self.color_hover = kwargs.get("color_active",(9, 132, 227))
            self.colorDesactivo = kwargs.get("color_desactive",(20,20,20))
            self.backgraud_color = kwargs.get("color",(200,200,200))
            self.radius = kwargs.get("radius",2)
            self.place_holder_color = (80,80,80)

        self.placeholder = placeholder
        self.text = ""
        self.ftn = kwargs.get('font','Franklin Gothic Medium') 
        self.ftn_size = kwargs.get('font_size',15)

        

        #colores
        self.color = self.colorDesactivo
        self.text_color = self.colorDesactivo

        self.txtBox = pg.Rect(posX,posY,140,self.ftn_size + 5)
        self.activo = False

        self.label = Label(self.thm ,font = self.ftn,font_size = self.ftn_size, text = self.text ,font_color= self.text_color)

        self.UpdateText()
        
    def UpdateText(self):

        placeText = self.text if self.text or self.activo else self.placeholder
        self.color = self.color_hover if self.activo else self.colorDesactivo

        if placeText == self.placeholder:
            self.text_color = self.place_holder_color
        else:
            self.text_color = self.colorDesactivo

        self.label_render = self.label.update_text(placeText,font_color = self.text_color)

        width = max(100,self.label_render.get_width()+10)
        self.txtBox.w = width

    def Reset(self):
        self.text = ""
        self.UpdateText()

    def check_active(self,event):

        if event.type == pg.MOUSEBUTTONDOWN:
            self.activo = self.txtBox.collidepoint(event.pos)
            
            self.UpdateText()

        if event.type == pg.KEYDOWN and self.activo:
            if event.key == pg.K_RETURN:
                self.activo = False
                self.UpdateText()
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.UpdateText()

    def Render(self,screen):
        pg.draw.rect(screen,self.backgraud_color,(self.txtBox.x,self.txtBox.y,self.txtBox.w,self.txtBox.h), 0,self.radius)
        if self.activo:
            pg.draw.rect(screen,self.color,self.txtBox, 2,self.radius)
        else:
            pg.draw.rect(screen,self.color,self.txtBox, 1,self.radius)
        screen.blit(self.label_render,(self.txtBox.x+5,self.txtBox.y+2))
class RadioButton:
    def __init__(self,posX,posY,text,idselected,radio = 8,theme = None):

        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.color_text = thme.get("font_color")
            self.color_active = thme.get("border_color")
            self.color_desactive = thme.get('color_shadow')
        
        self.id = idselected
        
        self.text =text
        self.font = thme.get("font")

        self.radio = radio
        self.position = (posX,posY)
        self.selected = False
        
        self.label = Label(theme ,font = self.font,font_size = radio*2, text = self.text ,font_color= thme.get("font_color"))
        self.label_render = self.label.update_text(text)

        anchoTotal = (radio*2) +20 +self.label_render.get_width()
        self.rect = pg.Rect(posX-radio,posY-radio,anchoTotal,radio*2)

    def checkClick(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            return False

    def Render(self,screen):
        pg.draw.circle(screen,self.color_desactive,self.position,self.radio,1)
        if self.selected:
            pg.draw.circle(screen,self.color_active,self.position,self.radio,1)
            pg.draw.circle(screen,self.color_active,self.position,self.radio//2)

        centrado = self.position[1] - (self.label_render.get_height() //2)
        screen.blit(self.label_render,(self.position[0]+20,centrado))
class RadioGroup:
    def __init__(self,x,y,listaRB,radio = 10, espacio = None,defaul = 0,theme = None):
        self.botones = []
        self.selected = None
        self.defaul = defaul
        espaciado = espacio if espacio else radio*3

        for rb,(texto,idRB) in enumerate(listaRB):
            posY = y + (rb*espaciado)
            newRB = RadioButton(x,posY,texto,idRB,radio,theme)
            self.botones.append(newRB)

        if self.botones:
            self.botones[defaul].selected = True
            self.selected = self.botones[defaul]

    def checkEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for radiobtn in self.botones:
                if radiobtn.checkClick(event):
                    for rb in self.botones:
                        rb.selected = False
                    radiobtn.selected = True
                    self.selected = radiobtn
                    return True
        return False

    def ObtenerSeleccion(self):
        return self.selected.id if self.selected else None
    
    def Reset(self):
        default = self.defaul
        for idB,btn in enumerate(self.botones):
            if idB == default:
                btn.selected = True
                self.selected = btn
            else:
                btn.selected = False


    def Render(self,screen):
        for rb in self.botones:
            rb.Render(screen)     
class Slider:
    def __init__(self,x,y,width,valMin,valMax,valInit,label = "", theme = None, **kwargs):

        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.color_bar = thme.get("color_bar")
            self.color_circle = thme.get("color")
            self.border = thme.get("border_w")
            self.color_border = thme.get("border_color")
            self.color_shadow = thme.get("color_shadow")
            self.fnt_color = thme.get("font_color")
        else:
            self.color_bar = (100,100,100)
            self.color_circle = "blue"
            self.color_shadow = "red"
            self.fnt_color = "blue"
            self.color_border = "black"
            self.border = 1
            

        self.bar = pg.Rect(x,y,width,5)
        self.radioBar = 10
        self.valMax = valMax
        self.valMin = valMin
        self.valInit = valInit
        self.label = label
        self.font = pg.font.SysFont('arial',16)
        self.ypos = y

        self.set_pos(valInit)

        self.agarrado = False

    def checkEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            centro = pg.Vector2(self.poscircle)
            if centro.distance_squared_to(event.pos) <= self.radioBar**2:
                self.agarrado = True

        if event.type == pg.MOUSEBUTTONUP:
            self.agarrado = False

        if event.type == pg.MOUSEMOTION and self.agarrado:
            self.poscircle[0] = max(self.bar.left,min(event.pos[0],self.bar.right))

    def Reset(self):
        self.poscircle = [self.xpos,self.ypos+2.5]

    def set_pos(self,valor):
        self.valInit = valor
        self.xpos = 10 + (self.valInit - self.valMin) / (self.valMax-self.valMin) * 180
        self.poscircle = [self.xpos,self.ypos+2.5]

    def getPosition(self):
        porcentaje = (self.poscircle[0]-self.bar.x) / self.bar.w
        value = self.valMin + porcentaje * (self.valMax-self.valMin)
        return int(value)

    def Render(self,screen):
        if self.label:
            lbl = self.font.render(f"{self.label}: {self.getPosition()}", True, self.fnt_color)
            screen.blit(lbl, (self.bar.right+10, self.bar.y-10))

        pg.draw.rect(screen,self.color_bar,self.bar,0,6)
        pg.draw.circle(screen,self.color_shadow,(self.poscircle[0]+1,self.poscircle[1]+1),self.radioBar)
        pg.draw.circle(screen,self.color_circle,self.poscircle,self.radioBar)
        pg.draw.circle(screen,self.color_border,self.poscircle,self.radioBar,self.border)
class CheckBox:
    def __init__(self,x,y,text,id,state = False,size = 14, theme = None,**kwargs):
            
        if theme and theme in THEMES:
            thme = THEMES[theme]
            self.color = thme.get("color_shadow")
            self.color_active = thme.get("border_color")
            self.text_color = thme.get("font_color")
            self.font = thme.get("font")
        else:
            self.color = kwargs.get("color_shadow",(40,40,40))
            self.color_active = kwargs.get("border_color",(41, 128, 185))
            self.text_color = kwargs.get("font_color",(10,10,10))
            self.font = kwargs.get("font","Franklin Gothic Medium")
            
        self.text = text
        self.defaultState = state
        self.state = state
        self.size = size
        self.fontsize = 16
        self.radius = kwargs.get('radius',1)

        self.checkbBox = pg.Rect(x,y,size,size)


        self.label = Label(theme ,font = self.font,font_size = size, text = self.text ,font_color= self.text_color)
        self.label_render = self.label.update_text(text)

        anchoTotal = self.checkbBox.w + 5 + self.label_render.get_width()
        self.content = pg.Rect(x,y,anchoTotal,size)

    def checkEvent(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.content.collidepoint(event.pos):
                self.state = not self.state
                return True
        return False

    def Reset(self):
        self.state = self.defaultState

    def Render(self,screen):
        
        if self.state:
            margin = self.size // 4
            check = self.checkbBox.inflate(-margin*2,-margin*2)
            pg.draw.rect(screen,self.color_active,self.checkbBox,1,self.radius)
            pg.draw.rect(screen,self.color_active,check,0,self.radius)
        else:
            pg.draw.rect(screen,self.color,self.checkbBox,1,self.radius)

        screen.blit(self.label_render,(self.checkbBox.right+5,self.checkbBox.y-2))