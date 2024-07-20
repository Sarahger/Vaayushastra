import serial

# Define the serial ports
arduino_port = "/dev/"
gps_port = "/dev/ttyS0"

# Create serial objects
arduino = serial.Serial(arduino_port, 9600)
gps = serial.Serial(gps_port, 9600)

# Continuously read data from the GPS port and send it to the Arduino port
while True:
    data = gps.readline().decode("utf-8")
    arduino.write(data.encode("utf-8"))
