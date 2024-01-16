# Environmental Monitoring with WIZNET W5500-EVB-Pico and BME280
A simple device to monitor temperature, humidity and pressure. Sends data to a publically accessible URL every 30 minutes or so.

## Hardware
- https://www.wiznet.io/product-item/w5500-evb-pico/
- https://shop.pimoroni.com/products/bme280-breakout?variant=29420960677971

## Wiring
Wiring Pimoroni BME280 module to W5500 Pico:
| BME Module | W5500 Board |
|-----|-------|
| GND |   38  |
| 2-5v|   36  |
| SDA |    1  |
| SCL |    2  |

## MicroPython Packages
- https://pypi.org/project/network/
- https://pypi.org/project/smbus2/
- https://github.com/robert-hh/BME280/blob/master/bme280_float.py

## Run
Copy main.py to W5500 Pico. Please update the following settings:
- [SERVER] - URL where processing script lives
- [SCRIPT] - name of script which processes incoming data on server
- [DEVICE_IP] and [ROUTER_IP] - on line 19
- [LOCATION] - on line 50

## Notes
- WIZNET W5500-EVB-Pico does not support TLS connections, so the [SERVER] needs to be accessible on port 80
