# ALGORITMOS_2_Marta_Navarro

En este repositorio se encuentran cuatro archivos con ejercicios de POO y de algoritmia. Más adelante en el READMe hay una breve explicación teorica de la imlementación de Bubble Sort y sus aplicaciones.

**Ejercicio 1** Archivios: Genre.py y Song.py
Consiste en una clase Song con sus atributos propios y uno de ellos es una lista que contiene elementos de tipo GENRE (que es de clase enum). En esta clase también se encuentran sus métodos propios como add_genre que añade gáneros a los tipos de generos de la canción y el método _ _ eq _ _ que compara si dos canciones son iguales.


**Ejercicio 2** Archivos: Factorial.py

Entrada: 
- n: un número entero no negativo para calcular su factorial.

Precondición:
- n debe ser un número entero no negativo.
Hipótesis: n! = n(n-1)!
Función factorial(n: entero) -> entero:
    poscondición:
    - Se asume que n es un número entero no negativo.

    Si n es igual a 0:
        Salida:
        - Retorna 1   # Caso base: factorial de 0 es 1
    Sino:
        Salida:
        - Retorna n * factorial(n - 1)   # Paso recursivo: calcula n * factorial(n-1) _> número entero
        - La función devuelve el factorial del número n.




**Bubble sort**
Se trata de una herramiento o una implementación que consiste en un algoritmo de ordenación. Con este métdo se recorre, o itera, una lista proporcionada en un principio desordenada, con el objetivo de ordenarla.
Elagorimo consiste enrecorrer toda la lista e ir  comparando dos elementos de la lista que se encuentran adyacentemente (en una posicion i e i+1) y ordenar esos dos elementos. Cuando haya finalizado la primera iteración evalúa si debe volver a realizar este proceso. En este caso vuelve a recorrer la lista y ordenar los pares de elementos. Este proceso finalizza cuando la lista esté perfectamente ordenada.


Bubble Sort es útil principalmente para listas pequeñas o casi ordenadas debido a que tiene que realizar varias repeticiones y deja de ser eficiente.

Supongamos que tenemos la lista de números: [34, 7, 23, 32, 5].
primera iteración: Se comparan los elementos 34 y 7. Como 34 es mayor que 7, se intercambian: [7, 34, 23, 32, 5]. Se comparan los elementos 34 y 23. No se requiere intercambio. Se comparan los elementos 34 y 32. Se intercambian: [7, 23, 34, 32, 5]. Se comparan los elementos 34 y 5. Se intercambian: [7, 23, 5, 32, 34]
segunda iteración: Se comparan los elementos 7 y 23, no requiere intercambio. Se comparan los elementos 23 y 5 y se intercambian. Las siguientes comparan los siguientes elementos y no requieren ordenación. resultado: [7, 5, 23, 32, 34]
tercera iteración: se comparan los elementos 7 y 5 y se intercambian. resultado: [5, 7, 23, 32, 34]

**Ejercicio 3** 
Este ejercicio consiste en la utilización y ejemplos de la función partial de functools.
