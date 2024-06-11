import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def display_welcome_message():
    lcd.clear()
    lcd.move_to(3, 0)  # Adjust position as needed
    lcd.putstr("Welcome to")
    lcd.move_to(1, 1)  # Adjust position as needed
    lcd.putstr("my tutorial")
    # Remove the delay and clear to keep the message on the screen indefinitely

# Call the function to display the message
display_welcome_message()

# Keep the program running indefinitely
while True:
    utime.sleep(1)
