# PDIPractica_5
Implementación de filtros suavizantes y realzantes: promedio, mediana, máximo y mínimo, laplaciano y gradiente.

Los filtros suavizantes son utilizados para difuminacion (blurring) y para recuddion de ruido.
La difuminacion se utiliza en tareas de procesamiento, tales como la eliminacion de detalles pequeños de una imagen previo a la extraccion de objetos (grandes), y la union de pequeños espacios vacios en lineas o curvas.
La reduccion de ruido se puede realizar mediante la difuminacion con un filtro lineal y tambien mediante filtrado no-lineal.

# Filtros Suavizantes Lineales
La salida o respuesta de un filtro espacial lineal suavizante es simplemente el promedio de los pixeles contenidos en la vecindad de la mascara de filtro. Tambien se conocen como filtros promediantes o filtros pasa-baja.
La idea basica es reemplazar el valor de cada pixel en una imagen por el promedio de los niveles de intensidad en la vecindad definida por la mascara de filtro.

El resultado es una imagen con transiciones en intensiades "agudas" reducidas. Debido a que el ruido aleatorio consiste tipicamente de transiciones agudas en niveles de intensidad, la aplicacion obvia del suavizado es la reduccion de ruido.

Una ventaja de lo anterior, es que produce imagenes con ejes difuminados (borrosos).

Los filtros promediantes se utilizan mayormente para la reduccion de detalle "irrelevante" en una imagen. Generalmente, las regiones de pixeles que son pequeñas con respecto al tamaño de la mascara de filtro son consideradas irrelevantes.

La siguiente figura muestra dos filtros suavizantes de 3 x 3.

![image](https://github.com/user-attachments/assets/bd5a05bb-80c9-441c-9bf7-bda4f136c05d)

El primer filtro produce el promedio estandar de los pixeles bajo la mascara, esto es:
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$


