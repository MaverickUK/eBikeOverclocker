from machine import Pin
import time

# Bike Underclocker
# Peter Bridger
# April 2022

led = Pin(25, Pin.OUT)
relay = Pin(6, Pin.OUT)
sensor = Pin(15, Pin.IN, Pin.PULL_UP)

# Recalculate every period
maxLoopPeriod = 100

# Reduce speed by 75%
overclockRatio = 0.75 

overclock = 0
loop = 0
sensorCount = 0
lastStateOn = False
pulseFrequency = 0

print("Start up complete")

while True:
    time.sleep(0.01)
    
    sensorOn = sensor.value() == False
    
    if sensorOn:
        # Sensor detection
        if not lastStateOn:
            print('@', end ="")
            sensorCount+=1
        
    # Record last sensor state for next loop
    lastStateOn = sensorOn
    
    # Recalculate pulse
    if loop == maxLoopPeriod:
        if sensorCount > 0:
            overclock = sensorCount * overclockRatio
            pulseFrequency = int(maxLoopPeriod / overclock)

            print()
            print('Sensor count: ' + str(sensorCount))
            print('Overclock: ' + str(overclock))
            print('Pulse frequency: ' + str(pulseFrequency))
        else:
            pulseFrequency = 0 # Not moving
            
        # Reset
        sensorCount = 0
        loop = 0
        print('/')
    
    # Emit pulse
    if pulseFrequency > 0 and loop % pulseFrequency == 0:
        print('#', end ="")
        led.high()
        relay.high()
    else:
        print('_', end ="")
        led.low()
        relay.low()
        
    loop+=1

