class Grafo:
    def __init__(self):
        self.vertices = []
        self.aristas = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            print("Vertice agregado:", vertice)
        else:
            print("El vertice ya existe:", vertice)

    def agregar_arista(self, nombre, origen, destino):
        if nombre in self.aristas:
            print("Ya existe una arista llamada", nombre)
            return
        if origen not in self.vertices:
            print("No existe el vertice:", origen)
            return
        if destino not in self.vertices:
            print("No existe el vertice:", destino)
            return
        self.aristas[nombre] = (origen, destino)
        print("Arista agregada:", nombre, "=", origen, "--", destino)

    def mostrar_grafo(self):
        print("\n--- GRAFO ---")
        print("Vertices:")
        for vertice in self.vertices:
            print("-", vertice)
        print("\nAristas:")
        for nombre, extremos in self.aristas.items():
            origen, destino = extremos
            print(nombre, ":", origen, "--", destino)

    def es_bucle(self, nombre_arista):
        if nombre_arista not in self.aristas:
            return False
        origen, destino = self.aristas[nombre_arista]
        return origen == destino

    def son_paralelas(self, arista1, arista2):
        if arista1 not in self.aristas or arista2 not in self.aristas:
            return False
        origen1, destino1 = self.aristas[arista1]
        origen2, destino2 = self.aristas[arista2]
        mismos_extremos = (origen1 == origen2 and destino1 == destino2)
        extremos_invertidos = (origen1 == destino2 and destino1 == origen2)
        return mismos_extremos or extremos_invertidos

    def obtener_aristas_paralelas(self):
        paralelas = []
        nombres = list(self.aristas.keys())
        for i in range(len(nombres)):
            for j in range(i + 1, len(nombres)):
                arista1 = nombres[i]
                arista2 = nombres[j]
                if self.son_paralelas(arista1, arista2):
                    paralelas.append((arista1, arista2))
        return paralelas

    def grado(self, vertice):
        if vertice not in self.vertices:
            return None
        contador = 0
        for origen, destino in self.aristas.values():
            if origen == vertice and destino == vertice:
                contador += 2
            elif origen == vertice or destino == vertice:
                contador += 1
        return contador

    def es_aislado(self, vertice):
        grado_vertice = self.grado(vertice)
        if grado_vertice is None:
            return False
        return grado_vertice == 0

    def obtener_vertices_aislados(self):
        aislados = []
        for vertice in self.vertices:
            if self.es_aislado(vertice):
                aislados.append(vertice)
        return aislados

    def grado_total(self):
        total = 0
        for vertice in self.vertices:
            total += self.grado(vertice)
        return total

    def mostrar_grados(self):
        print("\n--- GRADOS DE LOS VERTICES ---")
        for vertice in self.vertices:
            print(vertice, ":", self.grado(vertice))
        print("Grado total:", self.grado_total())

    def es_simple(self):
        for nombre in self.aristas:
            if self.es_bucle(nombre):
                return False
        if len(self.obtener_aristas_paralelas()) > 0:
            return False
        return True

    def matriz_adyacencia(self):
        cantidad = len(self.vertices)
        matriz = [[0] * cantidad for _ in range(cantidad)]
        for origen, destino in self.aristas.values():
            i = self.vertices.index(origen)
            j = self.vertices.index(destino)
            if i == j:
                matriz[i][j] += 2
            else:
                matriz[i][j] += 1
                matriz[j][i] += 1
        return matriz

    def mostrar_matriz_adyacencia(self):
        matriz = self.matriz_adyacencia()
        print("\n--- MATRIZ DE ADYACENCIA ---")
        print(" " * 14, end="")
        for vertice in self.vertices:
            print(f"{vertice[:8]:>10}", end="")
        print()
        for i in range(len(self.vertices)):
            print(f"{self.vertices[i][:12]:>12}", end="  ")
            for valor in matriz[i]:
                print(f"{valor:>10}", end="")
            print()

    def matriz_incidencia(self):
        cantidad_vertices = len(self.vertices)
        cantidad_aristas = len(self.aristas)
        matriz = [[0] * cantidad_aristas for _ in range(cantidad_vertices)]
        nombres_aristas = list(self.aristas.keys())
        for j in range(cantidad_aristas):
            nombre = nombres_aristas[j]
            origen, destino = self.aristas[nombre]
            i_origen = self.vertices.index(origen)
            i_destino = self.vertices.index(destino)
            if i_origen == i_destino:
                matriz[i_origen][j] = 2
            else:
                matriz[i_origen][j] = 1
                matriz[i_destino][j] = 1
        return matriz

    def mostrar_matriz_incidencia(self):
        matriz = self.matriz_incidencia()
        nombres_aristas = list(self.aristas.keys())
        print("\n--- MATRIZ DE INCIDENCIA ---")
        print(" " * 14, end="")
        for nombre in nombres_aristas:
            print(f"{nombre:>6}", end="")
        print()
        for i in range(len(self.vertices)):
            print(f"{self.vertices[i][:12]:>12}", end="  ")
            for valor in matriz[i]:
                print(f"{valor:>6}", end="")
            print()

    def obtener_vecinos(self, vertice):
        if vertice not in self.vertices:
            return []
        vecinos = []
        for origen, destino in self.aristas.values():
            if origen == vertice and destino not in vecinos:
                vecinos.append(destino)
            if destino == vertice and origen not in vecinos:
                vecinos.append(origen)
        return vecinos

    def lista_adyacencia(self):
        lista = {vertice: [] for vertice in self.vertices}
        for origen, destino in self.aristas.values():
            lista[origen].append(destino)
            if origen != destino:
                lista[destino].append(origen)
        return lista

    def mostrar_lista_adyacencia(self):
        lista = self.lista_adyacencia()
        print("\n--- LISTA DE ADYACENCIA ---")
        for vertice, vecinos in lista.items():
            print(vertice, "->", vecinos)

    def resumen(self):
        print("\n========== RESUMEN DEL GRAFO ==========")
        print("Cantidad de vertices:", len(self.vertices))
        print("Cantidad de aristas:", len(self.aristas))
        print("Grado total:", self.grado_total())
        print("Es simple:", self.es_simple())
        print("Vertices aislados:", self.obtener_vertices_aislados())
        print("Aristas paralelas:", self.obtener_aristas_paralelas())
        bucles = [nombre for nombre in self.aristas if self.es_bucle(nombre)]
        print("Bucles:", bucles)


