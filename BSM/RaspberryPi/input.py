import serial, time

ser = serial.Serial("/dev/ttyUSB0",9600,timeout=1)
frame = bytes([0x01,0x02,0x00,0x00,0x00,0x08,0x79,0xCC])


#DI ขา 3 

while True:
    ser.write(frame)
    res = ser.read(100)

    if len(res) >= 4:
        data = res[3]

        if data == 0x00:
            print("DI3 OFF")
        elif data == 0x04:
            print("DI3 ON")
        else:
            print("DATA =", data)

    else:
        print("No response")

    time.sleep(1)
