from ili9488 import driver, Color
import set_display
from time import sleep
import fonts.vga1_16x16 as font

lcd = set_display.setting(0)


lcd.fill(Color.YELLOW)

lcd.text(f"Cronometro:", 50, 90, Color.BLUE, font)
for i in range(60):
    lcd.text(f"{i}", 50+16*12, 90, Color.BLUE, font,Color.BLACK)