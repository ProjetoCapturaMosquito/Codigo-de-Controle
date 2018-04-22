import RPi.GPIO as GPIO
import time

SERVO_PIN = 32

def start_motor(initial_position):
    # Starting the PWM and setting the initial position of the servo with 50Hz frequency 
    servo = GPIO.PWM(SERVO_PIN,initial_position)
    servo.start(0)
    
    return servo
    
def open_door(servo):
    try:
        # Changing the Duty Cycle to rotate the motor 
        servo.ChangeDutyCycle(7.5)
	# Sleep for 5 Seconds 
        time.sleep(3)
        servo.ChangeDutyCycle(12.5)
        time.sleep(3)
        servo.ChangeDutyCycle(2.5)
        time.sleep(3)

    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
        quit()
    
def close_door(servo):
    try:
        # Changing the Duty Cycle to rotate the motor 
        servo.ChangeDutyCycle(7.5)
	# Sleep for 5 Seconds 
        time.sleep(3)
        servo.ChangeDutyCycle(12.5)
        time.sleep(3)
        servo.ChangeDutyCycle(2.5)
        time.sleep(3)

    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
        quit()

def main():
    # Setting the GPIO Mode to BOARD => Pin Count Mapping 
    GPIO.setmode(GPIO.BOARD)
    
    # Setting the GPIO Mode to BCM => GPIO Mapping 
    # Uncomment below line for to use GPIO number
    # GPIO.setmode(GPIO.BCM)

    # Setting the GPIO 18 as PWM Output 
    GPIO.setup(SERVO_PIN,GPIO.OUT)
    
    # Disable the warning from the GPIO Library
    GPIO.setwarnings(False)
    
    # Calibrar com a porta
    initial_position = 50
    servo = start_motor(initial_position)
    
    start(peltier)
    
    while True:
        if (cicle == 12):
            get_pics()
        
        if (cicle == 24):
            start(cooler_motor)
            open_door(cooler_servo)
            
            time.sleep(1)
            
            close_door(cooler_servo)
            stop(cooler_motor)
            
            cicle = 0
        
        time.sleep(5)
        
        start(cooler_motor)
        open_door(servo)
        
        time.sleep(1)
        
        close_door(servo)
        stop(cooler_motor)
        
        temp = getTemp()
        
        if (temp < 5):
            stop(peltier)
        if (temp > 5):
            start(peltier)
        
        cicle++

main()
        