import board
import busio
import adafruit_tcs34725
import time

# * Initializes the light color (light) sensor 
i2c = busio.I2C(board.SCL, board.SDA)
colorSensor = adafruit_tcs34725.TCS34725(i2c)

# * Recorded color ranges for the specific color pieces in the box
colors={
    "Red":((60,80),(4,9),(4,9)),
    "Orange":((52,63),(7,11),(1,3)),
    "Yellow":((30,40),(16,22),(2,4)),
    "Green":((10,16),(20,30),(9,14)),
    "Blue":((8,14),(10,18),(22,39)),
    "Purple":((16,31),(8,12),(15,20)),
    "Black":((15,35),(12,16),(12,16)),
    "Brown":((20,36),(8,16),(8,11)),
    "Pink":((55,68),(3,6),(7,9))
}

# * This function takes the r,g,b color values received from the sensor and checks whether it is in the accetable color range
def checkRGB(r,g,b,col):
    if r>=col[0][0] and r<=col[0][1] and g>=col[1][0] and g<=col[1][1] and b>=col[2][0] and b<=col[2][1]:
        return True

# * Gets the corresponding color name from the r,g,b values 
def getColorName(r,g,b):
    for col in colors:
        if checkRGB(r,g,b,colors[col]):
            return col
    return "Color Not Recognized"

# * Returns the r,g,b values and the colorname in an array        
def getRGB():
    red = colorSensor.color_rgb_bytes[0]
    green = colorSensor.color_rgb_bytes[1]
    blue = colorSensor.color_rgb_bytes[2]
    return [red,green,blue,getColorName(red,green,blue)]
