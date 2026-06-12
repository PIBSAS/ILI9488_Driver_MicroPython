from machine import SPI, Pin
from ili9488 import driver

SPI_ID = 2
SPI_BAUDRATE = 40000000

PIN_SCK  = 18
PIN_MOSI = 23
PIN_MISO = 19
PIN_CS   = 5

PIN_DC   = 12
PIN_RST  = 14
PIN_BL   =  27 # Backlight (opcional if not 3V3 Pin available)

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
