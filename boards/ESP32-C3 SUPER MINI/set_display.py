from machine import SPI, Pin
from ili9488 import driver

SPI_ID = 1
SPI_BAUDRATE = 40000000

PIN_SCK  = 4 #FSPICLK
PIN_MOSI = 6 #FSPID
PIN_MISO = 5 #FSPIQ Only for touch board 

PIN_CS   = 7 #FSPICS0
PIN_DC   = 3
PIN_RST  = 2
# Backlight (opcional if not 3V3 Pin available)
PIN_BL   = 10

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
