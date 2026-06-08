from ili9488 import driver, Color
import set_display
from time import sleep
import fonts.vga1_16x16 as font

lcd = set_display.setting(2)

lista =(Color.BLACK,Color.WHITE,Color.RED,Color.GREEN,Color.BLUE,Color.YELLOW,Color.CYAN,Color.MAGENTA)

for l in lista:
    lcd.fill(l) 
    sleep(1)

lcd.text(
    "Hola RP2040 ulala o oh! lala",
    20,
    20,
    0xFFFF, # Text color
    font,
    Color.MAROON # Background
)

lcd.text("Sin fondo", 20,60,Color.BLACK,font)

lcd.char(60,90,"O", Color.OLIVE, font, Color.PRED)
