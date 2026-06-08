<h1 align="center">ILI9488 Driver MicroPython for 3.5" TFT SPI 320x480 V1.0 Display</h1>

<div align="center">
  <img src="boards/ESP32-S3 16MB PSRAM 8MB/35_TFT_SPI_480x320_V1-0.jpg" alt="" target="_blank">
</div>

<div align="center">
  <table>
    <tr>
      <th colspan="3" align="center">Display Pins</th>
    </tr>
    <tr>
      <th>Display</th>
      <th>Touch</th>
      <th>SD Slot</th>
    </tr>
    <tr>
      <td>VCC</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>GND</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CS</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>RESET</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>CS/RS</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SDI (MOSI)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SCK</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>LED</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>SDO (MISO)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>T_CLK</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>T_CS</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>T_DIN (MOSI)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>T_DO (MISO)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>T_IRQ</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>SD_CS</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>SD_MOSI</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>SD_MISO</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>SD_SCK</td>
    </tr>
  </table>
</div>

<div>
  <h2>File estructure on microcontroller</h2>

<div>
<pre>
&#x1F4DF; root microcontroller
&#x251C;&#x2500;&#x2500; &#x1F4C1;fonts (WE DON'T NEED ALL OF THEM)
&#x7C;   &#x251C;&#x2500;&#x2500; &#x1F4C4;vga1_8x8.py
&#x7C;   &#x2514;&#x2500;&#x2500; &#x1F4C4;vga1_8x16.py 
&#x7C;  
&#x251C;&#x2500;&#x2500; &#x1F4C4;ili9488.py
&#x251C;&#x2500;&#x2500; &#x1F4C4;set_display.py (from boards/YOUR_BOARD)
&#x251C;&#x2500;&#x2500; &#x1F4C4;example.py (from examples)
&#x2514;&#x2500;&#x2500; &#x1F4C4;image.bmp (from examples)
</pre>  
</div>

<div>
  <h2>Basic template code</h2>
</div>

</div>


````python
from ili9488 import driver, Color # Class driver and Color
import set_display # SPI Pins of your board
import fonts.vga1_16x16 as font # Only if you're going to write

# Set display connection and rotation 0=0º, 1=90º, 2=180ª, 3=270ª
lcd = set_display.setting(0) 

# Put a background color to the display or will be gray with scanlines
lcd.fill(Color.WHITE)

# Write text on screen
lcd.text("Luciano's tech", 0, 10, Color.RED, font, Color.PCYAN)
````

<h2>Class Color</h2>

<p>See the next table on the web <a href="https://pibsas.github.io/ILI9488_Driver_MicroPython/" target="_blank">README</a> version</p>

<div align="center">
  <table style="background-color:#F0F0F0;">
    <tr>
      <th colspan="3" align="center">CONSTANTS COLOR</th>
    </tr>
    <tr>
      <th>Color.{CONSTANT}</th>
      <th>RGB 565 HEX Code</th>
      <th>PREVIEW</th>
    </tr>
    <tr>
      <td>BLACK</td>
      <td>0x0000</td>
      <td style="background-color:#000000; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>WHITE</td>
      <td>0xFFFF</td>
      <td style="background-color:#ffffff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>RED</td>
      <td>0xF800</td>
      <td style="background-color:#ff0000; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>BLUE</td>
      <td>0x001F</td>
      <td style="background-color:#0000ff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>GREEN</td>
      <td>0x07E0</td>
      <td style="background-color:#00ff00; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>CYAN</td>
      <td>0x07FF</td>
      <td style="background-color:#00ffff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>MAGENTA</td>
      <td>0xF81F</td>
      <td style="background-color:#ff00ff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>YELLOW</td>
      <td>0xFFE0</td>
      <td style="background-color:#ffff00; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>ORANGE</td>
      <td>0xFD20</td>
      <td style="background-color:#ffa600; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PINK</td>
      <td>0xFE3F</td>
      <td style="background-color:#ffc6ff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>MAROON</td>
      <td>0x7800</td>
      <td style="background-color:#7b0000; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PURPLE</td>
      <td>0x780F</td>
      <td style="background-color:#7b007b; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>OLIVE</td>
      <td>0x7BE0</td>
      <td style="background-color:#7b7d00; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>GREENYELLOW</td>
      <td>0xAFE5</td>
      <td style="background-color:#adff29; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>DARKGREEN</td>
      <td>0x03E0</td>
      <td style="background-color:#007d00; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>DARKCYAN</td>
      <td>0x03EF</td>
      <td style="background-color:#007d7b; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>DARKGREY</td>
      <td>0x7BEF</td>
      <td style="background-color:#7b7d7b; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>LIGHTGREY</td>
      <td>0xC618</td>
      <td style="background-color:#c5c2c5; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PRED</td>
      <td>0xFD75</td>
      <td style="background-color:#ffaead; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PORANGE</td>
      <td>0xFEB4</td>
      <td style="background-color:#ffd7a5; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PGREEN</td>
      <td>0xCFF7</td>
      <td style="background-color:#ceffbd; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PYELLOW</td>
      <td>0xFFF6</td>
      <td style="background-color:#ffffb5; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PCYAN</td>
      <td>0x9FBF</td>
      <td style="background-color:#9cf7ff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PBLUE</td>
      <td>0x9E1F</td>
      <td style="background-color:#9cc2ff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>PPURPLE</td>
      <td>0xBD9F</td>
      <td style="background-color:#bdb2ff; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>TRED</td>
      <td>0xD945</td>
      <td style="background-color:#de2829; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>TORANGE</td>
      <td>0xF384</td>
      <td style="background-color:#f77121; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>TYELLOW</td>
      <td>0xF643</td>
      <td style="background-color:#f7ca19; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>TGREEN</td>
      <td>0x7568</td>
      <td style="background-color:#73ae42; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>TDARKGREEN</td>
      <td>0x03E9</td>
      <td style="background-color:#007d4a; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>ALL</td>
      <td>A list with all constants</td>
      <td style="background-color:#000000; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>rgb(red 5 bit,green 6 bit,blue 5 bits)</td>
      <td>Color.rgb(255,34,124)</td>
      <td style="background-color:#ff8aff; width:40px; height:20px;"></td>
    </tr>
  </table>
</div>
