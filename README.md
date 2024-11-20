# PDIPractica_5
Implementación de filtros suavizantes y realzantes: promedio, mediana, máximo y mínimo, laplaciano y gradiente.

Los filtros suavizantes son utilizados para difuminacion (blurring) y para recuddion de ruido.
La difuminacion se utiliza en tareas de procesamiento, tales como la eliminacion de detalles pequeños de una imagen previo a la extraccion de objetos (grandes), y la union de pequeños espacios vacios en lineas o curvas.
La reduccion de ruido se puede realizar mediante la difuminacion con un filtro lineal y tambien mediante filtrado no-lineal.

# Introduccion
Los filtros suavizantes son utilizados para difuminacion (blurring) y para reduccion de ruido.

La difuminacion se utiliza en tareas de preprocesamiento, tales como la eliminacion de detalles pequelos de una imagen previo a la extraccion de objetos (grandes), y la union de pequeños espacios vacios en lineas o curvas.

La reduccion de ruido se puede realizar mediante la difuminacion con un filtro lineal y mediante filtrado no-lineal.

# Filtros Suavizantes Lineales
La salida o respuesta de un filtro espacial lineal suavizante es simplemente el promedio de los pixeles contenidos en la vecindad de la mascara de filtro. Tambien se conocen como filtros promediantes o filtros pasa-baja.
La idea basica es reemplazar el valor de cada pixel en una imagen por el promedio de los niveles de intensidad en la vecindad definida por la mascara de filtro.

El resultado es una imagen con transiciones en intensiades "agudas" reducidas. Debido a que el ruido aleatorio consiste tipicamente de transiciones agudas en niveles de intensidad, la aplicacion obvia del suavizado es la reduccion de ruido.

Una ventaja de lo anterior, es que produce imagenes con ejes difuminados (borrosos).

Los filtros promediantes se utilizan mayormente para la reduccion de detalle "irrelevante" en una imagen. Generalmente, las regiones de pixeles que son pequeñas con respecto al tamaño de la mascara de filtro son consideradas irrelevantes.

La siguiente figura muestra dos filtros suavizantes de 3 x 3.

![image](https://github.com/user-attachments/assets/bd5a05bb-80c9-441c-9bf7-bda4f136c05d)

El primer filtro produce el promedio estandar de los pixeles bajo la mascara, esto es:
$$(\left (R = {\frac{1}{9}}(\sum_{i=1}^9 Z_i)) \right)$$

Por cuestiones practicas (computacionales), los coeficientes del filtro son todos 1s, para qie al final del proceso el resultado se divide por 9.

De manera general, una mascara m x n tendria una constante normalizadora igual a {\left({\frac{1}{mn}}\right)}.

La segunda mascara produce un promedio pesado (ponderado), es decir, los pixeles son multiplicados por coeficientes diferentes, dando mayor importnacia a algunos pixeles que otros.

Esta estrategia se usa para reducir la difuminacion en el proceso de suavizado.

En la practica, es dificil notar la diferencia en la imagen resultante cuando se utilizan cualquiera de las dos mascaras, debido a su tamaño pequeño (3 x 3).

La implementacion general para filtrar una imagen M x N con un filtro promediante pesado de tamaño m x n es:

![image](https://github.com/user-attachments/assets/b0b66796-29f7-4822-9ade-95705fc33260)

La siguiente figura muestra los efecto de suavizado como una funcion del tamaño de filtro. Aqui, se utilizan filtro promediantes cuadrados de tamaños m = 3, 5, 9, 15 y 35, respectivamente.

![image](https://github.com/user-attachments/assets/40fe7d13-6890-4783-a411-7d46c3a231af)

Una aplicacion importatnte del promediado espacial es difuminar una imagen para el proposito de obtener una representacion gruesa de los objetos de interes.

De esta forma la intensidad de objetos mas pequeños se mezcla con el donfo y objetos mas grandes se convierten en masa amorfa y facil de detectar.

El tamaño de las mascaras establece el tamaño relativo de los objetos que seran mezclados con el fondo. La siguiente figura muestra un ejemplo.

![image](https://github.com/user-attachments/assets/fdbe17ad-7fc3-47eb-a758-c19500db71bb)

La primer imagen a la izquierda es la original, la que esta hasta la derecha es la mascara obtenida.

# Filtros (No-lineales) de Orden Estatico

La respuesta de los filtros de orden estatico se basa en el ordenamiento (ranking) de los pixeles contenidos en el área de la iamgen incluida por el filtro. Despues de reemplaza el valor del pixel central con el valor determinado por el resultado del ranking.

El filtro mas conocido de este tipo es el filtro de **mediana**, el cual reemplaza el valor de un pixel pro la mediana de los valores de intensidad en la vecindad de dicho pixel.

Este filtro es popular debido a que para ciertor topo de ruido aleatorio proporciona excelentes capacidades de reduccion de ruido, con menos difuminacion que los filtros suavizantes lineales de tamaño similar.

Un ejemplo de la efectividad del filtro mediana se observa en la presencia de ruido de "sal y pimienta".

![image](https://github.com/user-attachments/assets/0620baba-7e1b-48da-8278-cedc8eb0ec85)

La funcion principal de los filtros de mediana es forzar a los puntos con niveles de intensidad distintos a parecerse mas a sus vecinos.

Entonces, grupos aislados de pixeles que son luminosos u oscuros con respecto a sus vecinos, y cuya area es menor que m**2/2 son eliminados por un filtro de mediana m x m, i.e son fornzados a la intensidad mediana de sus vecinos.

Los grupos grandes son menos afectados.

Otros filtros de orden estadisticos son el filtro **maximo** y **minimo**. Ej: la respuesta despuesta de un filtro maximo 3 x 3 es:

R = máx{Zk | k = 1, 2, ..., 9}

Este encuentra el punto mas brillante de la vecindad.


