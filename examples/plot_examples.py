from ili9488 import driver, Color
import set_display
import fonts.vga1_16x16 as font
import math, time

lcd = set_display.setting(3)
lcd.fill(0x2378)   # opcional: limpiar fondo de pantalla

x_min = -(lcd.width//2)
x_max = lcd.width//2

lcd.set_scale(10, 10)

lcd.axes(Color.CYAN, Color.WHITE,axis_color=Color.WHITE)
A = (0, 0)
B = (6, 8)

lcd.line_points(A, B,thickness=2)
lcd.plot(6,8,thickness=8)

lcd.line_points((2,5), (3,2), thickness=3)
E=(3,4)
D=(-2,-3)
lcd.line_points(E, D)
lcd.plot(2,3,color=Color.WHITE, thickness=5)
lcd.plot_function(lambda x: x*x*x*x -3*x*x + 2, x_min,x_max+1, color=Color.YELLOW,thickness=3)
lcd.plot_function(
    lambda x: math.sin(x),
    x_min,
    x_max,
    color=0x07E0,
    thickness=2
)
lcd.plot_function(
    lambda x: 2* math.sin(x),
    x_min,
    x_max,
    color=0x780F,
    thickness=2
)
lcd.plot_function(
    lambda x: 0.02*x * x,
    x_min,
    x_max,
    color=0xAFE5,
    thickness=2
)
lcd.plot_function(
    lambda x: -0.2*x * x,
    x_min,
    x_max,
    color=0x03EF,
    thickness=2
)
lcd.plot_function(
    lambda x: x,
    x_min,
    x_max,
    color=0xFEB4,
    thickness=3
)
lcd.plot_function(
    lambda x: -x+3,
    x_min,
    x_max,
    color=0xF643,
    thickness=3
)
lcd.plot_function(
    lambda x: math.pow(x,3),
    x_min,
    x_max,
    color=0xA100,
    thickness=3
)
lcd.plot_function(
    lambda x: -math.pow(x,3),
    x_min,
    x_max,
    color=0x03E9,
    thickness=3
)
