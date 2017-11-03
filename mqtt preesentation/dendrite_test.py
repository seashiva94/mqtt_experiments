import time
from cloudmesh.pi import GroveRelay
import sys
from multiprocessing import Pool
from thread import start_new_thread
import grovepi

states = {"FREE" :0, "RECOVERING" :1, "WORKING":2}

class Dendrite:
	def __init__(self, pin = 3, recovery_time = 20, max_on_time = 0.5):
		self.dendrite = pin
		self.recovery_time = recovery_time
		grovepi.pinMode(self.dendrite,"OUTPUT")
		self.setState(states["FREE"])
		self.max_on_time = max_on_time
		#self.pool = Pool()
		print "INIT"

	def recover(self):
		print "recovering"
		time.sleep(self.recovery_time)
		print "recovered"
		self.setState(states["FREE"])
		#return states["FREE"]

	def on_wait(self):
		print "state = " , self.state,  "WAITING"
		time.sleep(self.max_on_time)
		print "max_on_time reached"
		self.off()

	def on(self):
		print "ON called at state", self.state
		if self.state == states["FREE"]:
			self.setState(states["WORKING"])
			grovepi.digitalWrite(self.dendrite,1)
			start_new_thread(self.on_wait,())
		else:
			print "BUSY"

	def off(self):
		print "OFF called at state", self.state

		grovepi.digitalWrite(self.dendrite,0)
		if self.state == states["WORKING"]:
			self.setState(states["RECOVERING"])
			# recover asynchronously and set state to free when recovered
			#self.pool.apply_async(self.recover, [], self.setState)
			start_new_thread(self.recover,())
		else:
			print "RELAXING"

	def setState(self,state):
		self.state = state
		print "state =" ,state


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Error"
		print "usage: dendrite_test.py <heating time in seconds>"
		exit()

	heat_time = float(sys.argv[1])

	dendrite0 = Dendrite(pin=2, recovery_time = 2)
	#dendrite1 = Dendrite(pin=4, recovery_time = 1)
	#dendrite2 = Dendrite(pin=6, recovery_time = 1)
	#dendrite3 = Dendrite(pin=8, recovery_time = 1)

	#dendrites = [dendrite0, dendrite1, dendrite2, dendrite3]
	"""
	msg = "ON ON ON ON"
	m_list = msg.split(" ")
	for i in range(len(dendrites)):
		if  m_list[i] == "ON":
			dendrites[i].on()
		else:
			dendrites[i].off()

	time.sleep(heat_time)
	for dendrite in dendrites:
		dendrite.off()

	"""
	dendrite0.on()
	#time.sleep(2)
	#dendrite0.off()
	time.sleep(20)
