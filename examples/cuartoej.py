from ili9488 import driver, Color
import set_display
from time import sleep

lcd = set_display.setting(2)

# Diagonal
lcd.line(0, 0, 319, 479, Color.ORANGE)

# Otra diagonal
lcd.line(319, 0, 0, 479, Color.LIGHTGREY)

# Horizontal
lcd.line(20, 100, 300, 100, Color.GREEN)
lcd.hline(50, 150, 200, Color.PURPLE)
lcd.fast_hline(60, 160, 230, Color.RED)

# Vertical
lcd.line(160, 20, 160, 460, Color.DARKGREEN)
lcd.vline(120, 20, 180, Color.DARKCYAN)
lcd.fast_vline(110, 10, 230, Color.MAROON)

# Recatngulo usando vline,hline
lcd.fast_rect(20, 80, 80, 300, Color.MAGENTA)

# Triangulo
lcd.triangle(
    160, 50,
    50, 250,
    270, 250,
    Color.BLUE
)

# Triangulo solido
lcd.fill_triangle(
    158, 48,
    48, 248,
    268, 248,
    0xD520
)

# Poiligo
hexagono = [
    (160, 50),
    (220, 90),
    (220, 170),
    (160, 210),
    (100, 170),
    (100, 90)
]

lcd.polygon(hexagono, 0xFFFF)

# Poligono con argumentos variables
lcd.var_polygon(
    (260, 50),
    (320, 90),
    (320, 170),
    (260, 210),
    (120, 170),
    (120, 90),
    color=0x3FFF
)

# Poligonos regulares
# Triángulo equilátero 0º por defecto
lcd.regular_polygon(
    160, 120,
    80,
    3,
    0xF800
)

# Pentágono
lcd.regular_polygon(
    160, 240,
    80,
    5,
    0x07E0
)

# Hexágono
lcd.regular_polygon(
    160, 360,
    80,
    6,
    0x001F
)

# Poligono regular solido girado 0º por defecto
lcd.fill_regular_polygon(
    160,
    120,
    80,
    5,
    0xF800
)

# Poligono regular solido girado 36º
lcd.fill_regular_polygon(
    160,
    240,
    80,
    6,
    0x07E0,
    rotation=36
)

# Poligono regular solido girado 22.5º
lcd.fill_regular_polygon(
    160,
    360,
    80,
    8,
    0x001F,
    rotation=22.5
)

# Circulo
lcd.circle(
    160,
    240,
    100,
    0xFFFF
)
# Circulo solido
lcd.fill_circle(
    160,
    240,
    80,
    Color.NAVY
)

lcd.show_bmp("bmp-24-bit.bmp", 0,0)
lcd.fill(Color.WHITE)
lcd.show_bmp_fit("bmp-24-bit.bmp")
lcd.fill(Color.WHITE)
lcd.show_bmp_stretch("bmp-24-bit.bmp")
lcd.fill(Color.PINK)

# BMP con modos 1:1 no se pasa parametro
lcd.bmp("bmp-24-bit.bmp")
lcd.fill(Color.MAGENTA)

#BMP con modo fit
lcd.bmp("bmp-24-bit.bmp", mode="fit")
lcd.fill(Color.YELLOW)

#BMP con modo stretch
lcd.bmp("bmp-24-bit.bmp", mode="stretch")