# ESP32-C3 SUPER MINI Pinout:

<div align="center">
  <img src="esp32-c3 super mini.png">  
</div>

<div align="center">
  <ul>
    <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-C3%20SUPER%20MINI/esp32-c3_datasheet_en.pdf" target="_blank">ESP32 C3 Datasheet</a>
    <br>
    <a href="https://wiki.nologo.tech/en/product/esp32/esp32c3SuperMini/esp32C3SuperMini.html" target="_blank">NoLogo ESP32-C3 Super Mini Wiki</a>
  </ul>
</div>

----

- SPI principal (`FSPI`) - `SPI_ID=1`

----

| Nombre normal |	Nombre en tabla	| Pin (No.)    	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	FSPICS0	        | 3 	          | GPIO 7   |
| MOSI/SDA/SDI	| FSPID	          | 2 	          | GPIO 6   |
| SCK/CLK	      | FSPICLK	        | 13	          | GPIO 4   |
| MISO/SDO      |	FSPIQ	          | 1	            | GPIO 5   |

----

# 3,5" TFT SPI 480x320 v1.0 ILI9488 Pinout:

| Nombre normal |	Nombre en tabla	| Pin (No.)       	| Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	FSPIQ	          | 1 	              | GPIO 13  |
| LED           | ----------------| 6                 | GPIO 10  |
| SCK/CLK	      | FSPICLK	        | 13	              | GPIO 4   |
| SDI/MOSI/SDA	| FSPID	          | 2 	              | GPIO 6   |
| DC/RS         | ----------------| 12                | GPIO 3   |
| RESET         | ----------------| 11                | GPIO 2   |
| CS/SS         |	FSPICS0	        | 3 	              | GPIO 7   |
| GND           | GND             | 15                | GND      |
| VCC           | 3V3             | 14                | 3V3      |

----

<div align="center">
  <table>
    <tr>
      <td>
        <a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-C3%20SUPER%20MINI-Pinout.png" target="_blank">
          <img src="ESP32-C3 SUPER MINI-Pinout.png" width="100%">
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
