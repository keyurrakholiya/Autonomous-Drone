import RPi.GPIO as GPIO
import time

def initialize():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	
	print 'RPi_PinMap- 7: Rudder, 11: Pitch, 12: Throttle, 15: Yaw, 16: AUX'

	op_freq_th = 417
	op_freq_rpy = 527
	op_freq_aux = 496
	min_time_val_th = 1100
	max_time_val_th = 2400
	min_time_val_rpy = 1100
	max_time_val_rpy = 1900
	rpy_mid = 1500
	min_time_val_aux = 1015
	max_time_val_aux = 2018
	base_dc_th= (min_time_val_th /  max_time_val_th) * 100
	base_dc_rpy = (rpy_mid / max_time_val_rpy) * 100
 
	r = GPIO.PWM(7, op_freq_rpy)
	p = GPIO.PWM(11, op_freq_rpy)
	t = GPIO.PWM(12, op_freq_th)
	y = GPIO.PWM(15, op_freq_rpy)
	a = GPIO.PWM(16, op_freq_aux)
	
	r.start(base_dc_rpy)
	time.sleep(0.01)
	
	p.start(base_dc_rpy)
	time.sleep(0.01)
	
	y.start(base_dc_rpy)
	time.sleep(0.01)
	
	t.start(base_dc_th)
	time.sleep(0.01)
	
	a.start(100)
	time.sleep(0.01)
	
	print 'Setup Complete'
	print 'System ready to be Armed'
	print 'Self Level is configured as ON'

def system_arm():
	t.ChangeDutyCycle(0)

	y.ChangeDutyCycle((min_time_val_rpy/max_time_val_rpy) * 100)
	time.sleep(2)

	y.ChangeDutyCycle((rpy_mid/max_time_val_rpy) * 100)
	time.sleep(1)
	print 'System Armed'

def system_disarm():
	t.ChangeDutyCycle(0)

	y.ChangeDutyCycle(100)
	time.sleep(2)

	y.ChangeDutyCycle((rpy_mid/max_time_val_rpy) * 100)
	time.sleep(1)
	print 'System Disarmed'

initialize()
	
try:
	while True:
		string = raw_input ('Enter Command: ')
		word = string.split()
		word1 = word[0]
		
		if word1 == 'INIT':
			initialize()
		
		elif word1 == 'ARM':
			system_arm()
		
		elif word1 == 'TH':
			word2 = int(word[1])
			t.ChangeDutyCycle((word2/max_time_val_th) * 100)
			print 'TH: ' + word2
		
		elif word1 == 'RO' or 'AI':
			word2 = int(word[1])
			r.ChangeDutyCycle((word2/max_time_val_rpy) * 100)
			print 'RO or AI: ' + word2
	
		elif word1 == 'PI' or 'EL':
			word2 = int(word[1])
			p.ChangeDutyCycle((word2/max_time_val_rpy) * 100)
			print 'PI or EL: ' + word2
			
		elif word1 == 'YA' or 'RU':
			word2 = int(word[1])
			y.ChangeDutyCycle((word2/max_time_val_rpy) * 100)
			print 'YA or RU: ' + word2
			
		elif word1 == 'AUX':
			if word2 == 'ON':
				a.ChangeDutyCycle(100)
				print 'Self Level is ON'
			elif word2 == 'OFF':
				a.ChangeDutyCycle((min_time_val_aux/max_time_val_aux) * 100)
				print 'Self Level is OFF'
			
		elif word1 == 'DARM':
			system_disarm()
		
		elif word1 == 'STOP':
			system_disarm()
			break
		
		else:
			print 'Wrong Input'
		
		time.sleep(0.1)
		
except KeyboardInterrupt:
		pass

r.stop()
p.stop()
y.stop()
t.stop()

print 'System Stopped'

GPIO.cleanup()
