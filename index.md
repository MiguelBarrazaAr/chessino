# Chessino

* [Inicio](index.md)
* [como se usa](docs/use.md)
* [Menú](docs/menu.md)
* [sonidos](docs/ui-sounds.md)

## Reloj de Ajedrez
  Es un dispositivo que sirve para contabilizar el tiempo invertido por cada jugador al pensar sus jugadas durante una partida de ajedrez. Previamente se pacta el ritmo del juego, y pierde por tiempo el jugador que no haya hecho hackemate y se haya quedado sin tiempo.  
Surge para controlar el tiempo total que puede durar una partida. Antes de su introducción las partidas podían alargarse durante horas y horas (e incluso días) ya que cada jugador podía pensar todo el tiempo que considerase conveniente.

## Modo de uso
  Después de cada jugada, el jugador aprieta un botón que desactiva su cronómetro y simultáneamente activa el de su adversario.  
La puesta en marcha del reloj se debe de hacer con la misma mano que se juegan las piezas; sin embargo no es obligatorio presionarlo, de modo y manera que si un jugador se olvida de hacerlo el adversario puede hacer su jugada cuando lo considere oportuno. No obstante lo dicho, siempre se debe de permitir que el adversario nos ponga el reloj en marcha una vez que haya hecho su jugada. El estar con una mano presionando continuamente el reloj, o permanentemente por encima del botón, es motivo de sanción por parte del árbitro, hasta el punto de que un jugador persistente puede ser expulsado de un torneo por conducta antideportiva.  
Sin embargo: no se considera que una jugada está terminada hasta que no se aprieta el reloj. El tiempo transcurrido entre la realización de la jugada en el tablero y la presión del reloj es parte de la jugada. Si en el intervalo se «cae la bandera» la partida se considera perdida. Caída de bandera se denomina cuando se termina el tiempo pactado. La expresión se debe a que los primeros relojes de competición tenían una banderita que iba subiendo a medida que se iba terminando en tiempo. Era una bandera externa que se veía desde el público.  
El reloj se coloca donde dice el árbitro. Normalmente se coloca a la derecha de las piezas negras, pero si el negro es zurdo y desea tener el reloj a la izquierda puede decírselo al árbitro que decidirá si cambia de sitio el reloj o no. Si el árbitro tiene una buena visión del reloj en ambos lados del tablero normalmente no hay problema, pero si el árbitro no ve el reloj cuando se coloca a la izquierda el negro lo normal es que no atienda la advertencia.  
En un torneo el reloj se pone en marcha a la hora prevista de comienzo, y en todo caso cuando da la orden el árbitro. En ese momento el jugador de negras pone en marcha el reloj de blancas. Si a la hora de comienzo el jugador de negras no está en la sala es el árbitro quien pone en marcha el reloj.  
Si un jugador detiene los relojes para solicitar la asistencia del árbitro, sin una razón válida para hacerlo será sancionado y si está imposibilitado para presiona el reloj puede ser ayudado por un asistente.  
[Reloj de ajedrez](https://es.wikipedia.org/wiki/Reloj_de_ajedrez)

## Objetivo del proyecto Chessino
  Miguel Barraza, soy ajedrecista ciego y en argentina o latinoamérica nos es muy difícil conseguir un reloj adaptado para jugar al ajedrez, sobre todo por su costo y disponibilidad, son muy difícil de conseguir en esta región. Como programador y estudiante de la universidad de quilmes pensamos que podemos aportar al hardware y al software libre con este proyecto y mostrar que se puede desarrollar uno a muy bajo costo.
Es importante que en el desarrollo nos incluyan a las personas con discapacidad, porque podemos ser buenos UX, desarrolladores, testers, y sobre todo podemos ser parte del cambio.
Un mundo mejor es aquel en el cual todos podemos jugar, ser deportistas y fumentar la cultura libre.
En este proyecto todo el hardware es liberado con foto y detalle de como  lo construimos. Realizado con un Arduino como parte electrónica y una rasberry 3b para manejo de sonido, procesamiento y manejo de audio.
Y el software fue programado en python utilizando  un lenguaje y sonidos libres. Utilizando las librerías pygame, pyfirmata.

## Desarrollado por

* [Miguel Barraza](https://github.com/MiguelBarrazaAr)
* [Juan Contardo](https://github.com/JPContardo)
* [Leandro Otel](https://github.com/LeandroOtel)

## Materiales y precios

* Raspberry 3 Model B (73.000$)

![](/imagenes/raspberry.png)

* Placa Arduino Leonardo (6800$)

![](/imagenes/arduinoLeonardo.jpg)

* Cables Arduino Macho-Macho (600$)

![](/imagenes/cablesArduinoMachoMacho.jpg)

* Botón pulsador de 46mm tipo arcade x2 (900$ c/u)

![](/imagenes/boton46mm.jpg)

* Botón pulsador de 30mm tipo arcade x2 (800$ c/u)

![](/imagenes/boton30mm.png)

* Mini pulsador (400$)

![](/imagenes/miniPulsador.png)

* Display lcd 16x2 con módulo I2c (2.400$)

![](/imagenes/Display%20lcd%2016x2%20con%20m%C3%B3dulo%20I2c.png)

* Mini Protoboard 170 puntos (580$)

![](/imagenes/miniProtoboard.png)

* Cable Datos Usb tipo A a Micro Usb ficha 90º (700$)

![](/imagenes/Cable%20Datos%20Usb%20tipo%20A%20a%20Micro%20Usb%20ficha%2090%C2%BA.png)

* Adaptador puerto de audio 3,5mm Macho(90º)-Hembra (390$)

![](/imagenes/Adaptador%20puerto%20de%20audio%203%2C5mm%20Macho(90%C2%BA)-Hembra.png)

* Buzzer (400$)

![](/imagenes/buzzer.png)

* Carcasa (madera-metal)

![](/imagenes/carcasa.png)

## Herramientas:

* Alicate
* Soldadora de estaño
* Estaño para soldar
* Agujereadora 
* Destornillador
* Tornillos/Remaches

## Pasos para el armado de la carcasa:

Comenzaremos por hacer los cortes en la cara derecha. En el proceso de corte podría notar como la chapa comienza a doblarse, no se preocupe que con unos golpes después podemos enderezarla. Es de vital importancia seguir los cortes propuestos en la siguiente imagen, comenzando por el corte central (línea negra) y luego con las restantes (líneas rojas).

![](/imagenes/armado1.png)

Luego de los cortes veremos que nos queda un sobrante, el cual podemos retirar con la tijera realizando un corte interno.

![](/imagenes/armado2.png)

Continuamos con dos cortes en la parte superior, fundamentales para el pliegue de las piezas en los siguientes pasos. El corte número 2 es un poco más ancho que el corte número 1.

![](/imagenes/armado3.png)

Repetimos los mismos cortes pero en la otra cara.

## Pliegos


Es necesario contar con una madera lo más recta posible. Colocaremos la madera en la línea dibujada en la parte superior de la carcasa, justo donde realizamos el corte número 2 en la sección anterior y doblamos hacia arriba como se especifica en la foto hasta obtener un ángulo de 90 grados.

![](/imagenes/armado4.png)

Luego hacemos nuevamente un pliego pero en sentido inverso.

![](/imagenes/armado5.png)

Ahora solo resta hacer el último pliego, para esto utilizaremos la técnica de la madera nuevamente pero esta vez apoyando en la línea número 2. Ahorramos fuerza de abajo hacia arriba hasta alinear con las paredes triangulares laterales.

![](/imagenes/armado6.png)


Como resultado deberíamos obtener algo como esto

![](/imagenes/armado7.png)

## Remachado o Atornillado
Para este paso tenemos dos opciones, podemos utilizar tornillos t1 para chapa o remaches. Nosotros usaremos remaches para darle maryor solidez estructural. Aquí tenemos que tener mucho ojo en alinear correctamente los márgenes triangulares con las pantallas internas para sujetar ambas partes correctamente. 

![](/imagenes/armado8.png)

Luego de realizar el atornillado pasamos a la otra cara para repetir el paso.

![](/imagenes/armado9.png)

Así debería de quedar el resultado final desde dentro, en ete caso hay remaches pero sería idéntico con los tornillos.

## Limado

Ahora solo resta comenzar a limar y realizar los cortes finales.

![](/imagenes/armado10.png)









