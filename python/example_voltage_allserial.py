from AbilityHandSerialClient import *
import time

abh = AbilityHandSerialClient(baudrate=460800)
abh.reply_mode=2	#1, 2, or 3
abh.create_read_thread()

print("beginning test")
try:
	fpos = np.array([30,30,30,30,30,-30])
	while(True):

		for i in range(0, len(fpos)):
			ft = time.time()*3 + i*(2*np.pi)/12
			fpos[i] = (.5*np.sin(ft)+.5)*45+15
		fpos[5] = -fpos[5]

		abh.writeVoltageDuty()
		with abh.readlock:
			if(len(abh.rPos) != 0):
				abh.tVoltageDuty = (fpos-abh.rPos)*0.01 - abh.rVelocity*.0001
				print(abh.rPos)
				# time.sleep(.0001)

except KeyboardInterrupt:
	abh.close()
	print("stopping")
