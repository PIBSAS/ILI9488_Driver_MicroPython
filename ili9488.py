from machine import Pin, SPI
from time import sleep_ms
from math import sin, cos, pi

TFT_WIDTH = 320
TFT_HEIGHT = 480

# MADCTL

MAD_MY = 0x80
MAD_MX = 0x40
MAD_MV = 0x20
MAD_BGR = 0x08


class driver:

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
        
        # Buffer reutilizable para fill_rect()
        self._fillbuf = bytearray(768)  # 256 píxeles RGB666

        # Caché del último color preparado
        self._last_fill_color = None
        
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

    def _prepare_fillbuf(self, color):

        pixel = self.color565_to_666(color)

        for i in range(256):

            pos = i * 3

            self._fillbuf[pos]     = pixel[0]
            self._fillbuf[pos + 1] = pixel[1]
            self._fillbuf[pos + 2] = pixel[2]

        self._last_fill_color = color

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
    """
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
    """
    def char(
            self,
            x,
            y,
            ch,
            color,
            font,
            bg=None,
            scale=1):

        code = ord(ch)

        if code < font.FIRST or code > font.LAST:
            return

        if bg is not None:

            self.fill_rect(
                x,
                y,
                font.WIDTH * scale,
                font.HEIGHT * scale,
                bg
            )

        bytes_per_row = font.WIDTH // 8

        offset = (
            (code - font.FIRST)
            * font.HEIGHT
            * bytes_per_row
        )

        glyph = font.FONT[
            offset:
            offset + font.HEIGHT * bytes_per_row
        ]

        for row in range(font.HEIGHT):

            row_offset = row * bytes_per_row

            row_data = 0

            for i in range(bytes_per_row):

                row_data = (
                    row_data << 8
                ) | glyph[row_offset + i]

            for col in range(font.WIDTH):

                if row_data & (
                    1 << (font.WIDTH - 1 - col)
                ):
                    if scale == 1:
                        self.pixel(
                            x + col,
                            y + row,
                            color
                        )
                    else:
                        self.fill_rect(
                            x + col * scale,
                            y + row * scale,
                            scale,
                            scale,
                            color
                        )

    # ----------------------
    """
    def text(self, text, x, y, color, bg=None):
        for ch in text:
            self.char(x, y, ch, color, bg)
            x += 16
    """
    def text(
            self,
            text,
            x,
            y,
            color,
            font,
            bg=None,
            scale=1):

        start_x = x

        for ch in text:

            if ch == "\n":

                x = start_x
                y += font.HEIGHT

                continue

            if x + font.WIDTH > self.width:

                x = start_x
                y += font.HEIGHT * scale

            if y + font.HEIGHT * scale > self.height:

                return

            self.char(
                x,
                y,
                ch,
                color,
                font,
                bg,
                scale
            )

            x += font.WIDTH * scale
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

        if color != self._last_fill_color:
            self._prepare_fillbuf(color)

        total = w * h

        self.cs(0)
        self.dc(1)

        while total > 256:
            self.spi.write(self._fillbuf)
            total -= 256

        if total:
            self.spi.write(memoryview(self._fillbuf)[:total * 3])

        self.cs(1)

    # -----------------------
    
    def rect(self, x, y, w, h, color):

        self.fill_rect(x, y, w, 1, color)          # arriba
        self.fill_rect(x, y+h-1, w, 1, color)      # abajo

        self.fill_rect(x, y, 1, h, color)          # izquierda
        self.fill_rect(x+w-1, y, 1, h, color)      # derecha

    # --------------------

    def fast_rect(self, x, y, w, h, color):

        self.hline(x, y, w, color)
        self.hline(x, y + h - 1, w, color)

        self.vline(x, y, h, color)
        self.vline(x + w - 1, y, h, color)
    
    # --------------------
    
    def _plot_ellipse_points(self, xc, yc, x, y, color):

        self.pixel(xc + x, yc + y, color)
        self.pixel(xc - x, yc + y, color)
        self.pixel(xc + x, yc - y, color)
        self.pixel(xc - x, yc - y, color)

    # ---------------------

    def ellipse(self, xc, yc, rx, ry, color):

        x = 0
        y = ry

        rx2 = rx * rx
        ry2 = ry * ry

        tworx2 = 2 * rx2
        twory2 = 2 * ry2

        px = 0
        py = tworx2 * y

        # Región 1
        p = ry2 - (rx2 * ry) + (rx2 // 4)

        while px < py:

            self._plot_ellipse_points(xc, yc, x, y, color)

            x += 1
            px += twory2

            if p < 0:
                p += ry2 + px
            else:
                y -= 1
                py -= tworx2
                p += ry2 + px - py

        # Región 2
        p = (
            ry2 * (x + 0.5) * (x + 0.5)
            + rx2 * (y - 1) * (y - 1)
            - rx2 * ry2
        )

        while y >= 0:

            self._plot_ellipse_points(xc, yc, x, y, color)

            y -= 1
            py -= tworx2

            if p > 0:
                p += rx2 - py
            else:
                x += 1
                px += twory2
                p += rx2 - py + px

    # --------------------

    def fill_ellipse(self, xc, yc, rx, ry, color):

        rx2 = rx * rx
        ry2 = ry * ry

        for y in range(-ry, ry + 1):

            x = int(rx * (1 - (y*y)/ry2) ** 0.5)

            self.fill_rect(
                xc - x,
                yc + y,
                2*x + 1,
                1,
                color
            )

    # --------------------
    """
    def line(self, x0, y0, x1, y1, color):

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1

        err = dx - dy

        while True:

            self.pixel(x0, y0, color)

            if x0 == x1 and y0 == y1:
                break

            e2 = err * 2

            if e2 > -dy:
                err -= dy
                x0 += sx

            if e2 < dx:
                err += dx
                y0 += sy
    """
    # -------------------

    def line(self, x0, y0, x1, y1, color):

        # Horizontal
        if y0 == y1:
            if x1 < x0:
                x0, x1 = x1, x0

            self.hline(x0, y0, x1 - x0 + 1, color)
            return

        # Vertical
        if x0 == x1:
            if y1 < y0:
                y0, y1 = y1, y0

            self.vline(x0, y0, y1 - y0 + 1, color)
            return
        # Bresenham
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1

        err = dx - dy

        while True:

            self.pixel(x0, y0, color)

            if x0 == x1 and y0 == y1:
                break

            e2 = err * 2

            if e2 > -dy:
                err -= dy
                x0 += sx

            if e2 < dx:
                err += dx
                y0 += sy

    # ------------------

    def hline(self, x, y, length, color):

        if length <= 0:
            return

        self.fill_rect(
            x,
            y,
            length,
            1,
            color
        )

    # -------------------

    def vline(self, x, y, length, color):

        if length <= 0:
            return

        self.fill_rect(
            x,
            y,
            1,
            length,
            color
        )

    # --------------------

    def fast_hline(self, x, y, length, color):
        self.hline(x, y, length, color)

    # --------------------

    def fast_vline(self, x, y, length, color):
        self.vline(x, y, length, color)

    # -------------------

    def triangle(self, x1, y1, x2, y2, x3, y3, color):

        self.line(x1, y1, x2, y2, color)
        self.line(x2, y2, x3, y3, color)
        self.line(x3, y3, x1, y1, color)

    # ------------------

    def _swap(a, b):
        return b, a

    # -------------------

    def fill_triangle(self,
                      x1, y1,
                      x2, y2,
                      x3, y3,
                      color):

        # Ordenar por Y
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if y2 > y3:
            x2, x3 = x3, x2
            y2, y3 = y3, y2

        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        def interp(y, xa, ya, xb, yb):

            if ya == yb:
                return xa

            return int(
                xa + (y - ya) *
                (xb - xa) /
                (yb - ya)
            )

        for y in range(y1, y3 + 1):

            if y < y2:

                xa = interp(y, x1, y1, x2, y2)
                xb = interp(y, x1, y1, x3, y3)

            else:

                xa = interp(y, x2, y2, x3, y3)
                xb = interp(y, x1, y1, x3, y3)

            if xa > xb:
                xa, xb = xb, xa

            self.hline(
                xa,
                y,
                xb - xa + 1,
                color
            )

    # ------------------

    def polygon(self, points, color):

        n = len(points)

        if n < 2:
            return

        for i in range(n):

            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]

            self.line(x1, y1, x2, y2, color)

    # --------------------

    def var_polygon(self, *points, color):

        n = len(points)

        if n < 2:
            return

        for i in range(n):

            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]

            self.line(x1, y1, x2, y2, color)

    # -----------------------

    def regular_polygon(self,
                        xc, yc,
                        radius,
                        sides,
                        color,
                        rotation=0):

        points = []
        rotation = rotation * pi / 180
        
        for i in range(sides):
            angle = ((2 * pi * i / sides) - (pi / 2) + rotation)

            x = int(xc + radius * cos(angle))
            y = int(yc + radius * sin(angle))

            points.append((x, y))

        self.polygon(points, color)

    # ------------------

    def fill_regular_polygon(self,
                             xc, yc,
                             radius,
                             sides,
                             color,
                             rotation=0):

        points = []
        
        rotation = rotation * pi / 180

        for i in range(sides):

            angle = ((2 * pi * i / sides) - (pi / 2) + rotation)

            x = int(xc + radius * cos(angle))
            y = int(yc + radius * sin(angle))

            points.append((x, y))

        self.fill_polygon(points, color)

    # --------------------

    def fill_polygon(self, points, color):

        if len(points) < 3:
            return

        ymin = min(y for _, y in points)
        ymax = max(y for _, y in points)

        n = len(points)

        for y in range(ymin, ymax + 1):

            intersections = []

            for i in range(n):

                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n]

                if y1 == y2:
                    continue

                if y < min(y1, y2):
                    continue

                if y >= max(y1, y2):
                    continue

                x = int(
                    x1 + (y - y1) *
                    (x2 - x1) /
                    (y2 - y1)
                )

                intersections.append(x)

            intersections.sort()

            for i in range(0, len(intersections), 2):

                if i + 1 >= len(intersections):
                    break

                x1 = intersections[i]
                x2 = intersections[i + 1]

                self.hline(
                    x1,
                    y,
                    x2 - x1 + 1,
                    color
                )

    # --------------------

    def _plot_circle_points(self, xc, yc, x, y, color):

        self.pixel(xc + x, yc + y, color)
        self.pixel(xc - x, yc + y, color)
        self.pixel(xc + x, yc - y, color)
        self.pixel(xc - x, yc - y, color)

        self.pixel(xc + y, yc + x, color)
        self.pixel(xc - y, yc + x, color)
        self.pixel(xc + y, yc - x, color)
        self.pixel(xc - y, yc - x, color)

    # --------------------

    def circle(self, xc, yc, radius, color):

        x = radius
        y = 0

        decision = 1 - radius

        while x >= y:

            self._plot_circle_points(
                xc,
                yc,
                x,
                y,
                color
            )

            y += 1

            if decision < 0:
                decision += (2 * y) + 1
            else:
                x -= 1
                decision += (2 * (y - x)) + 1

    # ---------------------

    def fill_circle(self, xc, yc, radius, color):

        x = radius
        y = 0

        decision = 1 - radius

        while x >= y:

            self.hline(
                xc - x,
                yc + y,
                2 * x + 1,
                color
            )

            self.hline(
                xc - x,
                yc - y,
                2 * x + 1,
                color
            )

            self.hline(
                xc - y,
                yc + x,
                2 * y + 1,
                color
            )

            self.hline(
                xc - y,
                yc - x,
                2 * y + 1,
                color
            )

            y += 1

            if decision < 0:
                decision += (2 * y) + 1
            else:
                x -= 1
                decision += (2 * (y - x)) + 1

    # -----------------------

    def blit_buffer(self, buffer, x, y, width, height):

        expected = width * height * 3

        if len(buffer) < expected:
            raise ValueError("buffer too small")

        self.set_window(
            x,
            y,
            x + width - 1,
            y + height - 1
        )

        self.cs(0)
        self.dc(1)

        self.spi.write(memoryview(buffer)[:expected])

        self.cs(1)

    # -----------------------

    def show_bmp(self, filename, x=0, y=0):

        with open(filename, "rb") as f:

            # Firma BMP
            if f.read(2) != b"BM":
                raise ValueError("Not a BMP file")

            # Offset donde comienzan los píxeles
            f.seek(10)
            pixel_offset = int.from_bytes(
                f.read(4),
                "little"
            )

            # Ancho
            f.seek(18)
            width = int.from_bytes(
                f.read(4),
                "little"
            )

            # Alto
            height = int.from_bytes(
                f.read(4),
                "little"
            )

            # Bits por pixel
            f.seek(28)
            bpp = int.from_bytes(
                f.read(2),
                "little"
            )

            if bpp != 24:
                raise ValueError(
                    "Only 24-bit BMP supported"
                )

            # Cada fila de BMP está alineada a 4 bytes
            row_size = (width * 3 + 3) & ~3

            # Buffer RGB666 para una fila
            rgb666 = bytearray(width * 3)

            for row in range(height):

                bmp_row = height - 1 - row

                f.seek(
                    pixel_offset +
                    bmp_row * row_size
                )

                data = f.read(row_size)

                for col in range(width):

                    i = col * 3

                    b = data[i]
                    g = data[i + 1]
                    r = data[i + 2]

                    rgb666[i]     = r & 0xFC
                    rgb666[i + 1] = g & 0xFC
                    rgb666[i + 2] = b & 0xFC

                self.blit_buffer(
                    rgb666,
                    x,
                    y + row,
                    width,
                    1
                )

    # -----------------------

    def show_bmp_fit(self, filename):

        with open(filename, "rb") as f:

            if f.read(2) != b"BM":
                raise ValueError("Not a BMP file")

            f.seek(10)
            pixel_offset = int.from_bytes(
                f.read(4),
                "little"
            )

            f.seek(18)
            bmp_w = int.from_bytes(
                f.read(4),
                "little"
            )

            bmp_h = int.from_bytes(
                f.read(4),
                "little"
            )

            f.seek(28)
            bpp = int.from_bytes(
                f.read(2),
                "little"
            )

            if bpp != 24:
                raise ValueError(
                    "Only 24-bit BMP supported"
                )

            screen_w = self.width
            screen_h = self.height

            scale = max(
                bmp_w / screen_w,
                bmp_h / screen_h
            )

            draw_w = int(bmp_w / scale)
            draw_h = int(bmp_h / scale)

            x_offset = (screen_w - draw_w) // 2
            y_offset = (screen_h - draw_h) // 2

            row_size = (bmp_w * 3 + 3) & ~3

            rgb666 = bytearray(draw_w * 3)

            for y in range(draw_h):

                src_y = int(y * scale)

                bmp_row = bmp_h - 1 - src_y

                f.seek(
                    pixel_offset +
                    bmp_row * row_size
                )

                row = f.read(row_size)

                for x in range(draw_w):

                    src_x = int(x * scale)

                    src = src_x * 3
                    dst = x * 3

                    b = row[src]
                    g = row[src + 1]
                    r = row[src + 2]

                    rgb666[dst]     = r & 0xFC
                    rgb666[dst + 1] = g & 0xFC
                    rgb666[dst + 2] = b & 0xFC

                self.blit_buffer(
                    rgb666,
                    x_offset,
                    y_offset + y,
                    draw_w,
                    1
                )

    # -----------------------

    def show_bmp_stretch(self, filename):

        with open(filename, "rb") as f:

            if f.read(2) != b"BM":
                raise ValueError("Not a BMP file")

            f.seek(10)
            pixel_offset = int.from_bytes(
                f.read(4),
                "little"
            )

            f.seek(18)
            bmp_w = int.from_bytes(
                f.read(4),
                "little"
            )

            bmp_h = int.from_bytes(
                f.read(4),
                "little"
            )

            f.seek(28)
            bpp = int.from_bytes(
                f.read(2),
                "little"
            )

            if bpp != 24:
                raise ValueError(
                    "Only 24-bit BMP supported"
                )

            screen_w = self.width
            screen_h = self.height

            row_size = (bmp_w * 3 + 3) & ~3

            rgb666 = bytearray(screen_w * 3)

            for y in range(screen_h):

                src_y = int(
                    y * bmp_h / screen_h
                )

                bmp_row = bmp_h - 1 - src_y

                f.seek(
                    pixel_offset +
                    bmp_row * row_size
                )

                row = f.read(row_size)

                for x in range(screen_w):

                    src_x = int(
                        x * bmp_w / screen_w
                    )

                    src = src_x * 3
                    dst = x * 3

                    b = row[src]
                    g = row[src + 1]
                    r = row[src + 2]

                    rgb666[dst]     = r & 0xFC
                    rgb666[dst + 1] = g & 0xFC
                    rgb666[dst + 2] = b & 0xFC

                self.blit_buffer(
                    rgb666,
                    0,
                    y,
                    screen_w,
                    1
                )

    # -----------------------

    def bmp(self, filename, x=0, y=0, mode=None):

        with open(filename, "rb") as f:

            if f.read(2) != b"BM":
                raise ValueError("Not a BMP file")

            f.seek(10)
            pixel_offset = int.from_bytes(
                f.read(4),
                "little"
            )

            f.seek(18)
            bmp_w = int.from_bytes(
                f.read(4),
                "little"
            )

            f.seek(22)
            bmp_h = int.from_bytes(
                f.read(4),
                "little",
                True
            )

            top_down = bmp_h < 0
            bmp_h = abs(bmp_h)

            f.seek(28)
            bpp = int.from_bytes(
                f.read(2),
                "little"
            )

            if bpp != 24:
                raise ValueError(
                    "Only 24-bit BMP supported"
                )

            screen_w = self.width
            screen_h = self.height

            row_size = (bmp_w * 3 + 3) & ~3

            # -------------------------
            # MODO 1: tamaño original
            # -------------------------

            if mode is None:

                draw_w = min(bmp_w, screen_w - x)
                draw_h = min(bmp_h, screen_h - y)

                rgb666 = bytearray(draw_w * 3)

                for sy in range(draw_h):

                    if top_down:
                        bmp_row = sy
                    else:
                        bmp_row = bmp_h - 1 - sy

                    f.seek(
                        pixel_offset +
                        bmp_row * row_size
                    )

                    row = f.read(row_size)

                    for sx in range(draw_w):

                        src = sx * 3
                        dst = sx * 3

                        b = row[src]
                        g = row[src + 1]
                        r = row[src + 2]

                        rgb666[dst]     = r & 0xFC
                        rgb666[dst + 1] = g & 0xFC
                        rgb666[dst + 2] = b & 0xFC

                    self.blit_buffer(
                        rgb666,
                        x,
                        y + sy,
                        draw_w,
                        1
                    )

                return

            # -------------------------
            # FIT
            # -------------------------

            if mode == "fit":

                scale = max(
                    bmp_w / screen_w,
                    bmp_h / screen_h,
                    1
                )

                draw_w = int(bmp_w / scale)
                draw_h = int(bmp_h / scale)

                x = (screen_w - draw_w) // 2
                y = (screen_h - draw_h) // 2

                rgb666 = bytearray(draw_w * 3)

                for sy in range(draw_h):

                    src_y = int(sy * scale)

                    if top_down:
                        bmp_row = src_y
                    else:
                        bmp_row = bmp_h - 1 - src_y

                    f.seek(
                        pixel_offset +
                        bmp_row * row_size
                    )

                    row = f.read(row_size)

                    for sx in range(draw_w):

                        src_x = int(sx * scale)

                        src = src_x * 3
                        dst = sx * 3

                        b = row[src]
                        g = row[src + 1]
                        r = row[src + 2]

                        rgb666[dst]     = r & 0xFC
                        rgb666[dst + 1] = g & 0xFC
                        rgb666[dst + 2] = b & 0xFC

                    self.blit_buffer(
                        rgb666,
                        x,
                        y + sy,
                        draw_w,
                        1
                    )

                return

            # -------------------------
            # STRETCH
            # -------------------------

            if mode == "stretch":

                rgb666 = bytearray(screen_w * 3)

                for sy in range(screen_h):

                    src_y = int(
                        sy * bmp_h / screen_h
                    )

                    if top_down:
                        bmp_row = src_y
                    else:
                        bmp_row = bmp_h - 1 - src_y

                    f.seek(
                        pixel_offset +
                        bmp_row * row_size
                    )

                    row = f.read(row_size)

                    for sx in range(screen_w):

                        src_x = int(
                            sx * bmp_w / screen_w
                        )

                        src = src_x * 3
                        dst = sx * 3

                        b = row[src]
                        g = row[src + 1]
                        r = row[src + 2]

                        rgb666[dst]     = r & 0xFC
                        rgb666[dst + 1] = g & 0xFC
                        rgb666[dst + 2] = b & 0xFC

                    self.blit_buffer(
                        rgb666,
                        0,
                        sy,
                        screen_w,
                        1
                    )

                return

            raise ValueError(
                "mode must be None, 'fit' or 'stretch'"
            )

    # -----------------------
    
    def fill_ring(self, xc, yc, rx, ry, width, color):
        rx_out = rx + width
        ry_out = ry + width
    
        # Recorremos cada fila de píxeles de la elipse exterior
        for y in range(yc - ry_out, yc + ry_out + 1):
    
            dy = y - yc
    
            # Mitad del ancho de la elipse exterior en esta fila
            value_out = 1 - (dy * dy) / (ry_out * ry_out)
    
            if value_out < 0:
                continue
    
            x_out = int(rx_out * sqrt(value_out))
    
            # Si la fila está dentro de la elipse interior,
            # calculamos su mitad de ancho.
            if -ry <= dy <= ry:
                value_in = 1 - (dy * dy) / (ry * ry)
    
                if value_in >= 0:
                    x_in = int(rx * sqrt(value_in))
    
                    # Segmento izquierdo del aro
                    self.hline(
                        xc - x_out,
                        y,
                        x_out - x_in + 1,
                        color
                    )
    
                    # Segmento derecho del aro
                    self.hline(
                        xc + x_in,
                        y,
                        x_out - x_in + 1,
                        color
                    )
    
            else:
                # Arriba y abajo del hueco interior:
                # toda la fila pertenece al aro.
                self.hline(
                    xc - x_out,
                    y,
                    2 * x_out + 1,
                    color
                )
    # -----------------------
    
    def axes(self, origin_color=0xFFFF, tick_color=0xFFFF, axis_color=0xFFFF, center_dot=True, scale_x=10, scale_y=10, tick_size=6):
        """
        Dibuja ejes cartesianos completos (X e Y) centrados en pantalla.
        Funciona con cualquier rotación porque usa lcd.width y lcd.height.

        origin_color: color del origen de coordenadas
        tick_color: color general de los ticks
        axis_color: color de los ejes principales
        center_dot: marca el origen
        scale_x: Unidad matematica 1 = 10 px
        scale_y: Unidad matematica 1 = 10 px
        tick_size: Tamaño del tick 6px
        """
    
        w = self.width
        h = self.height

        cx = w // 2
        cy = h // 2

        # Ejes principales
        self.hline(0, cy, w, axis_color)
        self.vline(cx, 0, h, axis_color)

        # Origen
        if center_dot:
            self.fill_circle(cx, cy, 2, origin_color)

        # Ticks del eje X:
        # cada tick está separado scale_x píxeles,
        # o sea, representa 1 unidad en X.
        x = cx + scale_x
        while x < w:
            self.vline(x, cy - tick_size//2, tick_size, tick_color)
            x += scale_x

        x = cx - scale_x
        while x >= 0:
            self.vline(x, cy - tick_size//2, tick_size, tick_color)
            x -= scale_x

        # Ticks del eje Y:
        # cada tick está separado scale_y píxeles,
        # o sea, representa 1 unidad en Y.
        y = cy + scale_y
        while y < h:
            self.hline(cx - tick_size//2, y, tick_size, tick_color)
            y += scale_y

        y = cy - scale_y
        while y >= 0:
            self.hline(cx - tick_size//2, y, tick_size, tick_color)
            y -= scale_y

    # -----------------------

    def _to_screen(self, x, y, scale_x=10, scale_y=10):
        """
        Convierte coordenadas cartesianas a píxeles de pantalla.

        Por defecto:
            1 unidad matemática = 10 píxeles.
        """
        cx = self.width // 2
        cy = self.height // 2

        sx = cx + int(x * scale_x)
        sy = cy - int(y * scale_y)

        return sx, sy

    # ----------------------

    def _thick_pixel(self, x, y, color, thickness=1):
        """
        Dibuja un punto cuadrado centrado en (x, y).
        thickness=1 dibuja exactamente un píxel.
        """
        if thickness <= 1:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.pixel(x, y, color)
            return

        radius = thickness // 2

        self.fill_circle(x ,y, radius, color)

    # -----------------------
    
    def _thick_line(self, x0, y0, x1, y1, color, thickness=1):
        """
        Dibuja una línea de grosor configurable.

        thickness=1 usa line() normal.
        Para grosores mayores dibuja líneas desplazadas.
        """
        if thickness <= 1:
            self.line(x0, y0, x1, y1, color)
            return

        half = thickness // 2

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        # Línea más horizontal: desplazamos verticalmente.
        if dx >= dy:
            for offset in range(-half, half + 1):
                self.line(x0, y0 + offset, x1, y1 + offset, color)

        # Línea más vertical: desplazamos horizontalmente.
        else:
            for offset in range(-half, half + 1):
                self.line(x0 + offset, y0, x1 + offset, y1, color)
    
    # ----------------------

    def plot(self, x, y, color=0xFFFF, scale_x=10, scale_y=10, thickness=1):
        """
        Dibuja un punto en coordenadas cartesianas.

        Ejemplo:
            lcd.plot(2, 3)

        dibuja el punto (2, 3), que por defecto queda:
            20 px a la derecha
            30 px arriba
        del origen.
        """
        sx, sy = self._to_screen(x, y, scale_x, scale_y)

        if 0 <= sx < self.width and 0 <= sy < self.height:
            self._thick_pixel(sx, sy, color, thickness)

    # -----------------------

    def plot_function(self, func, x_min, x_max, step=0.05, color=0xFFFF, scale_x=10, scale_y=10, thickness=1):
        """
        Grafica y = func(x).

        scale_x y scale_y indican cuántos píxeles representa
        una unidad matemática en cada eje.
        """

        prev = None
        x = x_min

        while x <= x_max:

            try:
                y = func(x)
            except Exception:
                # Si la función falla en un punto, por ejemplo 1 / 0,
                # no conectamos la parte anterior con la siguiente.
                prev = None
                x += step
                continue

            sx, sy = self._to_screen(x, y, scale_x, scale_y)

            # Solo dibujamos y conectamos puntos visibles.
            if 0 <= sx < self.width and 0 <= sy < self.height:
                if prev is not None:
                    self._thick_line(prev[0], prev[1], sx, sy, color, thickness)

                prev = (sx, sy)
            else:
                prev = None

            x += step   

# -----------------------

class Color:
    # Colores RGB565
    BLACK   = 0x0000
    NAVY    = 0x000F
    DARKGREEN = 0x03E0
    DARKCYAN  = 0x03EF
    MAROON    = 0x7800
    PURPLE    = 0x780F
    OLIVE     = 0x7BE0
    LIGHTGREY = 0xC618
    DARKGREY  = 0x7BEF

    BLUE    = 0x001F
    GREEN   = 0x07E0
    CYAN    = 0x07FF
    RED     = 0xF800
    MAGENTA = 0xF81F
    YELLOW  = 0xFFE0
    WHITE   = 0xFFFF

    ORANGE  = 0xFD20
    GREENYELLOW = 0xAFE5
    PINK    = 0xFE3F
    # PASTEL
    PRED = 0xFD75
    PORANGE = 0xFEB4
    PYELLOW = 0xFFF6
    PGREEN = 0xCFF7
    PCYAN = 0x9FBF
    PBLUE = 0x9E1F
    PPURPLE = 0xBD9F
    
    #Tropical sunrise
    TRED = 0xD945
    TORANGE = 0xF384
    TYELLOW = 0xF643
    TGREEN = 0x7568
    TDARKGREEN = 0x03E9
    
    ALL = (
        BLACK,
        NAVY,
        DARKGREEN,
        DARKCYAN,
        MAROON,
        PURPLE,
        OLIVE,
        LIGHTGREY,
        DARKGREY,
        BLUE,
        GREEN,
        CYAN,
        RED,
        MAGENTA,
        YELLOW,
        WHITE,
        ORANGE,
        GREENYELLOW,
        PINK,
        PRED,
        PORANGE,
        PYELLOW,
        PGREEN,
        PCYAN,
        PBLUE,
        PPURPLE,
        TRED,
        TORANGE,
        TYELLOW,
        TGREEN,
        TDARKGREEN
    )
    
    @staticmethod
    def rgb(r, g, b):
        return (
            ((r & 0xF8) << 8) |
            ((g & 0xFC) << 3) |
            (b >> 3)
        )
