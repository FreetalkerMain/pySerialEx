import serial
import time


#COM="COM5"
COM="/dev/ttyACM0"
bitRate=9600

ser = serial.Serial(COM, bitRate, timeout=0.1)

while True:
 time.sleep(0.1)
 result = ser.read_all()
 print(result)
 if result == b'\r':	# <Enter>で終了
  break

print('program end')

ser.close()
