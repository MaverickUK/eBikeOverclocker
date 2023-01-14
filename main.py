from machine import Pin
import time

# RDF device (Reality Distrotion Field)
# Peter Bridger
# April 2022

led = Pin(25, Pin.OUT)
relay = Pin(6, Pin.OUT)
sensor = Pin(15, Pin.IN, Pin.PULL_UP)

# ============== Settings ==============
# Recalculate every period
maxLoopPeriod = 400

# Reduce speed by 75%
overclockRatio = 0.75

# Simulate a specifc sensor count for debugging
simulateSensorCount = None

debugMode = False

# Acceptable pulse values to prevent stuttering
# Higher is faster
pulseValues = [0,1,2,4,5] # ,8] # ,10] # , 20]


# 5 = 12.5mph
# 4 = 10mph
# 2 = 5mph
# 1 = 2.5mph
# 0 = 0mph

pulseExtendBy = 5 # Loops

# ============== Variables =============
loop = 0 # Count current loop
sensorCount = 0 # Number of actual sensor pulses within loop
lastStateOn = False # Used to determine if sensor state has changed between loops
pulseFrequency = 0 # Calcuated simulated pulse frequency
pulseExtendCount = 0 # How many loops has the electromagnet been extended
# ======================================

def debug(output, newline = False):
    if debugMode:
        if newline:
            print(output)
        else:
            print(output, end ="")
            
# Round pulse up/down to nearest value on list
# https://www.entechin.com/find-nearest-value-list-python/
def smoothedPulse(input):
  pulseValues.sort(reverse=True)
  difference = lambda pulseValues : abs(pulseValues - input)
  res = min(pulseValues, key=difference)
  return res            

debug("Start up complete", True)

while True:
    # time.sleep(0.01)
    time.sleep(0.005)
    
    sensorOn = sensor.value() == False
    
    if sensorOn:
        # Sensor detection
        if not lastStateOn:
            debug('@')
            sensorCount+=1
        
    # Record last sensor state for next loop
    lastStateOn = sensorOn
    
    # Debug
    if simulateSensorCount is not None:
        sensorCount = simulateSensorCount
    
    # Recalculate pulse
    if loop == maxLoopPeriod:
        if sensorCount > 0:
            # Alter the pulse by overclock ratio
            overclockPulse = sensorCount * overclockRatio
            
            # Round to nearest value in list
            overclockPulse = smoothedPulse(overclockPulse)            
            
            # Convert to a frequency to be pulsed with in loop period
            pulseFrequency = int(maxLoopPeriod / overclockPulse)
            
            debug("", True)
            debug('Sensor count: ' + str(sensorCount), True)
            debug('Overclock pulse: ' + str(overclockPulse), True)
            debug('Pulse frequency: ' + str(pulseFrequency), True)
        else:
            pulseFrequency = 0 # Not moving
            
        # Reset
        sensorCount = 0
        loop = 0
        debug('/')
    
    # Emit pulse
    emitPulse = False
    
    if pulseFrequency > 0 and loop % pulseFrequency == 0:
        emitPulse = True
    elif pulseExtendCount > 0:
        emitPulse = True

   
    if emitPulse:
        debug('#')
        led.high()
        relay.high()
        pulseExtendCount += 1
        
        # Reset - if extension of pulse reached
        if pulseExtendCount >= pulseExtendBy:
            pulseExtendCount = 0
    else:
        debug('_')
        led.low()
        relay.low()
        
    loop+=1
