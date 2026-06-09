# Pins Raspberry Pi Pico:

- SPI principal - SPI_ID=1

| Nombre normal |	Nombre en tabla	| Pin (No.)	    | Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	SPI0 CSn        | 17	          | GPIO 13  |
| MOSI/SDA/SDI	| SPI1 TX         | 20	          | GPIO 15  |
| SCK/CLK	      | SPI1 SCK        | 19	          | GPIO 14  |
| MISO/SDO      |	SPI1 RX	        | 16	          | GPIO 12  |

# Pins 3,5" TFT SPI 480x320 v1.0 ILI9488:

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


<div align="center">
  <table>
    <tr>
      <td align="center"><a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/Raspberry%20Pi%20Pico/pico-pinout.png" target="_blank"></a><img src="pico-pinout.png" width="100%"></td>
      <td align="center"><a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/35_TFT_SPI_480x320_V1-0.jpg" target="_blank"></a><img src="../ESP32-S3 16MB PSRAM 8MB/35_TFT_SPI_480x320_V1-0.jpg" width="100%"></td>
    </tr>
  </table>
</div>
