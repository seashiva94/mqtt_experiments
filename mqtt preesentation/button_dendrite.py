####
# Connect button on port D5 of grovepi
# connect relay of the dendrite on port D3 of grovepi
# program waits for a buton press
# if button is pressed it tries to turn the dendrite on
# if the denrite is in recovered state, it gets turned on and plant bows down
####
from dendrite import Dendrite
from cloudmesh.pi import Button
import time

dendrite = Dendrite(3, recovery_time= 10, max_on_time = 2.5)
b = Button(5)

pressed = 0
while True:
	print "\n\n--- Waitig for button press ---"
	val = 0
	while not pressed:
		val = b.get()
		pressed = val
	if val:
		dendrite.on()
	pressed = 0
	time.sleep(1)

