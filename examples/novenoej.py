from ili9488 import driver, Color # Class driver and Color
import set_display # SPI Pins of your board
import fonts.vga1_16x16 as font # Only if you're going to write
import fonts.vga2_8x8 as font2
# Set display connection and rotation 0=0º, 1=90º, 2=180ª, 3=270ª
lcd = set_display.setting(1) 

# Put a background color to the display or will be gray with scanlines
lcd.fill(Color.WHITE)

# Write text on screen
lcd.text("ILI9488", 240-(48*3), 10, Color.RED, font,scale=2)
lcd.text("",20,50,Color.RED,font)
lcd.text("Micropython", 20, 60, Color.BLACK, font,scale=1)
lcd.text("",20,70,Color.RED,font)
lcd.text("https://github.com/PIBSAS/ILI9488_Driver_MicroPython", 5, 90, Color.BLUE, font2,scale=1)
lcd.text("",20,90,Color.RED,font)
lcd.fill_triangle(
    158, 100,
    48, 315,
    268, 315,
    0xD520
)
lcd.fill_circle(300,230,50,Color.PCYAN)
