from gpiozero import LED, Button
from signal import pause

#Asigno los pines al LED y el botón#
led = LED(13)
button = Button(18)

#Utilizo las funciones "Button" que importé desde "gpiozero" para declarar que cuando el botón esté presionado, se prenda el LED,
#y cuando no lo esté, que el LED se apague
button.when_pressed = led.on
button.when_released = led.off

pause()
