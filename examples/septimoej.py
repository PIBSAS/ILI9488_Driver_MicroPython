from ili9488 import driver, Color
import set_display
from time import sleep

lcd = set_display.setting(2)

size = 20
gap = 2

cols = lcd.width // (size + gap)

for i, color in enumerate(Color.ALL):

    col = i % cols
    row = i // cols

    x = col * (size + gap)
    y = row * (size + gap)

    lcd.fill_rect(
        x,
        y,
        size,
        size,
        color
    )