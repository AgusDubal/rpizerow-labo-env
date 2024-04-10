from gpiozero import LED
from time import sleep

ledverde = LED(13)
ledrojo = LED(19)
ledazul = LED(26)

while True:
	ledverde.on()
	sleep(0.25)
	ledrojo.off()


	ledazul.on()
	sleep(0.5)
	ledverde.off()


	ledrojo.on()
	sleep(1)
	ledazul.off()

