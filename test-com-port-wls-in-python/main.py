import serial
ser = serial.Serial('/dev/ttyS8', 57600, timeout=10) # open serial port
print(ser.name) # check which port was really used
#ser.write(b'hello') # write a string
s = ser.read(20)
print(f'--> {s}')
ser.close()