from machine import Pin, PWM
import time
from time import sleep
import dht

#Rui Santos & Sara Santos - Random Nerd Tutorials
#Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-servo-motor-micropython/

#Set up PWM Pin for servo control
servo_pin = machine.Pin(0)
servo = PWM(servo_pin)

#Set Duty Cycle for Different Angles
max_duty = 7864
min_duty = 1802
half_duty = int(max_duty/2)

#Set PWM frequency
frequency = 50
servo.freq (frequency)



sensor = dht.DHT22(Pin(16))
                   
try:
    while True:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)

        if temp <= 24:
            #Servo at 0 degrees
            servo.duty_u16(min_duty)
            sleep(2)
        elif temp <= 26:
            #Servo at 90 degrees
            servo.duty_u16(half_duty)
            sleep(2)
        else:
            #Servo at 180 degrees
            servo.duty_u16(max_duty)
            sleep(2)
        
        sleep(5)
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    #Turn off PWM 
    servo.deinit()
