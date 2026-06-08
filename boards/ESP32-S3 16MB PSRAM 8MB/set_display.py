from machine import SPI, Pin
from ili9488 import driver

SPI_ID = 1
SPI_BAUDRATE = 40000000 # MAX 60Mhz

PIN_SCK  = 12
PIN_MOSI = 11
PIN_MISO = 13 #Optional if you have Touch model

PIN_CS   = 10
PIN_DC   = 6
PIN_RST  = 7
# Backlight (opcional if not 3V3 Pin available)
#PIN_BL   = # 3V3 available

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
    #Pin(PIN_BL, Pin.OUT, value=1)
    
    display = driver(
        spi,
        PIN_CS,
        PIN_DC,
        PIN_RST
    )
    
    display.set_rotation(rotation)
    
    return display
