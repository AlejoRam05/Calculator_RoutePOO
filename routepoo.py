class Matriz:
    
    def __init__(self, FILAS: int, COLUMNAS: int, STAR, FIN):
        
        self.FILAS = FILAS
        self.COLUMNAS = COLUMNAS
        self.STAR = STAR
        self.FIN = FIN
        self.OBSTACULO = 1
        self.matriz = self.generar_matriz()
    
    @staticmethod
    def obtener_posicion(mensaje, FILAS, COLUMNAS, exclusion=None):
        while True:
            try:
                fila = int(input(f"Ingrese la fila para {mensaje} (0 a {FILAS-1}): "))
                columna = int(input(f"Ingrese la columna para {mensaje} (0 a {COLUMNAS-1}): "))
                if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
                    if exclusion and (fila, columna) == exclusion:
                        raise ValueError("La posición no puede coincidir con la de exclusión.")
                    return (fila, columna)
                else:
                    raise ValueError("La posición debe estar dentro de los límites de la matriz.")
            except ValueError as e:
                print(e)
    
        
    def generar_matriz(self):
        
        matriz = []
        
        for i in range(self.FILAS):
            fila = []
            for j in range(self.COLUMNAS):
                
                if j % 2 == 1 and i % 2 != 1:
                    fila.append(self.OBSTACULO)
                else: 
                    fila.append(0)
            matriz.append(fila)
        return matriz
    
    def incluir_obstaculo(self, menaje):
        while True:
            try:
                pregunta = int(input(menaje))
                if pregunta == 1:
                    cant_obst = int(input("Ingresa la cantidad que quieres agregar: ")) 
                    for _ in range(cant_obst):
                        while True:
                            fila = int(input(f"Ingrese la fila del obstaculo (0 a {self.FILAS - 1}): "))
                            columna = int(input(f"Ingrese la columna del obstaculo (0 a {self.COLUMNAS - 1}): "))   
                            if 0 <= fila < self.FILAS and 0 <= columna < self.COLUMNAS:
                                if self.matriz[fila][columna] == 0:
                                    self.matriz[fila][columna] = self.OBSTACULO
                                    break
                                else:
                                    print("La posición ya está ocupada por un obstáculo.")
                            else: 
                                print("La posición está fuera de los límites.")
                else: 
                    return

            except ValueError as e: 
                print(e)

