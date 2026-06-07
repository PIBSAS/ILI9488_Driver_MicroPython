from ili9488 import driver, Color
import set_display
from time import sleep

lcd = set_display.setting(2)

lcd.fill(Color.rgb(255,128,64))
sleep(.5)
lcd.fill(Color.rgb(234,0,235))
sleep(.5)
lcd.fill(Color.rgb(34,230,0))