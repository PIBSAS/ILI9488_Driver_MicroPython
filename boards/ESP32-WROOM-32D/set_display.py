from machine import SPI, Pin
from ili9488 import driver

SPI_ID = 1
SPI_BAUDRATE = 40000000

PIN_SCK  = 14
PIN_MOSI = 13
PIN_MISO = 12

PIN_CS   = 15
PIN_DC   = 16
PIN_RST  = 17
# Backlight (opcional if not 3V3 Pin available)
PIN_BL   = 4

def setting(rotation=0):
    spi = SPI(
        SPI_ID,
        baudrate=SPI_BAUDRATE,
        polarity=0,
        phase=0,
        sck=Pin(PIN_SCK),
        mosi=Pin(PIN_MOSI),
        miso=Pin(PIN_MISO)
    )
    Pin(PIN_BL, Pin.OUT, value=1)
    
    display = driver(
        spi,
        PIN_CS,
        PIN_DC,
        PIN_RST
    )
    
    display.set_rotation(rotation)
    
    return display
