from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font
from time import sleep

lcd = set_display.setting(2)

lcd.text("Hola RP2040", 0, 0, Color.PRED, font, Color.BLACK,scale=3)
