import time
import RPi.GPIO as GPIO

#set up GPIO pins
GPIOpin = -1

#set up raspberry pi
GPIO.setmode(GPIO.BCM)

#set up pins
GPIO.setup(GPIOpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def moveActuators():
    print("Moved Actuators")

# Detect Piece
def detectPiece():
    if(GPIOpin != -1):
        state = GPIO.input(GPIOpin)
        if state:
            moveActuators()
        else :
            print("part is not detected")

def laserSensor():

    while GPIO.input(GPIOpin)==1:
        Current_State = 0 #not triggered
        Current_State = GPIO.input(GPIOpin) #normally open/closed pin 
        if Current_State == 1 and Previous_State == 0:
            #motion detected, triggered state
            Previous_State = 1 #triggered state
        elif Current_State == 0 and Previous_State == 1:
            Previous_State = 0 #stops being triggered

    # Wait for 10 milliseconds
    time.sleep(0.01)




if __name__ == '__main__':
    #FOR THE BOTTOM PART
    #proximity sensor to sense place - u shape first
    #actuators push
    #clamps engage

    #LEFT SIDE
    #proximity confirms detection
    #laser checks
    #Actuator pushes till laser is no longer in triggered state
    #Laser will tell clamp engages

    #RIGHT
    #proximity confirms detection
    #laser checks
    #Actuator pushes till laser is no longer in triggered state
    #Laser will tell clamp engages
    