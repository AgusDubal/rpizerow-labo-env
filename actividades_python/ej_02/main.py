#Importo las funciones LED y sleep de las librerías gpiozero y time respectivamente
from gpiozero import LED
from time import sleep

#Defino los pines asignados para cada color del LED
ledverde = LED(13)
ledrojo = LED(19)
ledazul = LED(26)

while True:

	#Prendo el LED verde y 250ms despues apago el LED rojo
	ledverde.on()
	sleep(0.25)
	ledrojo.off()

	#Prendo el LED azul y  500ms despues apago el LED verde
	ledazul.on()
	sleep(0.5)
	ledverde.off()

	#Prendo el LED rojo y 1s despues apago el LED azul
	ledrojo.on()
	sleep(1)
	ledazul.off()

