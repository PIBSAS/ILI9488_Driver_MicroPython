from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font
from time import sleep

lcd = set_display.setting(2)

lcd.fill(Color.BLACK)
lcd.text(
    "Elipse",
    0,
    0,
    Color.RED,
    font
)

lcd.ellipse(160, 240, 100, 50, Color.YELLOW)
lcd.fill_ellipse(
    160,
    240,
    50,
    50,
    Color.MAGENTA
)
