from pymodbus.client import ModbusSerialClient
import time

GPIO_BOX = ModbusSerialClient(
    port="/dev/ttyUSB0",
    baudrate=9600,
    parity="N",
    stopbits=1,
    bytesize=8,
    timeout=1
)

relay=6

def on(IO):
    print("Connect:", GPIO_BOX.connect())
    print("ON")
    GPIO_BOX.write_coil(IO, True, device_id=1)

def off(IO):
    print("OFF")
    GPIO_BOX.write_coil(IO, False, device_id=1)
    GPIO_BOX.close()

on(relay)
time.sleep(2)
off(relay)
