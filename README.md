La versión de Python utilizada para realizar el juego fue PYTHON 3.6

Pygame versión 1.9.3

Pyserial 3.4

NO eliminar nada de esta carpeta para que el juego funcione correctamente.

Para jugar:

-Controlar el jugador 1: con las teclas "w" y "s" o con el Control del jugador 1

-Controlar el jugador 2: con las teclas "Flecha Arriba" y "Flecha Abajo" o con el Control del jugador 2

Es necesario tener Pygame y Pyserial instalados y utilizar el programa en windows, ya que se utiliza la librería winsound es cierta parte del juego

Descarga Pygame de aqui https://www.pygame.org/download.shtml, elije un archivo .msi o .exe, que sea compatible con tu computadora (32 o 64 bits)

Para instalar Pyseria es necesario utilizar pip y usar el comando: pip install serial

En caso de tener errores se le sugiere instalar Pycharm desde aqui https://www.jetbrains.com/pycharm/download/#section=windows, desde ahí se puede acceder a las configuraciones y se pueden elegir cuales paquetes instalar, entre ellos Pygame.

Errores conocidos:

-A veces, en el nivel 3 principalmente, se producirá un error de índices cuando se va a golpear la bola de cierta manera, por ejemplo, si la bola viene hacia uno y se intenta golpear (todo se mueve muy rápido en ese momento), se producirá un problema en cual la posicion de la bola y la posicion de la barra serán la misma, eso no puede suceder y se cae el programa. Ocurre rara vez en el nivel 3.
