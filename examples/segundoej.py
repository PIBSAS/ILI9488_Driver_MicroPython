from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font
from time import sleep

lcd = set_display.setting(2)

lcd.fill(Color.BLACK)
lcd.text(
    "Hola",
    0,
    0,
    Color.WHITE,
    font
)
lcd.fill_rect(20, 20, 100, 50, Color.RED)
lcd.fill_rect(50, 100, 150, 80, Color.GREEN)
lcd.fill_rect(10, 220, 300, 100, Color.TORANGE)
lcd.rect(30, 30, 80, 30, Color.TGREEN)
lcd.rect(60, 110, 130, 60, Color.PBLUE)
lcd.rect(20, 230, 280, 80, Color.PRED)
