from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font
import time

lcd = set_display.setting(0)
sd = set_display.mount_sd()

archivos = set_display.files()

por_pagina = 30

for inicio in range(0,len(archivos), por_pagina):
    lcd.fill(Color.WHITE)
    fila = 0
    
    for archivo in archivos[inicio:inicio + por_pagina]:
        lcd.text(archivo, 0, fila, Color.BLACK,font, Color.WHITE)
        fila += 18
    
    time.sleep(2)

print(set_display.files())

set_display.umount()

