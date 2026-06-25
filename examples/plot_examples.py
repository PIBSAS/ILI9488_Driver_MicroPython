from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font
import math, time

lcd = set_display.setting(3)
lcd.fill(0x2378)   # opcional: limpiar fondo de pantalla

x_min = -(lcd.width//2)
x_max = lcd.width//2

SCALE_X = 30
SCALE_Y = 50

lcd.axes(Color.CYAN, Color.WHITE,axis_color=Color.WHITE,scale_x=SCALE_X, scale_y=SCALE_Y)


lcd.plot(2,3,color=Color.WHITE, scale_x=SCALE_X, scale_y=SCALE_Y, thickness=5)

lcd.plot_function(
    lambda x: math.sin(x),
    x_min,
    x_max,
    color=0x07E0,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=2
)
lcd.plot_function(
    lambda x: 2* math.sin(x),
    x_min,
    x_max,
    color=0x780F,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=2
)
lcd.plot_function(
    lambda x: 0.02*x * x,
    x_min,
    x_max,
    color=0xAFE5,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=2
)
lcd.plot_function(
    lambda x: -0.2*x * x,
    x_min,
    x_max,
    color=0x03EF,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=2
)
lcd.plot_function(
    lambda x: x,
    x_min,
    x_max,
    color=0xFEB4,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=3
)
lcd.plot_function(
    lambda x: -x+3,
    x_min,
    x_max,
    color=0xF643,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=3
)
lcd.plot_function(
    lambda x: math.pow(x,3),
    x_min,
    x_max,
    color=0xA100,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=3
)
lcd.plot_function(
    lambda x: -math.pow(x,3),
    x_min,
    x_max,
    color=0x03E9,
    scale_x=SCALE_X,
    scale_y=SCALE_Y,
    thickness=3
)