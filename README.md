## Recursos utilizados en el código

### Algoritmos y Estructuras de Datos
- **A\***: Algoritmo de búsqueda utilizado para encontrar el camino más corto desde el punto de inicio hasta el objetivo. Este algoritmo utiliza una heurística para guiar su búsqueda.
- **Nodos**: Clase utilizada para representar cada punto en la matriz durante la búsqueda A\*.
- **Heurística Manhattan**: Método utilizado para estimar la distancia entre dos puntos en una cuadrícula, sumando las diferencias absolutas de sus coordenadas.

### Funciones y Métodos
- **obtener_entrada()**: Función para recibir y validar la entrada del usuario, asegurando que los valores sean mayores que 10.
- **obtener_posicion()**: Función para recibir y validar las coordenadas (fila y columna) ingresadas por el usuario.
- **obtener_obstaculos()**: Función para recibir las posiciones de los obstáculos y asegurar que no se coloquen en lugares ocupados por edificios, el inicio o el objetivo.
- **Nodo**: Clase que representa un nodo en el camino, con atributos para su posición, nodo padre, y costos de movimiento (g, h, f).
- **heuristica()**: Función que calcula la distancia heurística entre el nodo actual y el nodo objetivo.
- **generar_matriz()**: Función que genera la matriz inicial con posiciones predeterminadas para los edificios.
- **a_estrella()**: Implementación del algoritmo A\* para encontrar el camino más corto entre el inicio y el objetivo.
- **visualizar()**: Función para imprimir la matriz, mostrando edificios, obstáculos, el punto de inicio, el objetivo y el camino encontrado.
