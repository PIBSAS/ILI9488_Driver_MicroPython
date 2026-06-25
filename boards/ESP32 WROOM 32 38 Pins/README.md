# ESP32 WROOM 32 38 Pins Pinout:

<div align="center">
  <img src="ESP32 WROOM 32 38.png" alt="ESP32 WROOM 32 38 Pins">
</div>

<div align="center">
  <ul>
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032%2038%20Pins/esp32-wroom-32_datasheet_en.pdf" target="_blank">ESP32 WROOM 32 Datasheet</a>
    <br>
    <a href="https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide_v2.html" target="_blank">ESP32 WROOM 32 38 Pins Docs</a>
  </ul>
</div>

----

- SPI principal (`VSPI`) - `SPI_ID=2`

----

| Nombre normal |	Nombre en tabla	| Pin (No.)   	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	VSPI SS	        | 29	          | GPIO  5  |
| MOSI/SDA/SDI	| VSPI MOSI       | 37	          | GPIO 23  |
| SCK/CLK	      | VSPI SCK        | 30	          | GPIO 18  |
| MISO/SDO      |	VSPI MISO       | 31	          | GPIO 19  |

----

# 3,5" TFT SPI 480x320 v1.0 ILI9488 Pinout:

| Nombre normal |	Nombre en tabla	| Pin (No.)	        | Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	VSPI MISO       | 31	              | GPIO 19  |
| LED           | ----------------| 11                | GPIO 27  |
| SCK/CLK	      | VSPI SCK        | 30	              | GPIO 18  |
| SDI/MOSI/SDA	| VSPI MOSI	      | 37	              | GPIO 23  |
| DC/RS         | ----------------|  9                | GPIO 25  |
| RESET         | ----------------| 10                | GPIO 26  |
| CS/SS         |	VSPI SS	        | 29	              | GPIO  5  |
| GND           | GND             | 38                | GND      |
| VCC           | 3V3             | 1                 | 3V3      |

----

# SPI SD with MicroPython SDCard Class Pinout:

----

| Nombre normal |	Nombre en tabla	| Pin (No.)   	| Pin Name |
|---------------|-----------------|---------------|----------|
| SD_CS         |	HSPICS0	        | 23	          | GPIO 15  |
| SD_MOSI	      | HSPID           | 15	          | GPIO 13  |
| SD_MISO       |	HSPICLK         | 12	          | GPIO 14  |
| SD_SCK        | GPIO 33         |  8	          | GPIO 33  |


----

<div align="center">
  <table>
    <tr>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032%2038%20Pins/ESP32%20WROOM%2032%2038%20pin%20pinout.jpg" target="_blank">
          <img src="ESP32 WROOM 32 38 pin pinout.jpg" width="100%">
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
