
import serial

with serial.Serial('COM3', 9600, timeout=1) as ser:
   
    while True:
        arduino_output = ser.readline().decode('ISO-8859-1')
        print(arduino_output)
        
       