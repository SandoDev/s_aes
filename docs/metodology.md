# Metodología

## Desarrollo del algoritmo

Para el desarrollo del algoritmo de S-AES se usó el lenguaje de programación [python](https://www.python.org/) y algunas librerías extra. Puede encontrar el código fuente del proyecto y probarlo en este enlace de [github](https://github.com/SandoDev/s_aes).

Toda la lógica para la construcción de cada uno de los métodos y la integración de estos se basan en las [referencias](references.md) dispuestas.

El código proporciona los métodos para encriptar y desencriptar texto, además ofrece una interfaz de consola para la ejecución del mismo.

## Implementación del algoritmo

Para implementar el algoritmo puede ejecutar directamente el proyecto por su interfaz de consola:

![Ejecución](images/total_execution.png)

También puede utilizarlo como librería y ejecutar directamente los métodos para encriptar y desencriptar:

![Librería](images/librari_methods.png)

Se sugiere revisar el paquete de `s_aes/test` ya que ahí se muestra el correcto consumo de los métodos.

## Generación de ataques

Para la generación de ataque también exsiten los métodos y la opción desde la interfaz de consola.

En este caso se trabaja desde un [jupyter-notebook](https://jupyter.org/) para la generación de ataque por fuerza bruta.

### Pasos

1. Se parte del hecho que hemos capturado un texto cifrado y el objetivo será encontrar la clave para descifrar el texto.
2. Para ello se usarán multiples claves, la cuales surgen de permutar los caracteres imprimibles de ascii en pares de a 2 valores.
3. Cada llave generará un resultado de desencripción diferente para el mismo texto.
4. A partir de esto se emplearán diferenetes métodos de analisis para limpiar los resultados y llegar así a encontrar la llave.

      1. Métodos de coincidencia y análisis de caracteres: se genera una lista de valores descifrados que contengan solo caracteres imprimibles de ascii, ya que no se espera que el texto inicial hubiera contenido estos valores.
      2. Filtros mediante [regex](https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular): Cada texto descifrado del paso anterior es pasado por expresiones regulares con el fin de filtrar solo los textos que contengan valores numericos o letras del alfabeto, ya que son estos datos los que generalmente se cifran.
      3. Análisis manual: se analiza manualmente cada resultado del paso anterior observando si el texto descifrado representa algo significativo y si se podría afirmar que se encontró la clave
