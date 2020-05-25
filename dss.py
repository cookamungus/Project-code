
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

Red=40
Green=38

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.

def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    while(True):         
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
        lcd.message('Distance:' + str(distance) + 'cm') # String that will be d$
        if distance < 30:
            GPIO.output(Red, GPIO.HIGH)
            lcd.setCursor(0,1)
            lcd.message('Too Close!')
            print('Too Close')
            time.sleep(3)
            GPIO.output(Red, GPIO.LOW)
            time.sleep(3)
            print ('Enter close to exit program')
            input()
            if input == 'close':
                sys.exit()
        if distance > 30:
            GPIO.output(Green, GPIO.HIGH)
            lcd.setCursor(0,1)
            lcd.message('Safe Distance')
            print('Safe Distance')
            time.sleep(3)
            GPIO.output(Green, GPIO.LOW)
            time.sleep(3)
            print ('Enter close to exit program')
            input()
            if input == close:
                sys.exit()

def led():
    GPIO.setmode(GPIO.BOARD) # Use physical GPIO numbering
    GPIO.setup(Red, GPIO.OUT) # Sets GPIO pin 40 to output, as 40 is stored in variable 'Red"
    GPIO.setup(Green, GPIO.OUT) #Sets GPIO pin 38 to output, as 38 is stored in varable "Green"
    GPIO.output(Red, GPIO.LOW) #Sets Red to Low power, or 0, for no LED
    GPIO.output(Green, GPIO.LOW) #Sets Green to low power, or 0 for no LED


try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp) # Create LCD, passing in MCP GPIO adapter.


try:
        if __name__ == '__main__':
            print ('Program is starting ... ')

            GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 7
        PIN_ECHO = 11

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        print('Input time until scan commences.') # Line prompting user to input time in seconds

        scantime = input() # Edited original code here to wait for user input

        time.sleep(int(scantime))

        print('Calculating Distance')

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
        pulse_duration = pulse_end_time -pulse_start_time
        distance = round(pulse_duration * 17150, 2)

        led()

        try:
                loop()
        except KeyboardInterrupt:
                destroy()
                
finally:
        GPIO.cleanup()
