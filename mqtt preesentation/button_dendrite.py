from dendrite import Dendrite
from cloudmesh.pi import Button
import time

dendrite = Dendrite(3, recovery_time= 10, max_on_time = 2.5)
b = Button(5)

while True:
	val = b.get()
	if val:
		dendrite.on()
	time.sleep(1)

