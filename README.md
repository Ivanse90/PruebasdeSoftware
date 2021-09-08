# PruebasdeSoftware
Pruebas de Software

Ejercicio Celdas
1. Este Ejercicio consiste en encontrar el estado de las celdas luego de días transcurridos para esto se debe desarrollar un algoritmo en el cual como parámetros de entrada 
requiere un arreglo de unos y ceros, así como también un numero entero que indicara
el número de días, el arreglo simulara ser celdas led en la cuales cuando se encuentra el número 1 se encuentran prendidas y 0 cuando estas se encuentran apagadas, cada celda
tendrá dos celdas continuas incluso para la celda en la posición 0 y -1 las celdas adyacentes fuera del arreglo siempre serán 0, de tal manera que para el arreglo 
[1, 1, 1, 0, 1, 1, 1, 1] el total de celdas será 0[1, 1, 1, 0, 1, 1, 1, 1]0.
Luego de un día las celdas cambian a 0 si las celdas adyacentes son iguales y cambia a 1 en el caso de que sus celdas adyacentes serán diferentes.

La Función simulate_cells () recibe como parámetros una lista de 1 y 0 por ejemplo [1, 1, 1, 0, 1, 1, 1, 1] la cual indicara el estado en el que se encuentra cada celda 
1 encendido 0 apagado, el segundo parámetro que recibe es el número de días el cual será utilizado para simular el estado de las celdas luego de X días
Esta función retornara un arreglo de 1 y 0 luego de X días transcurridos con el estado de cada celda según las indicaciones anteriormente mostradas
