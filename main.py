from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=5, echo_pin=18)

distance = sensor.distance_mm()

print('Distance:', distance, 'mm')
