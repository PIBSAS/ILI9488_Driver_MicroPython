# ESP32 WROOM 32 Pinout:

<div align="center">
  <img src="ESP32 WROOM 32.jpg" alt="ESP32 WROOM 32">
</div>

<div align="center">
  <ul>
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032/esp32-wroom-32_datasheet_en.pdf" target="_blank">ESP32 WROOM 32 Datasheet</a>
    <br>
    <a href="https://documentation.espressif.com/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide_v2.html" target="_blank">ESP32 WROOM 32 Docs</a>
  </ul>
</div>

----

- SPI principal (`FSPI`) - `SPI_ID=1`

----

| Nombre normal |	Nombre en tabla	| Pin (No.)   	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	VSPI SS	        | 23	          | GPIO  5  |
| MOSI/SDA/SDI	| VSPI MOSI       | 30	          | GPIO 23  |
| SCK/CLK	      | VSPI SCK        | 24	          | GPIO 18  |
| MISO/SDO      |	VSPI MISO       | 25	          | GPIO 19  |

----

# 3,5" TFT SPI 480x320 v1.0 ILI9488 Pinout:

| Nombre normal |	Nombre en tabla	| Pin (No.)	        | Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	VSPI MISO       | 25	              | GPIO 19  |
| LED           | ----------------| 10                | GPIO 27  |
| SCK/CLK	      | VSPI SCK        | 24	              | GPIO 18  |
| SDI/MOSI/SDA	| VSPI MOSI	      | 30	              | GPIO 23  |
| DC/RS         | ----------------| 12                | GPIO 12  |
| RESET         | ----------------| 11                | GPIO 14  |
| CS/SS         |	VSPI SS	        | 23	              | GPIO  5  |
| GND           | GND             | 14                | GND      |
| VCC           | 3V3             | 16                | 3V3      |

----

<div align="center">
  <table>
    <tr>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32%20WROOM%2032/ESP32%20WROOM%2032%20pinout.jpg" target="_blank">
          <img src="ESP32 WROOM 32 pinout.jpg" width="100%">
        </a>
      </td>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/35_TFT_SPI_480x320_V1-0.jpg" target="_blank">
          <img src="../ESP32-S3 16MB PSRAM 8MB/35_TFT_SPI_480x320_V1-0.jpg" width="100%">
        </a>
      </td>
    </tr>
  </table>
</div>
