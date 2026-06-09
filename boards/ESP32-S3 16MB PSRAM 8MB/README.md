# Pins ESP32 S3 WRROM-1 16MB PSRAM 8MB:

<div align="center">
  <img src="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/ESP32-S3-16MB-PSRAM-8MB.png">
</div>

<div align="center">
  <ul>
  <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf">ESP32 S3 WROOM-1 Datasheet</a><br>
  <a href="https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/index.html">ESP32 S3 WROOM-1 docs</a>
  </ul>
</div>

----

- SPI principal (`FSPI`) - `SPI_ID=1`

----

| Nombre normal |	Nombre en tabla	| Pin J3 (No.)	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	FSPICS0	        | 16	          | GPIO 10  |
| MOSI/SDA/SDI	| FSPID	          | 17	          | GPIO 11  |
| SCK/CLK	      | FSPICLK	        | 18	          | GPIO 12  |
| MISO/SDO      |	FSPIQ	          | 19	          | GPIO 13  |

----

# Pins 3,5" TFT SPI 480x320 v1.0 ILI9488:

| Nombre normal |	Nombre en tabla	| Pin J3 & J1 (No.)	| Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	FSPIQ	          | 19	              | GPIO 13  |
| LED           | ----------------| J1 =2             | 3V3      |
| SCK/CLK	      | FSPICLK	        | 18	              | GPIO 12  |
| SDI/MOSI/SDA	| FSPID	          | 17	              | GPIO 11  |
| DC/RS         | ----------------| 6                 | GPIO 6   |
| RESET         | ----------------| 7                 | GPIO 7   |
| CS/SS         |	FSPICS0	        | 16	              | GPIO 10  |
| GND           | GND             | 1                 | GND      |
| VCC           | 3V3             | J1 = 1            | 3V3      |

----

<div align="center">
  <table>
    <tr>
      <td align="center"><a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/ESP32-S3_DevKitC-1_pinlayout_v1.1.jpg" target="_blank"><img src="ESP32-S3_DevKitC-1_pinlayout_v1.1.jpg" width="100%"></td>
      <td align="center"><a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/35_TFT_SPI_480x320_V1-0.jpg" target="_blank" rel="noopener noreferrer"></a><img src="../ESP32-S3 16MB PSRAM 8MB/35_TFT_SPI_480x320_V1-0.jpg" width="100%"></td>
    </tr>
  </table>
</div>
