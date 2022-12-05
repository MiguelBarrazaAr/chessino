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
Atención: Los precios relacionados con mercado libre no poseen el incremento extra del envió. Para la fecha un envió normal dentro de la provincia está en 1100 pesos.

* Raspberry 3 Model B (73.000$) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-754174478-kit-raspberry-pi-3b-uk-completo-con-microsd-32gb-emakers-_JM#position=6&search_layout=grid&type=item&tracking_id=60e2a8c4-11c7-4d54-a0d0-dab02fdbf693)

![](/imagenes/raspberry.png)

* Placa Arduino Leonardo (5780$) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-774242769-arduino-leonardo-atmega32u4-delta-iot-_JM#position=6&search_layout=grid&type=item&tracking_id=a7d48bce-7f11-4075-a449-d69ab407d742)

![](/imagenes/arduinoLeonardo.jpg)

* Cables Arduino Macho-Macho (649$) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-621254141-pack-40-cables-macho-macho-10cm-dupont-arduino-y-protoboard-_JM#position=1&search_layout=stack&type=item&tracking_id=adf8ff96-581f-4715-8967-c1b258d69f1c)

![](/imagenes/cablesArduinoMachoMacho.jpg)

* Botón pulsador de 46mm tipo arcade x2 (929$ c/u) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-719205591-boton-pulsador-arcade-generico-46mm-retroiluminado-_JM#position=6&search_layout=stack&type=item&tracking_id=b4c73e00-c093-484e-84f5-4a5e792f83db)

![](/imagenes/boton46mm.jpg)

* Botón pulsador de 30mm tipo arcade x2 (458$ c/u) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-921892605-boton-pulsador-arcade-30mm-push-varios-colores-_JM?searchVariation=85588773987#searchVariation=85588773987&position=14&search_layout=stack&type=item&tracking_id=9ea8dcd5-a2ca-4bd8-8443-76cbed23bbef)

![](/imagenes/boton30mm.png)

* Mini pulsador (250$) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-831826308-mini-pulsador-nc-na-metal-1a-250v-rojo-negro-_JM?searchVariation=48395399536#searchVariation=48395399536&position=1&search_layout=stack&type=item&tracking_id=2a1defd4-b235-4434-ba29-d0eacce22c4b)

![](/imagenes/miniPulsador.png)

* Display lcd 16x2 con módulo I2c (2089$) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-767233824-display-lcd-1602-16x2-verde-modulo-i2c-arduino-25off-nut-_JM#position=1&search_layout=grid&type=item&tracking_id=62a16191-e0b3-4616-8687-91d1f1889f65)

![](/imagenes/Display%20lcd%2016x2%20con%20m%C3%B3dulo%20I2c.png)


