import board
import busio
import adafruit_tcs34725
import time
import rgbSensor


# * Colors corresponding to the fraction values on the pieces 
values={  "Red":"1/8",
    "Orange":"1/6",
    "Yellow":"1/4",
    "Green":"1/5",
    "Blue":"1/1",
    "Purple":"1/10",
    "Black":"1/3",
    "Brown":"1/2",
    "Pink":"1/12"
    }

# * Helper function which returns the fraction value of the color scanned which will be used for calculations and updating the GUI
def getScannedFraction():
    colorAttr=rgbSensor.getRGB()
    colorName=colorAttr[3]
    print(colorName+": "+str(colorAttr[0])+","+str(colorAttr[1])+","+str(colorAttr[2]))
    if colorName == "Color Not Recognized":
        return "1/13"
    else:
        return values[colorName]