class ConfiguracionMatriz:
    
    @staticmethod
    def obtener_dimensiones():
        while True:
            try:
                FILAS = int(input("Ingrese el número de filas (mayor que 7): "))
                if FILAS > 7:
                    break
                else:
                    print("El número de filas debe ser mayor que 7.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        while True:
            try:
                COLUMNAS = int(input("Ingrese el número de columnas (mayor que 7): "))
                if COLUMNAS > 7:
                    break
                else:
                    print("El número de columnas debe ser mayor que 7.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        return FILAS, COLUMNAS
    
    @staticmethod
    def obtener_inicio_y_fin(FILAS, COLUMNAS):
        inicio = Matriz.obtener_posicion("La posición de inicio", FILAS, COLUMNAS)
        fin = Matriz.obtener_posicion("La posición de fin", FILAS, COLUMNAS, inicio)
        return inicio, fin        

class VisualizarMatriz:
    
    @staticmethod
    def mostrar_matriz(matriz):
        for fila in matriz:
            print(fila)

class Nodo:
    
    def __init__(self, posicion, parent= None):
        self.posicion = posicion
        self.parent = parent
        self.Q = 0   # Coste de Nodo de inicio hasta este NodoX
        self.H = 0   # Heurística estimada desde el NodoX hasta el objetivo
        self.F = 0   # Coste total (Q + F)
        
    def __eq__(self, other):
        return self.posicion == other.posicion
    
    def heuristica(self, objetivo):
        """Calcula la heurística utilizando la distancia Manhattan."""
        self.H = abs(self.posicion[0] - objetivo[0]) + abs(self.posicion[1] - objetivo[1])
        self.F = self.Q + self.H

class BusquedaAStar:
    
    def __init__(self, matriz, inicio, fin):
        self.matriz = matriz
        self.inicio = Nodo(inicio)
        self.fin = Nodo(fin)
        self.lista_abierta = []
        self.lista_cerrada = []
        
    def a_star(self):
        """Implementación del Algoritmo A*"""
        # Añadimos el Nodo inicial a la lista abierta
        self.lista_abierta.append(self.inicio)
        
        while self.lista_abierta:
            # Toma el Nodo con menor coste
            nodo_actual = min(self.lista_abierta, key=lambda nodo: nodo.F)
            self.lista_abierta.remove(nodo_actual)
            self.lista_cerrada.append(nodo_actual)
            
            if nodo_actual == self.fin: 
                return self.reconstruir_camino(nodo_actual)
            
            # Generar hijos
            hijos = self.generar_hijos(nodo_actual)
            
            for hijo in hijos:
                if hijo in self.lista_cerrada:
                    continue
                
                hijo.Q = nodo_actual.Q + 1
                hijo.heuristica(self.fin.posicion)
                
                if any(nodo for nodo in self.lista_abierta if hijo == nodo and hijo.Q > nodo.Q):
                    continue
                
                self.lista_abierta.append(hijo)
        
        # Retorna nulo si se agotan los Nodos y no hay camino
        return None
    
    def generar_hijos(self, nodo):
        """Genera los hijos para un Nodo dado"""
        
        hijos = []
        movimientos = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for nueva_pos in movimientos:
            nodo_pos = (nodo.posicion[0] + nueva_pos[0], nodo.posicion[1] + nueva_pos[1])
            
            # Controlar si está dentro de los límites
            if (0 <= nodo_pos[0] < len(self.matriz) and
                0 <= nodo_pos[1] < len(self.matriz[0]) and
                self.matriz[nodo_pos[0]][nodo_pos[1]] == 0):
                
                nodo_nuevo = Nodo(nodo_pos, nodo)
                hijos.append(nodo_nuevo)
                
        return hijos
    
    def reconstruir_camino(self, nodo):
        """Reconstruir el camino desde el Fin al Inicio"""
        
        camino = []
        nodo_actual = nodo
        while nodo_actual is not None:
            camino.append(nodo_actual.posicion)
            nodo_actual = nodo_actual.parent
        return camino[::-1]  # Devuelve la lista desde el Último al primero

class Visualizacion:

    def __init__(self, FILAS, COLUMNAS, OBJETIVO, STAR, matriz, camino):
        self.FILAS = FILAS
        self.COLUMNAS = COLUMNAS
        self.OBJETIVO = OBJETIVO
        self.STAR = STAR
        self.matriz = matriz
        self.camino = camino
    
    def visualizar(self):
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if self.matriz[i][j] == 1:
                    print("⏹", end=" ")
                elif (i, j) == self.STAR:
                    print("🚗", end=" ")
                elif (i, j) == self.OBJETIVO:
                    print("🏠", end=" ")
                elif self.camino and (i, j) in self.camino:
                    print("🚩", end=" ")
                else:
                    print(".", end=" ")
            print()


FILAS, COLUMNAS = ConfiguracionMatriz.obtener_dimensiones()
STAR, FIN = ConfiguracionMatriz.obtener_inicio_y_fin(FILAS, COLUMNAS)

matriz_obj = Matriz(FILAS, COLUMNAS, STAR, FIN)
matriz_obj.incluir_obstaculo("¿Quieres agregar obstáculos? (1 para sí, 0 para no): ")

a_star_obj = BusquedaAStar(matriz_obj.matriz, STAR, FIN)
camino = a_star_obj.a_star()

visualizador = Visualizacion(FILAS, COLUMNAS, FIN, STAR, matriz_obj.matriz, camino)
visualizador.visualizar()
