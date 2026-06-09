from machine import SPI, Pin
from ili9488 import driver

SPI_ID = 1
SPI_BAUDRATE = 40000000

PIN_CS   = 13 # CD
PIN_MOSI = 15 # SDI(MOSI)
PIN_SCK  = 14 # SCK
PIN_MISO = 12 # SDO(MISO) Only fot touch board

PIN_DC   = 6 # DC/RS
PIN_RST  = 7 # RESET
# Backlight (opcional if not 3V3 Pin available)
PIN_BL   = 22 # LED or use 3V3 from debg pins

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