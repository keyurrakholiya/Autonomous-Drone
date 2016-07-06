##########################################################################################################################
# Project : Autonomous Drone												#
# Hardware: Raspberry pi ,Arducopter , laptop or desktop ,ultrasonic sensor HC-SR04					#
#	  : Arducopter(APM2.6)												#
# Author  : Keyur Rakholiya												#
# Author  : Akshit Gandhi												#
#															#
# by using this code, quadcopter can controlled by using laptop keyboard. we can also change the different modes also   #												#
#															#
# Requrinment: Refer Tutorial Folder											#
#########################################################################################################################
from dronekit import connect, VehicleMode ,LocationGlobalRelative
import time
import getch
from RPIO import PWM


print "connecting to vehicle...."
vehicle = connect('/dev/ttyAMA0', baud = 57600)
print "connected"

#changing vehicle mode to stabilize
print "\nSet Vehicle.mode = (currently: %s)" % vehicle.mode.name
while not vehicle.mode=='STABILIZE':
    vehicle.mode = VehicleMode('STABILIZE')
    vehicle.flush()

print "vehicle mode: %s" % vehicle.mode

# ARMING the vehicle
vehicle.armed = True
while not vehicle.armed:
    vehicle.armed = True
    vehicle.flush()
    print " trying to change mode and arming ..."
    time.sleep(1)

print "its armed"

# initialize servo objects with PWM function
roll = PWM.Servo()
pitch = PWM.Servo()
throttle = PWM.Servo()
yaw = PWM.Servo()
mode = PWM.Servo()

# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(17,1520)# pin 11
pitch.set_servo(18,1520)# pin 12
throttle.set_servo(27,1100)# pin 13, pin 14 is Ground
yaw.set_servo(22,1520)# pin 15
mode.set_servo(26,1200)# pin 37
# assign global min and max values
th_min = 1100
th_max = 2000
r_min = 1100
r_max = 1900
p_min = 1100
p_max = 1900
y_min = 1100
y_max = 1900
a_min = 980
a_max = 2300
th =1100
r = 1520
p = 1520
y = 1520
a = False
flag = 0

#print "\nSet Vehicle.mode =  (currently: %s)" % vehicle.mode.name

print "Taking off!"
print "controll drone from keyboard"




try:
    while True:
# waiting for key strokes
        key = getch.getch()
        if key == 'w':
            
            th = th + 10
            if (th < th_min):
                th = 1100
                throttle.set_servo(27,th)
            elif (th > th_max):
                th = 2000
                throttle.set_servo(27,th)
            else: 
                throttle.set_servo(27,th)
            print 'th :' + str(th)
            
        elif key == 's':
            th = th - 10
            if (th < th_min):
                th = 1100
                throttle.set_servo(27,th)
            elif (th > th_max):
                th = 2000
                throttle.set_servo(27,th)
            else:
                throttle.set_servo(27,th)
            print 'th :' + str(th)

            #yaw left
        elif key == 'a':
            yaw.set_servo(22,1350)
	    print "yaw left"
            time.sleep(0.3)
            yaw.set_servo(22,1500)

        #yaw right
        elif key == 'd':
            yaw.set_servo(22,1650)
	    print "yaw right"
            time.sleep(0.3)
            yaw.set_servo(22,1500)

        #roll left
        elif key == '4':
            roll.set_servo(17,1350)
	    print "roll left"
            time.sleep(0.3)
            roll.set_servo(17,1500)

        #roll right
        elif key == '6':
            roll.set_servo(17,1650)
	    print "roll right"
            time.sleep(0.3)
            roll.set_servo(17,1500)
            
        #pitch forward
        elif key == '8':
            pitch.set_servo(18,1650)
	    print "pitch forward"
            time.sleep(0.3)
            pitch.set_servo(18,1500)
	#pitch back
	elif key == '2':
		pitch.set_servo(18,1350)
		print "pitch back"
		time.sleep(0.3)
		pitch.set_servo(18,1500)

        #atlitude hold
	elif key == 'h':
		mode.set_servo(26,1550)
		time.sleep(0.5)
		print " mode is %s" % vehicle.mode.name
		
      
	#land mode
	elif key == 'l':
		mode.set_servo(26,1800)
		time.sleep(0.5)
		print " mode is %s " % vehicle.mode.name
	#stabilize mode
	elif key =='5' and th<1200:
                mode.set_servo(26,1200)
                time.sleep(0.5)
                print "mode is %s" % vehicle.mode.name
                
except KeyboardInterrupt:
	throttle.set_servo(27,1100)
	while vehicle.armed:
		vehicle.armed = False
	        print "disarming"
		time.sleep(1)
		vehicle.flush()
print "DISARMED"
vehicle.close()
