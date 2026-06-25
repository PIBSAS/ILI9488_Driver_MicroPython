from machine import SPI, Pin, SDCard
from ili9488 import driver
import os

SPI_ID = 1
SPI_BAUDRATE = 40000000 # MAX 60Mhz

PIN_SCK  = 12 # FSPICLK
PIN_MOSI = 11 # FSPID
PIN_MISO = 13 # FSPIQ Optional if you have Touch model
PIN_CS   = 10 # FSPICS0

PIN_DC   = 6
PIN_RST  = 7
# Backlight (opcional if not 3V3 Pin available)
#PIN_BL   = # 3V3 available

# SD Pins
SD_CS   = 5  # GPIO 5
SD_MOSI = 18 # GPIO 18
SD_MISO = 17 # GPIO 17
SD_SCK  = 16 # GPIO 16

MOUNT_POINT = "/sd"

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

def mount_sd():
    sd = SDCard(
        slot=2,
        sck=SD_SCK,
        mosi=SD_MOSI,
        miso=SD_MISO,
        cs=SD_CS
    )
    
    try:
        os.mount(sd, MOUNT_POINT)
    except OSError:
        pass
    
    return sd


def files():
    try:
        return os.listdir(MOUNT_POINT)
    except OSError:
        return []


def umount():
    try:
        os.umount(MOUNT_POINT)
    except OSError:
        pass