# Ejecución de prueba
if __name__ == "__main__":
    grafo_simple = Grafo()
    grafo_simple.agregar_vertice("Bodega")
    grafo_simple.agregar_vertice("Norte")
    grafo_simple.agregar_vertice("Centro")
    grafo_simple.agregar_vertice("Sur")
    grafo_simple.agregar_vertice("Aeropuerto")

    grafo_simple.agregar_arista("e1", "Bodega", "Norte")
    grafo_simple.agregar_arista("e2", "Bodega", "Centro")
    grafo_simple.agregar_arista("e3", "Norte", "Centro")
    grafo_simple.agregar_arista("e4", "Centro", "Sur")

    grafo_simple.mostrar_grafo()
    grafo_simple.mostrar_grados()
    grafo_simple.mostrar_lista_adyacencia()
    grafo_simple.mostrar_matriz_adyacencia()
    grafo_simple.mostrar_matriz_incidencia()
    grafo_simple.resumen()

    # ---------------------------------------------------------
# PASO 27: ACTIVIDAD GUIADA - MODIFICACIONES AL GRAFO
# ---------------------------------------------------------

print("\n" + "=" * 50)
print("MODIFICACIÓN 1: Conectar el vértice aislado (e5: Sur -- Aeropuerto)")
print("=" * 50)
grafo_simple.agregar_arista("e5", "Sur", "Aeropuerto")
grafo_simple.mostrar_grados()
grafo_simple.mostrar_matriz_adyacencia()
grafo_simple.mostrar_matriz_incidencia()
grafo_simple.resumen()

print("\n" + "=" * 50)
print("MODIFICACIÓN 2: Agregar arista paralela (e6: Norte -- Bodega)")
print("=" * 50)
grafo_simple.agregar_arista("e6", "Norte", "Bodega")
grafo_simple.mostrar_grados()
grafo_simple.mostrar_matriz_adyacencia()
grafo_simple.mostrar_matriz_incidencia()
grafo_simple.resumen()

print("\n" + "=" * 50)
print("MODIFICACIÓN 3: Agregar un bucle (e7: Centro -- Centro)")
print("=" * 50)
grafo_simple.agregar_arista("e7", "Centro", "Centro")
grafo_simple.mostrar_grados()
grafo_simple.mostrar_matriz_adyacencia()
grafo_simple.mostrar_matriz_incidencia()
grafo_simple.resumen()