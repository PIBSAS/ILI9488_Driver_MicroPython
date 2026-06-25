# NodeMCU ESP32-S Pinout:

<div align="center">
  <img src="NodeMCU ESP32-S 38 pin.png" alt="NodeMCU ESP32-S">
</div>

<div align="center">
  <ul>
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/NodeMCU%20ESP32%20S/esp32_datasheet_en.pdf" target="_blank">ESP32 Datasheet</a>
    <br>
    <a href="https://nodemcu.readthedocs.io/en/dev-esp32/" target="_blank">NodeMCU ESP32-S Docs</a>
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
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/NodeMCU%20ESP32%20S/NodeMCU%20ESP32-S%2038%20pin%20pinout.jpg" target="_blank">
          <img src="NodeMCU ESP32-S 38 pin pinout.jpg" width="100%">
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

<h3>ESP32 Series Datasheet:</h3>
<div align="left">
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032/esp32_datasheet_en.pdf" target="_blank">
      <img src="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032/esp32_datasheet_en.webp" width="40%">
    </a>
</div>

<h3>ESP32 Technical Reference Manual:</h3>
<div align="left">
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032/esp32_technical_reference_manual_en.pdf" target="_blank">
      <img src="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032/esp32_technical_reference_manual_en.webp" width="40%">
    </a>
</div>
