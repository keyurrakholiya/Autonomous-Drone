import cv2
import numpy as np
from RPIO import PWM
import time
import io
import picamera
import picamera.array

# initialize servo objects with PWM function
roll = PWM.Servo()
pitch = PWM.Servo()
throttle = PWM.Servo()
yaw = PWM.Servo()
aux = PWM.Servo()

# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(17,1520)# pin 11
pitch.set_servo(18,1520)# pin 12
throttle.set_servo(27,1100)# pin 13, pin 14 is Ground
yaw.set_servo(22,1520)# pin 15
aux.set_servo(23,1010)# pin 16

# assign global min and max values
th_min = 1100
th_max = 2400
r_min = 1100
r_max = 1900
p_min = 1100
p_max = 1900
y_min = 1100
y_max = 1900
a_min = 980
a_max = 2300
th = 1100
r = 1520
p = 1520
y = 1520
a = False
th1 = 0
bot_in_bounds = False

# initialize picamera objects
camera=picamera.PiCamera()
camera.resolution = (160,120)

stream= io.BytesIO()

try:
    while True:
        string = raw_input ('Enter Command: ')
        word = string.split()
        word1 = word[0]
        
        if word1 == 'ARM':
	    th = 1100
            throttle.set_servo(27,th)
            time.sleep(1)
            yaw.set_servo(22,1100)
            time.sleep(1)
            yaw.set_servo(22,1520)
            time.sleep(1)
            print 'System is armed'
            continue

        elif word1 == 'FLY':

            # mapping for MANUAL MODE
            if word[1] == 'MANUAL':
                print 'Flight control: MANUAL'

                try:
                    while True:
                        camera.capture(stream, format="bgr", use_video_port=True)
                        frame = np.fromstring(stream.getvalue(), dtype=np.uint8)
                        stream.seek(0)
                        frame= stream.array
                        cv2.imshow('frame',frame)

                        k = cv2.waitKey(1)

                        # mapping TH = UP
                        if (k & 0xFF) == ord('w'):
                            th = th + 10
                            if (th < th_min):
                                throttle.set_servo(27,1100)
                                th = 1100
                            elif (th > th_max):
                                throttle.set_servo(27,2400)
                                th = 2400
                            elif (th > th_min & th < th_max):
                                throttle.set_servo(27,th)
                            print 'TH: ' + str(th)
                            continue

                        # mapping TH = DOWN
                        if (k & 0xFF) == ord('s'):
                            th = th - 10
                            if (th < th_min):
                                throttle.set_servo(27,1100)
                                th = 1100
                            elif (th > th_max):
                                throttle.set_servo(27,2400)
                                th = 2400
                            elif (th > th_min & th < th_max):
                                throttle.set_servo(27,th)
                            print 'TH: ' + str(th)
                            continue

                        # mapping YA = LEFT
                        if (k & 0xFF) == ord('a'):
                            y = y - 10
                            if (y < y_min):
                                yaw.set_servo(22,1100)
                                y = 1100
                            elif (y > y_max):
                                yaw.set_servo(22,1900)
                                y = 1900
                            elif (y > y_min & y < y_max):
                                yaw.set_servo(22,y)
                            print 'YA: ' + str(y)
                            continue

                        # mapping YA = RIGHT
                        if (k & 0xFF) == ord('d'):
                            y = y + 10
                            if (y < y_min):
                                yaw.set_servo(22,1100)
                                y = 1100
                            elif (y > y_max):
                                yaw.set_servo(22,1900)
                                y = 1900
                            elif (y > y_min & y < y_max):
                                yaw.set_servo(22,y)
                            print 'YA: ' + str(y)
                            continue

                        # mapping PI = UP
                        elif (k & 0xFF) == ord('8'):
                            p = p + 10
                            if (p < p_min):
                                pitch.set_servo(18,1100)
                                p = 1100
                            elif (p > p_max):
                                pitch.set_servo(18,1900)
                                p = 1900
                            elif (p > p_min & p < p_max):
                                pitch.set_servo(18,p)
                            print 'PI: ' + str(p)
                            continue
            
                        # mapping PI = DOWN
                        if (k & 0xFF) == ord('2'):
                            p = p - 10
                            if (p < p_min):
                                pitch.set_servo(18,1100)
                                p = 1100
                            elif (p > p_max):
                                pitch.set_servo(18,1900)
                                p = 1900
                            elif (p > p_min & p < p_max):
                                pitch.set_servo(18,p)
                            print 'PI: ' + str(p)
                            continue

                        # mapping RO = LEFT
                        if (k & 0xFF) == ord('4'):
                            r = r - 10
                            if (r < r_min):
                                roll.set_servo(17,1100)
                                r = 1100
                            elif (r > r_max):
                                roll.set_servo(17,1900)
                                r = 1900
                            elif (r > r_min & r < r_max):
                                roll.set_servo(17,r)
                            print 'RO: ' + str(r)
                            continue

                        # mapping RO = RIGHT
                        if (k & 0xFF) == ord('6'):
                            r = r + 10
                            if (r < r_min):
                                roll.set_servo(17,1100)
                                r = 1100
                            elif (r > r_max):
                                roll.set_servo(17,1900)
                                r = 1900
                            elif (r > r_min & r < r_max):
                                roll.set_servo(17,r)
                            print 'RO: ' + str(r)
                            continue

                        # mapping for NO KEY
                        if k == -1:
			    if th1 != th:
                                throttle.set_servo(27,th)
                            else:
                                pass
                            if r != 1520:
                                roll.set_servo(17,1520)
                            else:
                                pass
                            if p !=1520:
                                pitch.set_servo(18,1520)
                            else:
                                pass
                            if y != 1520:
                                yaw.set_servo(22,1520)
                            else:
                                pass
                            th1 = th
                            print 'STABLE'
                            continue

                        # mapping for AUX
                        if (k & 0xFF) == ord(' '):
                            a = not(a)
                            if a == True:
                                aux.set_servo(23,2300)
                                print 'Self Level is ON'
                            elif a == False:
                                aux.set_servo(23,980)
                                print 'Self Level is OFF'
                                continue

                        # mapping for BREAK CONDITION
                        if (k & 0xFF) == ord('j'):
                            aux.set_servo(23,2300)
                            throttle.set_servo(27,th)
                            roll.set_servo(17,1520)
                            pitch.set_servo(18,1520)
                            yaw.set_servo(22,1520)
                            break
                        
                        else:
                            continue
                                
                except KeyboardInterrupt:
                    pass

            # mapping for AUTO MODE    
            elif word2 == 'AUTO':
                print 'Flight control: AUTO'
                aux.set_servo(23,2300)
                print 'Self Level is ON'

                def nothing(x):
                    pass

                cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

                cv2.namedWindow('Trackbar', cv2.WINDOW_NORMAL)
                cv2.createTrackbar('HL','Trackbar',0,180,nothing)
                cv2.createTrackbar('SL','Trackbar',0,255,nothing)
                cv2.createTrackbar('VL','Trackbar',0,255,nothing)
                cv2.createTrackbar('HU','Trackbar',0,180,nothing)
                cv2.createTrackbar('SU','Trackbar',0,255,nothing)
                cv2.createTrackbar('VU','Trackbar',0,255,nothing)

                try:
                    while True:
                        camera.capture(stream, format="bgr", use_video_port=True)
                        frame = np.fromstring(stream.getvalue(), dtype=np.uint8)
                        stream.seek(0)
                        frame= stream.array
                        cv2.imshow('frame',frame)

                        # convert image frame to hsv
                        hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
                        
                        # get current positions of four trackbars
                        h_lower = cv2.getTrackbarPos('HL','Trackbar')
                        s_lower = cv2.getTrackbarPos('SL','Trackbar')
                        v_lower = cv2.getTrackbarPos('VL','Trackbar')
                        h_upper = cv2.getTrackbarPos('HU','Trackbar')
                        s_upper = cv2.getTrackbarPos('SU','Trackbar')
                        v_upper = cv2.getTrackbarPos('VU','Trackbar')
                        
                        # set upper and lower limits to color extraction
                        lower_eye = np.array([h_lower,s_lower,v_lower]) # values for frame
                        upper_eye = np.array([h_upper,s_upper,v_upper])# values for frame
                        
                        # detect blob
                        mask = cv2.inRange(hsv_img, lower_eye, upper_eye)

                        # apply morph technique to remove noise        
                        kernel = np.ones((5,5),np.uint8)
                        filtered_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

                        # find contours
                        contours, hierarchy = cv2.findContours(filtered_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

                        # set bounding rectangle
                        cv2.rectangle(frame,(16,12),(144,108),(255,0,0),1)
                        
                        # find biggest contour & draw
                        #cnt = contours[0]
                        # find contours and draw
                        cv2.drawContours(frame, contours, -1, (0,255,0), 1)
                        cv2.imshow('frame',frame)

                        # find biggest contour & draw
                        if len(contours) > 0:
                            for i in range(len(contours)):
                                cnt = contours[i]
                                M = cv2.moments(cnt)               
                                cx = int(M['m10']/(M['m00'] + 0.01))
                                cy = int(M['m01']/(M['m00'] + 0.01))
                                if (((cx > 15) & (cx < 145)) & ((cy > 11) & (cy < 109))):
                                    print 'Bot %s inside the boundary'%(i)
                                    if bot_in_bounds == False:
                                        roll.set_servo(17,1520)
                                        pitch.set_servo(18,1520)
                                        yaw.set_servo(22,1520)
                                        bot_in_bounds = True
                                    else:
                                        pass
                                elif ((cx < 15) & ((cy > 11) & (cy < 109))):
                                    print 'Bot %s straying to left of boundary'%(i)
                                    roll.set_servo(17,1590)
                                    bot_in_bounds = False
                                elif ((cx > 145) & ((cy > 11) & (cy < 109))):
                                    print 'Bot %s straying to right of boundary'%(i)
                                    roll.set_servo(17,1450)
                                    bot_in_bounds = False
                                elif (((cx > 15) & (cx < 145)) & (cy < 11)):
                                    print 'Bot %s  straying to above boundary'%(i)
                                    pitch.set_servo(18,1590)
                                    bot_in_bounds = False
                                elif (((cx > 15) & (cx < 145)) & (cy > 109)):
                                    print 'Bot %s straying to below boundary'%(i)
                                    pitch.set_servo(18,1450)
                                    bot_in_bounds = False
                                
                                #print 'center of %s: %s,%s'%(i,cx,cy)
                        
                        # show filtered image
                        cv2.imshow('filtered image', mask)
                        k = cv2.waitKey(1)
                        if (k & 0xFF) == ord('q'):
                            break
                        
                except KeyboardInterrupt:
                        pass

                
        elif word1 == 'DARM':
            throttle.set_servo(27,1100)
            time.sleep(1)
            yaw.set_servo(22,1900)
            time.sleep(1)
            yaw.set_servo(22,1520)
            time.sleep(1)
            print 'System is disarmed'

        elif word1 == 'LAND':
            throttle.set_servo(27,th-50)
            time.sleep(10)
            print 'The Eagle has landed!'
            break
        
##        elif word1 == 'STOP':
##            throttle.set_servo(15,1100)
##            time.sleep(1)
##            yaw.set_servo(15,1900)
##            time.sleep(2)
##            yaw.set_servo(15,1520)
##            time.sleep(1)
##            print 'System is disarmed'
##            time.sleep(1)
##            break
        
        else:
                print 'Wrong Input'
        
        time.sleep(0.1)
            
except KeyboardInterrupt:
	pass

finally:
    roll.stop_servo(17)
    pitch.stop_servo(18)
    throttle.stop_servo(27)
    yaw.stop_servo(22)
    aux.stop_servo(23)

    cv2.destroyAllWindows()
