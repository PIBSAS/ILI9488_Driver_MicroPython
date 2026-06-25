from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font

lcd = set_display.setting(3)
sd = set_display.mount_sd()

lcd.fill(0x2356)

lcd.text("Hola", 480//2 -16*2, 320//2-8, 0xffff,font)

# vline(x, y, length, color)
lcd.vline(lcd.width//2, 0,lcd.height,Color.YELLOW)

# hline(x, y, length, color)
lcd.hline(0, lcd.height//2,lcd.width,Color.GREEN)


rosa = Color.rgb(245, 77, 142)

lcd.fill_ring(240,160,90,90,50,rosa)