* Cable Datos Usb tipo A a Micro Usb (240$) (Mercado Libre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-922248891-cable-corto-de-carga-25-cms-ideal-p-parlante-celular-tablet-_JM?searchVariation=85747430067#searchVariation=85747430067&position=7&search_layout=stack&type=item&tracking_id=00c94a89-5cef-4585-ae22-902d35b70e45)

![](/imagenes/Cable%20Datos%20Usb%20tipo%20A%20a%20Micro%20Usb%20ficha%2090%C2%BA.png)

* Adaptador puerto de audio 3,5mm Macho(90º)-Hembra (390$) (Casa de musica )

![](/imagenes/Adaptador%20puerto%20de%20audio%203%2C5mm%20Macho(90%C2%BA)-Hembra.png)


* Fuente de PC Rota (200$) (MercadoLibre) - [Publicacion](https://articulo.mercadolibre.com.ar/MLA-930270942-fuentes-quemadas-de-pc-varias-marcas-_JM?searchVariation=91678007991#searchVariation=91678007991&position=1&search_layout=grid&type=item&tracking_id=2601323a-46c7-441e-b057-a60362b50868)


![](/imagenes/carcasa.png)

* 4 Tornillos T1 para chapa (25$) + 2 Tornillos 3,5 x 9 (10$) o Remaches 4 (10$) + 2 Tornillos 3,5 x 9 (10$) (Ferreteria 11 - Berazategui)

* Papel Contact Negro 1 metro (500$) (Libreria Casa Juni - Berazategui)

* Sierra Copa 40 Mm Bimetal Venturo Giro Triplex Copa 40 mm (Opcional) (2030$) (Mercado Libre) - [Publiacion](https://articulo.mercadolibre.com.ar/MLA-917403294-sierra-copa-40-mm-bimetal-venturo-giro-triplex-acero-madera-_JM?matt_tool=62476992&matt_word=&matt_source=google&matt_campaign_id=14508409193&matt_ad_group_id=124055975422&matt_match_type=&matt_network=g&matt_device=c&matt_creative=543394189904&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=147800068&matt_product_id=MLA917403294&matt_product_partition_id=1408932717052&matt_target_id=aud-415044759576:pla-1408932717052&gclid=Cj0KCQiAvqGcBhCJARIsAFQ5ke5LLl-4yMZ78_XARnjRSIj3CN5XKfWd5Q4mWvoJBCY80hdG5ZomFWAaAmF0EALw_wcB)
* Sierra Copa 30 Mm Bimetal Venturo Giro Triplex (Opcional) (1940$) (Mercado Libre) - [Publiacion](https://articulo.mercadolibre.com.ar/MLA-688006288-copa-bimetalica-acero-madera-g-triplex-30mm-gtr-30-venturo-_JM?matt_tool=62476992&matt_word=&matt_source=google&matt_campaign_id=14508409193&matt_ad_group_id=124055975422&matt_match_type=&matt_network=g&matt_device=c&matt_creative=543394189904&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=134679115&matt_product_id=MLA688006288&matt_product_partition_id=1408932717052&matt_target_id=aud-415044759576:pla-1408932717052&gclid=Cj0KCQiAvqGcBhCJARIsAFQ5ke6f4mdGOynL3D1981PNQeP38s5XmcAjpK_Uy-dMAQg1mjq73-0j1tIaAtBwEALw_wcB)

## Herramientas:

* Alicate
* Soldadora de estaño + estaño
* Agujereadora 
* Destornillador
* Tijera Corta Hoja Chapa
* Remachadora

## Esquema de conexión:

![](/imagenes/EsquemaChessino.jpg)

## Pasos para el armado de la carcasa:

Comenzaremos por hacer los cortes en la cara derecha. En el proceso de corte podría notar como la chapa comienza a doblarse, no se preocupe que con unos golpes después podemos enderezarla. Es de vital importancia seguir los cortes propuestos en la siguiente imagen, comenzando por el corte central (línea negra) y luego con las restantes (líneas rojas).

![](/imagenes/armado1.png)

Luego de los cortes veremos que nos queda un sobrante, el cual podemos retirar con la tijera realizando un corte interno.

![](/imagenes/armado2.png)

Continuamos con dos cortes en la parte superior, fundamentales para el pliegue de las piezas en los siguientes pasos. El corte número 2 es un poco más ancho que el corte número 1.

![](/imagenes/armado3.png)

Repetimos los mismos cortes pero en la otra cara.

## Pliegos 1.0


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

## Cortes + Limado  
Cuando ya se cuenta con la carcaza atornillada o arremachada, podemos comenzar a realizar los cortes finales para esta parte. 
A continuación se adjunta una imagen con los cortes a realizar y donde limar para evitar rebabas.

![](/imagenes/armado10.png)

## Pliegos 2.0

Ahora trabajaremos sobre la base, tomaremos una medida interna desde la pared trasera a unos 11 cm y trazamos una línea horizontal de pliego.
Luego realizaremos el pliegue tal cual se muestra en imagen, es decir, hacia arriba y hacia el interior de la base.

![](/imagenes/armado12.png)

Luego realizaremos un corte del sobrante superior y lo dejaremos como la siguiente imagen

![](/imagenes/armado13.png)

De esta forma finalizamos el proceso de cortes y pliegues


## Agujeros para botones
Para realizar los agujeros para los botones podemos usar tanto una agujeradora con mecha de copa o usar una técnica más económica. 
La técnica consiste en realizar perforaciones simultáneas muy cercanas en el contorno del círculo dibujado. Cuando ya se realizaron la mayor cantidad de perforaciones
mediante una alicate y una lima podemos dejar un perfecto círculo.

![](/imagenes/armado14.png)

Distribución de los agujeros para los botones
Dejaremos una imagen que muestra los agujeros a realizar para colocar los botones y el display lcd. También deberá realizar un agujero en el lateral derecho para colocar un pulsador (botón menú)

![](/imagenes/armado11.png)

## Resultado Final Exterior

![](/imagenes/Final1.png)
![](/imagenes/Final2.png)


## Resultado Final Interior
![](/imagenes/Interior.png)