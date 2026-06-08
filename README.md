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
&#x251C;&#x2500;&#x2500; &#x1F4C1;fonts
   &#x251C;&#x2500;&#x2500; &#x1F4C4;vga1_8x8.py
   &#x2514;&#x2500;&#x2500; &#x1F4C4;vga1_8x16.py
  
&#x251C; &#x2500; &#x2500; &#x1F4C4; ili9488.py
&#x2514; &#x2500;&#x2500; &#x1F4C4;set_display.py
</pre>  
</div>
</div>
