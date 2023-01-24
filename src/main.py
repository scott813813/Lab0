"""!
@file main.py
This file contains code which increases and decreases the brightness of the LED on pin A0 over an interval of ten second.

@author Gabriel Ahern & Scott Brown
@date   23-Jan-2258 SPL Original file
@copyright (c) 2258 by Nobody and released under GNU Public License v3
"""

import pyb

def led_setup():
    
    """!
    Setup the LED channel on pin A0
    @returns channel 1
    """
    
    # Prepare the PWM timer and channel for use
    pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP) # Set output pin
    
    tim2 = pyb.Timer(2, freq=20000) # Set timer 2
    
    ch1 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0) # Set channel 1
    return ch1
    
def led_brightness(t):
    
    """!
    Setup the LED channel on pin A0
    @parameters the time interval
    @returns the brightness of the LED
    """
    
    ledb = t/50 # Divide by 50 because we are using time in milliseconds
    return ledb
    
def main():
    
    """!
    Increase and then decrease the brightness of the LED on pin A0.
    """
    
    ch1 = led_setup()
    tInit = pyb.millis()
    gg = True

    while(True): # Count upwards/increase brightness
        if(gg == True):
            cTime = pyb.millis() - tInit # Increase time
            ch1.pulse_width_percent(led_brightness(cTime)) # Set duty cycle
            if(cTime >= 5000):
                gg = False # Swap to decrease the brightness
                tInit = pyb.millis() # Reset initialized time
                
        else: # Count downwards/decrease brightness
            cTime = 5000 - (pyb.millis() - tInit) # Decrease time
            ch1.pulse_width_percent(led_brightness(cTime)) # Set duty cycle
            if(cTime <= 0):
                gg = True # Swap to increase the brightness
                tInit = pyb.millis() # Reset initialized time

# The following code only runs if this file is run as the main script;
# it does not run if this file is imported as a module
if __name__ == "__main__":
    main()