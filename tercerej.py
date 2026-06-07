from machine import SPI, Pin

import config
from ili9488 import ILI9488
import time
BLACK   = 0x0000
WHITE   = 0xFFFF
RED     = 0xF800
GREEN   = 0x07E0
BLUE    = 0x001F
YELLOW  = 0xFFE0
CYAN    = 0x07FF
MAGENTA = 0xF81F

spi = SPI(
    config.SPI_ID,
    baudrate=config.SPI_BAUDRATE,
    polarity=0,
    phase=0,
    sck=Pin(config.PIN_SCK),
    mosi=Pin(config.PIN_MOSI),
    miso=Pin(config.PIN_MISO)
)

tft = ILI9488(
    spi,
    config.PIN_CS,
    config.PIN_DC,
    config.PIN_RST
)
Pin(config.PIN_BL, Pin.OUT, value=1)
tft.set_rotation(2)
"""
lista =(BLACK,WHITE,RED,GREEN,BLUE,YELLOW,CYAN,MAGENTA)
for l in lista:
    tft.fill(l)  # rojo
    time.sleep(1)

tft.text(
    "Hola RP2040 ulala o oh! lala",
    20,
    20,
    WHITE
)
"""
tft.fill(BLACK)
tft.text(
    "Elipse",
    0,
    0,
    RED
)

tft.ellipse(160, 240, 100, 50, YELLOW)
tft.fill_ellipse(
    160,
    240,
    50,
    50,
    MAGENTA
)