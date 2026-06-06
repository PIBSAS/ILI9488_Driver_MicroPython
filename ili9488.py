from machine import Pin, SPI
from time import sleep_ms

TFT_WIDTH = 320
TFT_HEIGHT = 480

# MADCTL

MAD_MY = 0x80
MAD_MX = 0x40
MAD_MV = 0x20
MAD_BGR = 0x08


class ILI9488:

    def __init__(
            self,
            spi,
            cs,
            dc,
            rst):

        self.spi = spi

        self.cs = Pin(cs, Pin.OUT)
        self.dc = Pin(dc, Pin.OUT)
        self.rst = Pin(rst, Pin.OUT)

        self.width = TFT_WIDTH
        self.height = TFT_HEIGHT

        self.reset()
        self.init_display()

    # -------------------------

    def reset(self):

        self.rst(1)
        sleep_ms(5)

        self.rst(0)
        sleep_ms(20)

        self.rst(1)
        sleep_ms(150)

    # -------------------------

    def write_cmd(self, cmd):

        self.cs(0)
        self.dc(0)

        self.spi.write(bytearray([cmd]))

        self.cs(1)

    # -------------------------

    def write_data(self, data):

        self.cs(0)
        self.dc(1)

        if isinstance(data, int):
            self.spi.write(bytearray([data]))
        else:
            self.spi.write(data)

        self.cs(1)

    # -------------------------

    def write_reg(self, cmd, data):

        self.write_cmd(cmd)
        self.write_data(bytearray(data))

    # -------------------------

    def init_display(self):

        # Positive Gamma

        self.write_reg(0xE0, [
            0x00,0x03,0x09,0x08,0x16,
            0x0A,0x3F,0x78,0x4C,0x09,
            0x0A,0x08,0x16,0x1A,0x0F
        ])

        # Negative Gamma

        self.write_reg(0xE1, [
            0x00,0x16,0x19,0x03,0x0F,
            0x05,0x32,0x45,0x46,0x04,
            0x0E,0x0D,0x35,0x37,0x0F
        ])

        self.write_reg(0xC0, [0x17,0x15])
        self.write_reg(0xC1, [0x41])
        self.write_reg(0xC5, [0x00,0x12,0x80])

        self.write_reg(0x36, [0x48])

        # SPI => RGB666

        self.write_reg(0x3A, [0x66])

        self.write_reg(0xB0, [0x00])
        self.write_reg(0xB1, [0xA0])
        self.write_reg(0xB4, [0x02])

        self.write_reg(0xB6, [
            0x02,
            0x02,
            0x3B
        ])

        self.write_reg(0xB7, [0xC6])

        self.write_reg(0xF7, [
            0xA9,
            0x51,
            0x2C,
            0x82
        ])

        self.write_cmd(0x11)
        sleep_ms(120)

        self.write_cmd(0x29)
        sleep_ms(25)

    # -------------------------

    def set_rotation(self, rotation):

        rotation &= 7

        self.write_cmd(0x36)

        if rotation == 0:
            self.write_data(MAD_MX | MAD_BGR)
            self.width = 320
            self.height = 480

        elif rotation == 1:
            self.write_data(MAD_MV | MAD_BGR)
            self.width = 480
            self.height = 320

        elif rotation == 2:
            self.write_data(MAD_MY | MAD_BGR)
            self.width = 320
            self.height = 480

        elif rotation == 3:
            self.write_data(
                MAD_MX | MAD_MY | MAD_MV | MAD_BGR
            )
            self.width = 480
            self.height = 320

    # -------------------------

    def set_window(self, x0, y0, x1, y1):

        self.write_cmd(0x2A)

        self.write_data(bytearray([
            x0 >> 8,
            x0 & 0xFF,
            x1 >> 8,
            x1 & 0xFF
        ]))

        self.write_cmd(0x2B)

        self.write_data(bytearray([
            y0 >> 8,
            y0 & 0xFF,
            y1 >> 8,
            y1 & 0xFF
        ]))

        self.write_cmd(0x2C)

    # -------------------------

    @staticmethod
    def color565_to_666(color):

        r = (color >> 11) & 0x1F
        g = (color >> 5) & 0x3F
        b = color & 0x1F

        r = (r * 255) // 31
        g = (g * 255) // 63
        b = (b * 255) // 31

        return bytes([
            r & 0xFC,
            g & 0xFC,
            b & 0xFC
        ])

    # -------------------------
    """
    def fill(self, color):

        self.set_window(
            0,
            0,
            self.width - 1,
            self.height - 1
        )

        pixel = self.color565_to_666(color)

        self.cs(0)
        self.dc(1)

        chunk = pixel * 256

        total = self.width * self.height

        while total > 256:

            self.spi.write(chunk)
            total -= 256

        self.spi.write(pixel * total)

        self.cs(1)
    """
    def fill(self, color):
        self.fill_rect(
            0,
            0,
            self.width,
            self.height,
            color
        )
    # -------------------------

    def pixel(self, x, y, color):

        self.set_window(x, y, x, y)

        self.write_data(
            self.color565_to_666(color)
        )
    
    # --------------------------
    
    def char(self, x, y, ch, color, bg=None):

        import vga1_16x16 as font

        code = ord(ch)

        if code < font.FIRST or code > font.LAST:
            return

        offset = (code - font.FIRST) * 32
        glyph = font.FONT[offset:offset + 32]

        for row in range(16):

            row_data = (glyph[row * 2] << 8) | glyph[row * 2 + 1]

            for col in range(16):

                if row_data & (0x8000 >> col):
                    self.pixel(x + col, y + row, color)

                elif bg is not None:
                    self.pixel(x + col, y + row, bg)
    
    # ----------------------
    
    def text(self, text, x, y, color, bg=None):
        for ch in text:
            self.char(x, y, ch, color, bg)
            x += 16
    
    # ----------------------
    
    def fill_rect(self, x, y, w, h, color):

        if w <= 0 or h <= 0:
            return

        self.set_window(
            x,
            y,
            x + w - 1,
            y + h - 1
        )

        pixel = self.color565_to_666(color)

        self.cs(0)
        self.dc(1)

        chunk = pixel * 256

        total = w * h

        while total > 256:
            self.spi.write(chunk)
            total -= 256

        self.spi.write(pixel * total)

        self.cs(1)

    # -----------------------
    
    def rect(self, x, y, w, h, color):

        self.fill_rect(x, y, w, 1, color)          # arriba
        self.fill_rect(x, y+h-1, w, 1, color)      # abajo

        self.fill_rect(x, y, 1, h, color)          # izquierda
        self.fill_rect(x+w-1, y, 1, h, color)      # derecha
