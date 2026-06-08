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
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
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
      <td>LIGHTGREY</td>
      <td>0xC618</td>
      <td style="background-color:#c5c2c5; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>DARKGREY</td>
      <td>0x7BEF</td>
      <td style="background-color:#7b7d7b; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td></td>
      <td>0x0000</td>
      <td style="background-color:#000000; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
    <tr>
      <td>NAVY</td>
      <td>0x000F</td>
      <td style="background-color:#00007B; width:40px; height:20px;"></td>
    </tr>
  </table>
</div>

| Column 1                              | Column 2                              | Column 3                              |
|----------------------------------------|----------------------------------------|----------------------------------------|
| Normal cell                            | <span style="background-color:yellow">Yellow cell</span> | Normal cell                            |
| <span style="background-color:lightblue">Light blue cell</span> | Normal cell                            | <span style="background-color:pink">Pink cell</span> |
