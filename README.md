# Environmental Monitoring with WIZNET W5500-EVB-Pico and BME280

## Wiring
Wiring Pimoroni BME280 module to W5500 Pico:
- BME GND -> 38
- BME 2 - 5v -> 36
- BME SDA -> 1
- BME SCL -> 2

## Packages
- https://pypi.org/project/network/
- https://pypi.org/project/smbus2/
- https://github.com/robert-hh/BME280/blob/master/bme280_float.py

## Run
Copy main.py to W5500 Pico. Please update the following settings:
- [SERVER] - URL where processing script lives
- [SCRIPT] - name of script
- [DEVICE_IP] and [ROUTER_IP] - on line 19
- [LOCATION] - on line 50

## Notes
- WIZNET W5500-EVB-Pico does not support TLS connections, so the [SERVER] needs to be accessible on port 80
