

def set_color(list_color,value):
        new_colors = tuple(max(0,min(255,color+value)) for color in list_color)
        return new_colors

THEMES = {
    "dark" : {
        #estilos para botones
        "color" : (45, 52, 54),
        "color_hover":set_color((45, 52, 54),10),
        "color_shadow": (set_color((45, 52, 54),-20)),
        "border_color" : (41, 128, 185),
        "box_shadow" : 1,
        "padding_w" : 20,
        "padding_h" : 20,
        "radius" : 4,
        "border_w" : 1,
        "font" : "Arial",
        "font_size" : 15,
        "font_color" : "white",
        #estilos para entrada de texto
        "color_bg_txt" : (set_color((45, 52, 54),-10)),
        "color_txt_off": (set_color((45, 52, 54),120)),
        "color_txt_on": (41, 128, 185),
        #estilos para los slider(deslizadores)
        "color_bar" : ((set_color((45, 52, 54),-20)))
    },
    "light" : {
        #estilos para botones
        "color" : (245, 246, 250),
        "color_hover":set_color((245, 246, 250),-10),
        "color_shadow": (set_color((245, 246, 250),-40)),
        "border_color" : (41, 128, 185),
        "box_shadow" : 2,
        "padding_w" : 20,
        "padding_h" : 20,
        "radius" : 8,
        "border_w" : 1,
        "font" : "Arial",
        "font_size" : 12,
        "font_color" : (47, 54, 64),
        #estilos para entrada de texto
        "color_bg_txt" : (set_color((245, 246, 250),-20)),
        "color_txt_off": (set_color((245, 246, 250),-140)),
        "color_txt_on": (41, 128, 185),
        #estilos para los slider(deslizadores)
        "color_bar" : ((set_color((245, 246, 250),-50)))
    },
    "neon" : {
        "color" : (30,30,30),
        "color_hover":set_color((30,30,30),10),
        "color_shadow": (0,0,0),
        "border_color" : (41, 128, 185),
        "box_shadow" : 0,
        "padding_w" : 20,
        "padding_h" : 20,
        "radius" : 2,
        "border_w" : 1,
        "font" : "Arial",
        "font_size" : 12,
        "font_color" : (41, 128, 185),
        #estilos para entrada de texto
        "color_bg_txt" : (30,30,30),
        "color_txt_off": (set_color((245, 246, 250),-140)),
        "color_txt_on": (41, 128, 185),
        #estilos para los slider(deslizadores)
        "color_bar" : (set_color((41, 128, 185),-20))
    },
    "pink" : {
        "color" : (248, 165, 194),
        "color_hover":set_color((248, 165, 194),10),
        "color_shadow": (set_color(((248, 165, 194)),-30)),
        "border_color" : (set_color(((248, 165, 194)),-40)),
        "box_shadow" : 1,
        "padding_w" : 30,
        "padding_h" : 20,
        "radius" : 20,
        "border_w" : 2,
        "font" : "Arial",
        "font_size" : 12,
        "font_color" : (48, 57, 82),
        #estilos para entrada de texto
        "color_bg_txt" : (set_color((248, 165, 194),-10)),
        "color_txt_off": (set_color((248, 165, 194),-80)),
        "color_txt_on": ((set_color((248, 165, 194),-100))),
        #estilos para los slider(deslizadores)
        "color_bar" : ((set_color((248, 165, 194),-30)))
    }
}