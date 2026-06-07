from ili9488 import driver, Color
import set_display
from time import sleep

lcd = set_display.setting(2)

for color in Color.ALL:
    lcd.fill(color)
    sleep(0.3)