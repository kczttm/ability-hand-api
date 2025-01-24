from AbilityHandSerialClient import *
import time

abh = AbilityHandSerialClient(baudrate=460800, noprint=1)
abh.reply_mode=2	#1, 2, or 3
abh.create_read_thread()

print("Index Targ, Index Pos, time")
try:
	fpos = np.array([30.,30.,30.,30.,30.,-30.])
	start_time = time.time()
	while(True):

		for i in range(0, len(fpos)):
			ft = time.time()*1 + i*(2*np.pi)/12
			fpos[i] = (.5*np.sin(ft)+.5)*45. + 15.
		fpos[5] = -fpos[5]

		abh.writePos()
		with abh.readlock:
			if(len(abh.rPos) != 0):
				abh.tPos = fpos
				ps = ""
				
				ps = ps + str(fpos[0])+", "+str(abh.rPos[0])+","+str( time.time() - start_time )
				print(ps)
				# time.sleep(.0001)

except KeyboardInterrupt:
	abh.close()
