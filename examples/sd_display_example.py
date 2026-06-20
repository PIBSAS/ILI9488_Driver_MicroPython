from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font

lcd = set_display.setting(0)
sd = set_display.mount_sd()

fila = 0
for archivo in set_display.files():
    lcd.text(archivo, 0, fila, Color.WHITE,font, Color.RED)
    fila += 18

print(set_display.files())

set_display.umount()