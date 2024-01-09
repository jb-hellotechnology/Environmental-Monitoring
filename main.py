import usocket
from machine import Pin, SPI, I2C
import network
import uasyncio as asyncio
import time
import bme280_float

BASE_URL = "[SERVER]"
URL_PATH = "[SCRIPT]"

# W5x00 chip init
def w5x00_init():
    print("Initiating internet connection...")
    spi = SPI(0, 2_000_000, mosi=Pin(19), miso=Pin(16), sck=Pin(18))
    nic = network.WIZNET5K(spi, Pin(17), Pin(20))  # spi,cs,reset pin
    nic.active(True)

    # None DHCP
    nic.ifconfig(('[DEVICE_IP]', '255.255.255.0', '[ROUTER_IP]', '8.8.8.8'))

    # DHCP
    # nic.ifconfig('dhcp')
    print('IP address:', nic.ifconfig())

def resolve_dns(hostname):
    print("Resolving DNS...")
    addr_info = usocket.getaddrinfo(hostname, 80)
    return addr_info[0][-1]

async def read_bme280():
    i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
    bme = bme280_float.BME280(i2c=i2c)

    temperature, pressure, humidity = bme.read_compensated_data()

    return {
        "temperature": temperature,
        "pressure": pressure / 256.0,
        "humidity": humidity,
    }

async def make_request(data):
    try:
        server_ip = resolve_dns(BASE_URL)
        addr = (server_ip[0], 80)
        s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        s.connect(addr)

        # Construct the POST request data
        post_data = "temperature={:.2f}&pressure={:.2f}&humidity={:.2f}&location=[LOCATION]".format(
            data["temperature"], data["pressure"], data["humidity"]
        )

        # Construct the POST request headers
        headers = "POST {} HTTP/1.1\r\n".format(URL_PATH)
        headers += "Host: {}\r\n".format(BASE_URL)
        headers += "Content-Type: application/x-www-form-urlencoded\r\n"
        headers += "Content-Length: {}\r\n\r\n".format(len(post_data))

        # Send the POST request
        s.write(headers.encode('utf-8'))
        s.write(post_data.encode('utf-8'))

        # Read and print the response data
        response = s.read(4096)
        s.close()

        if response:
            print("Request successful. Response:", response.decode('utf-8'))
        else:
            print("No data received.")

    except Exception as e:
        print("Error during request:", e)

def main():
    w5x00_init()

    while True:
        bme_data = asyncio.run(read_bme280())
        asyncio.run(make_request(bme_data))
        time.sleep(1800)

if __name__ == "__main__":
    main()

