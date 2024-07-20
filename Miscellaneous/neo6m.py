import serial

rx_pin = '/dev/tty.BLTH'  # Replace with your actual serial port
baud_rate = 9600

try:
    serialGPS = serial.Serial(rx_pin, baud_rate)

    while True:
        if serialGPS.in_waiting > 0:
            data = serialGPS.readline()
            print(data.decode('utf-8').strip())  # Assuming GPS data is in UTF-8 encoding

except KeyboardInterrupt:
    serialGPS.close()
    print("Serial connection closed.")
