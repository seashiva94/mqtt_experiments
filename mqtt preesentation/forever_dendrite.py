from dendrite import Dendrite
import time

dendrite = Dendrite(3, recovery_time=10, max_on_time=2)
while True:
	dendrite.on()
	time.sleep(2)
