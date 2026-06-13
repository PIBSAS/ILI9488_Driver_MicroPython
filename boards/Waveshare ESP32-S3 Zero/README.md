# Waveshare ESP32-S3 Zero Pinout:

<div align="center">
  <img src="ESP32-S3-Zero.png" alt="ESP32-S3 Zero">
</div>

<div align="center">
  <ul>
  <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/Waveshare%20ESP32-S3%20Zero/esp32-s3_datasheet_en.pdf" target="_blank">ESP32 S3 Datasheet</a>
    <br>
  <a href="https://docs.waveshare.com/ESP32-S3-Zero" target="_blank">Waveshare ESP32-S3 Zero Wiki</a>
  </ul>
</div>

----

- SPI principal (`FSPI`) - `SPI_ID=1`

----

| Nombre normal |	Nombre en tabla	| Pin J3 (No.)	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	FSPICS0	        | 13	          | GPIO 10  |
| MOSI/SDA/SDI	| FSPID	          | 14	          | GPIO 11  |
| SCK/CLK	      | FSPICLK	        | 15	          | GPIO 12  |
| MISO/SDO      |	FSPIQ	          | 16	          | GPIO 13  |

----

# 3,5" TFT SPI 480x320 v1.0 ILI9488 Pinout:

| Nombre normal |	Nombre en tabla	| Pin (No.)	        | Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	FSPIQ	          | 16	              | GPIO 13  |
| LED           | ----------------| 8                 | GPIO 5   |
| SCK/CLK	      | FSPICLK	        | 15	              | GPIO 12  |
| SDI/MOSI/SDA	| FSPID	          | 14	              | GPIO 11  |
| DC/RS         | ----------------| 9                 | GPIO 6   |
| RESET         | ----------------| 10                | GPIO 7   |
| CS/SS         |	FSPICS0	        | 13	              | GPIO 10  |
| GND           | GND             | 2                 | GND      |
| VCC           | 3V3             | 3                 | 3V3(OUT) |

----

<div align="center">
  <table>
    <tr>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/Waveshare%20ESP32-S3%20Zero/ESP32-S3-Zero.jpg" target="_blank">
          <img src="ESP32-S3-Zero.jpg" width="100%">
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
