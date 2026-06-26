# Raspberry Pi Pico W Pinout:

<div align="center">
  <img src="picow.png">
</div>

<div align="center">
  <ul>
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/Raspberry%20Pi%20Pico%20W/pico-w-datasheet.pdf" target="_blank">Raspberry Pi Pico W Datasheet</a>
    <br>
    <a href="https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#wireless_pico" target="_blank">Raspberry Pi Pico W Docs</a>
  </ul>
</div>

----

- SPI principal (`SPI`) - `SPI_ID=1`

----

| Nombre normal |	Nombre en tabla	| Pin (No.)	    | Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	SPI0 CSn        | 17	          | GPIO 13  |
| MOSI/SDA/SDI	| SPI1 TX         | 20	          | GPIO 15  |
| SCK/CLK	      | SPI1 SCK        | 19	          | GPIO 14  |
| MISO/SDO      |	SPI1 RX	        | 16	          | GPIO 12  |

----

# 3,5" TFT SPI 480x320 v1.0 ILI9488 Pinout:

| Nombre normal |	Nombre en tabla	| Pin (No.)       	| Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	SPI1 RX         | 16	              | GPIO 12  |
| LED           | --------------- | 37                | GPIO 22  |
| SCK/CLK	      | SPI1 SCK        | 19	              | GPIO 14  |
| SDI/MOSI/SDA	| SPI1 TX         | 20	              | GPIO 15  |
| DC/RS         | --------------- | 9                 | GPIO 6   |
| RESET         | --------------- | 10                | GPIO 7   |
| CS/SS         |	SPI0 CSn        | 17	              | GPIO 13  |
| GND           | GND             | 18                | GND      |
| VCC           | 3V3             | 36                | 3V3 (OUT)|

----

<div align="center">
  <table>
    <tr>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/Raspberry%20Pi%20Pico%20W/Picow-pinout.png" target="_blank">
          <img src="Picow-pinout.png" width="100%">
        </a>
      </td>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/35_TFT_SPI_480x320_V1-0.png" target="_blank">
          <img src="../ESP32-S3 16MB PSRAM 8MB/35_TFT_SPI_480x320_V1-0.png" width="100%">
        </a>
      </td>
    </tr>
  </table>
</div>

<h3>Raspberry Pi Pico W Datasheet:</h3>
<div align="left">
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/Raspberry%20Pi%20Pico%20W/pico-w-datasheet.pdf" target="_blank">
      <img src="pico-w-datasheet.webp" width="40%">
    </a>
</div>
