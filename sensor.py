import board
import busio
import adafruit_tcs34725
import time

i2c = busio.I2C(board.SCL, board.SDA)
colorSensor = adafruit_tcs34725.TCS34725(i2c)

def getScannedFraction(): # match the reading from the fraction circle to its corresponding color
    
    red = colorSensor.color_rgb_bytes[0]
    green = colorSensor.color_rgb_bytes[1]
    blue = colorSensor.color_rgb_bytes[2]

    print("red: " + str(red))
    print("green: " + str(green))
    print("blue: " + str(blue))

    if(red > 90 and green < 7 and blue < 6):
        return "1/8"
    
    elif(red < 10 and green > 5 and green < 20 and blue > 50):
        return "1/1"
    
    elif(red > 5 and red < 15 and green > 10 and green < 20 and blue > 15 and blue < 25):
        return "1/2"
    
    elif(red < 10 and green > 10 and green < 25 and blue > 20 and blue < 35):
        return "1/3"
    
    elif(red > 100 and green > 100 and blue > 30):
        return "1/4"
    
    elif(red < 5 and green > 40 and green < 55 and blue > 5 and blue < 15):
        return "1/5"
    
    elif(red > 70 and green < 10 and blue < 5 ):
        return "1/6"
    
    elif(red > 10 and red < 30 and green < 15 and blue > 20 and blue < 40):
        return "1/10"

    else: return "1/1"

i = 0
while i < 10: #True:
    print('Color: ({0}, {1}, {2})'.format(*colorSensor.color_rgb_bytes))
    i = i + 1
    #time.sleep(2)


