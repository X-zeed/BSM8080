from pymodbus.client import ModbusSerialClient
import time

client = ModbusSerialClient(
    port="/dev/ttyUSB0",
    baudrate=9600,
    parity="N",
    stopbits=1,
    bytesize=8,
    timeout=1
)

relay=0

print("Connect:", client.connect())

print("Relay ON")
client.write_coil(relay, True, device_id=1)
time.sleep(2)

print("Relay OFF")
client.write_coil(relay, False, device_id=1)

client.close()
