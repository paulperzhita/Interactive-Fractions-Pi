import board
import busio
import adafruit_tcs34725
import time

i2c = busio.I2C(board.SCL, board.SDA)
colorSensor = adafruit_tcs34725.TCS34725(i2c)

red = colorSensor.color_rgb_bytes[0]
green = colorSensor.color_rgb_bytes[1]
blue = colorSensor.color_rgb_bytes[2]

print(str(red))
print(str(green))
print(str(blue))