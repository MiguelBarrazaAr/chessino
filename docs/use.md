# Como se usa Chessino

Chessino es un reloj de ajedrez libre hecho en la [UNQ](http://www.unq.edu.ar/) con tecnologías libres.  
Su hardware está hecho con Raspberry y Arduino.  
Cuenta con un display (pantalla) y 5 botones que está distribuido de la siguiente forma.  
2 botones superiores (en la parte de arriba del dispositivo) de 4.6 cm que son para pasar turno.  
2 botones inferiores (al lado del display) de 3 cm que es para decir el tiempo.  
y un botón pequeño en la zona central que es para el menú.  
por defecto los botones de la derecha del display son para el jugador de piezas blancas. y los de la izquierda son para el jugador de piezas negras.  
Si es el turno de las blancas, y el jugador de piezas negras pulsa el botón de pasar turno, se escuchará un sonido de error, pero no pasará el turno. Tampoco podrá pulsar el botón de escuchar tiempo, quedará inhabilitado. Solo se podrá pulsar los botones del jugador que tiene el tiempo vigente.

## Navegación por el menú

Al entrar al menú, el mismo botón central sirve para salir.
el botón superior derecha es el botón "+" (más) y el de la izquierda el "-" (menos), que sirven para moverte por las opciones del menú.  
Los botones de abajo son para incrementar (botón derecha) y decrementar (el botón izquierda) o también sirven para dar enter (seleccionar una opción)

## Futuras mejoras

Esta es una versión primera de el software Chessino, se nos ocurre futura mejoras para ahcerle.

* Traducir el message.json a otros idiomas, para que se tenga audios en otros idiomas.
* Agregar la opción de invertir botones: para poder poner el reloj a la derecha o izquierda del tablero.
* conectar los botones a los pines de la raspberry para usar solo una placa o usar un microcontrolador con mayor potencia que pueda reproducir audio y cargar el script python como el esp32.
* agregar mas audios de voces.
* conectar con un servidor para seguirlo por una web cuanto queda de tiempo.
* conectarlo con un bot como el de telegram o facebook para que un juez pueda ir escribiendo los movimientos y ir registrando en la web el progreso de tiempo y cada movimiento.

Chessino es un proyecto de software y hardware libre. No se permite la comercialización.

* [Ir al inicio](../index.md)