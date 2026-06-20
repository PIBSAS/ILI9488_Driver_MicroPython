from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font

lcd = set_display.setting(0)
sd = set_display.mount_sd()

archivos = set_display.files()

for i, archivo in enumerate(archivos[:30]):
    lcd.text(archivo, 0, i*16, Color.WHITE,font, Color.RED)

print(set_display.files())

set_display.umount()
