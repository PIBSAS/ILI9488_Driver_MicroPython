# Pins ESP32-WROOM-32D:

- SPI principal (FSPI) - SPI_ID=1

| Nombre normal |	Nombre en tabla	| Pin (No.)   	| Pin Name |
|---------------|-----------------|---------------|----------|
| CS/SS         |	FSPICS0	        | 23	          | GPIO 15  |
| MOSI/SDA/SDI	| FSPID	          | 15	          | GPIO 13  |
| SCK/CLK	      | FSPICLK	        | 12	          | GPIO 14  |
| MISO/SDO      |	FSPIQ	          | 13	          | GPIO 12  |

# Pins 3,5" TFT SPI 480x320 v1.0 ILI9488:

| Nombre normal |	Nombre en tabla	| Pin (No.)	        | Pin Name |
|---------------|-----------------|-------------------|----------|
| MISO/SD0      |	FSPIQ	          | 13	              | GPIO 12  |
| LED           | ----------------| 26                | GPIO 4   |
| SCK/CLK	      | FSPICLK	        | 12	              | GPIO 14  |
| SDI/MOSI/SDA	| FSPID	          | 15	              | GPIO 13  |
| DC/RS         | ----------------| 27                | GPIO 16  |
| RESET         | ----------------| 28                | GPIO 17  |
| CS/SS         |	FSPICS0	        | 23	              | GPIO 15  |
| GND           | GND             | 38                | GND      |
| VCC           | 3V3             | 1                 | 3V3      |


<div align="center">
  <table>
    <tr>
      <td align="center"><a href="" target="_blank"><img src="esp32_devkitC_v4_pinlayout.png" width="100%"></td>
      <td align="center"><a href="https://github.com/PIBSAS/ILI9488_Driver_MicroPython/blob/main/boards/ESP32-S3%2016MB%20PSRAM%208MB/35_TFT_SPI_480x320_V1-0.jpg" target="_blank" rel="noopener noreferrer"></a><img src="../ESP32-S3 16MB PSRAM 8MB/35_TFT_SPI_480x320_V1-0.jpg" width="100%"></td>
    </tr>
  </table>
</div>
