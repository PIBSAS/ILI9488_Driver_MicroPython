from machine import SPI, Pin, SDCard
from ili9488 import driver
import os

SPI_ID = 1
SPI_BAUDRATE = 40000000

PIN_CS   = 15 # HSPICS0
PIN_MOSI = 13 # HSPID
PIN_SCK  = 14 # HSPICLK
PIN_MISO = 33 # HSPIQ GPIO12 its strapping pin so remap to GPIO 33

PIN_DC   = 16
PIN_RST  = 17
PIN_BL   = 4  # Backlight (opcional if not 3V3 Pin available)

# SD Pins
SD_CS   = 5  # VSPICS0
SD_MOSI = 23 # VSPID
SD_MISO = 19 # VSPIQ
SD_SCK  = 18 # VSPICLK

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
    Pin(PIN_BL, Pin.OUT, value=1)
    
    display = driver(
        spi,
        PIN_CS,
        PIN_DC,
        PIN_RST
    )

def mount_sd():
    sd = SDCard(
        slot=2,
        width=1,
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
    display.set_rotation(rotation)
    
    return display
