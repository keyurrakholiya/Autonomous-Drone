from dronekit import connect, VehicleMode ,LocationGlobalRelative
import time

vehicle = connect('/dev/ttyAMA0', baud = 57600)


print "\nSet Vehicle.mode = GUIDED (currently: %s)" % vehicle.mode.name
while not vehicle.mode=='GUIDED':
    vehicle.mode = VehicleMode('GUIDED')
    vehicle.commands.upload()

print "vehicle mode: %s" % vehicle.mode
"""vehicle is ARMABLE??
print "Basic pre-arm checks"

# Don't try to arm until autopilot is ready
while not vehicle.is_armable:
    print " Waiting for vehicle to initialise..."
    time.sleep(1)
print "vehicle is armable"
"""




vehicle.armed = True
while not vehicle.armed:
    vehicle.armed = True
    vehicle.flush()
    print " trying to change mode and arming ..."
    time.sleep(1)

print "its armed"
"""
while not vehicle.mode=='STABILIZE':
    vehicle.mode = VehicleMode('STABILIZE')
    vehicle.commands.upload()
"""
print "\nSet Vehicle.mode =  (currently: %s)" % vehicle.mode.name
"""
while True:
	print vehicle.rangefinder
"""
print "Taking off!"
vehicle.simple_takeoff(2) # Take off to target altitude

while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=2*0.95: 
            print "Reached target altitude"
            break
        time.sleep(1)
"""
print "\nChannel overrides: %s" % vehicle.channels.overrides
print "Set Ch1-Ch8 overrides to 110-810 respectively"
vehicle.channels.overrides = {'1': 110, '2': 210,'3':1500,'4':410, '5':510,'6':610,'7':710,'8':810}
print " Channel overrides: %s" % vehicle.channels.overrides
"""
time.sleep(10)
while not vehicle.mode=='LAND':
    vehicle.mode = VehicleMode('LAND')
    vehicle.commands.upload()

print "\nSet Vehicle.mode =  (currently: %s)" % vehicle.mode.name
print vehicle.armed
##while vehicle.armed:
##    vehicle.armed = False
##    print "disarming"
##    vehicle.flush()
##print "DISARMED"
vehicle.close()
print vehicle.armed
