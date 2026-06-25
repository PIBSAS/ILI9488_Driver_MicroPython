from machine import SPI, Pin, SDCard
from ili9488 import driver
import os

SPI_ID = 2
SPI_BAUDRATE = 40000000

PIN_CS   = 5  # VSPICS0
PIN_MOSI = 23 # VSPID
PIN_SCK  = 18 # VSPICLK
PIN_MISO = 19 # VSPIQ

PIN_DC   = 25
PIN_RST  = 26
PIN_BL   = 27 # Backlight (opcional if not 3V3 Pin available)

# SD Pins
SD_CS   = 15 # HSPICS0
SD_MOSI = 13 # HSPID
SD_MISO = 33 # HSPIQ GPIO12 its strapping pin so remap to GPIO 33
SD_SCK  = 14 # HSPICLK

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
    
    display.set_rotation(rotation)
    
    return display

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
