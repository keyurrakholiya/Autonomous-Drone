##########################################################################################################################
# Project : Autonomous Drone												#
# Hardware: Raspberry pi 												#
#	  : Arducopter(APM2.6)												#
# Author  : Keyur Rakholiya												#
# Author  : Akshit Gandhi												#
#															#
# Drone will takeoff after running this code. and it will goes to cirtain height(adjustable) and after cirtain time it  #
# will land on the ground.												#
#															#
# Requrinment: Refer Tutorial Folder											#
#########################################################################################################################

from dronekit import connect, VehicleMode ,LocationGlobalRelative
import time
from RPIO import PWM
vehicle = connect('/dev/ttyAMA0', baud = 57600)
throttle = PWM.Servo()

#vehicle must be in guided mode because we are using dronekit library for changing vehicle's mode. NOT PWM.

print "\nSet Vehicle.mode = (currently: %s)" % vehicle.mode.name

#this loop will change the mode of vehicle
while not vehicle.mode=='GUIDED':
    vehicle.mode = VehicleMode('GUIDED')
    vehicle.commands.upload()

print "vehicle mode: %s" % vehicle.mode

#this while loop is for arming the vehicle
vehicle.armed = True
while not vehicle.armed:
    vehicle.armed = True
    vehicle.flush()
    print " trying to change mode and arming ..."
    time.sleep(1)

print "its armed"
print "\nSet Vehicle.mode =  (currently: %s)" % vehicle.mode.name
print "Taking off!"

vehicle.simple_takeoff(2) # Take off to target altitude,here is 2meter

try:
	while True:
		altitude = vehicle.location.global_relative_frame.alt
		print " Altitude: ", altitude
		print "sensors:",vehicle.attitude

        	if vehicle.location.global_relative_frame.alt>=2*0.95: 
	            	print "Reached target altitude"
			print "Final Altitude:", vehicle.location.global_relative_frame.alt
        	    	break
        		time.sleep(1)

#it will hold the altitude for 2 seconds
	time.sleep(2)
	
#it will now goes to in land mode
	while not vehicle.mode=='LAND':
    		vehicle.mode = VehicleMode('LAND')
    		vehicle.commands.upload()
except Keyboardinterrupt:
	throttle.set_servo(27,1100)
print "\nSet Vehicle.mode =  (currently: %s)" % vehicle.mode.name
print vehicle.armed
vehicle.close()
print vehicle.armed
