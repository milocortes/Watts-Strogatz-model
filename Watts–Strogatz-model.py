import sys
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np


# Generamos una gráfica vacía
G=nx.Graph()
# Definimos los nodos
N = int(sys.argv[1])
m = int(sys.argv[2])
p = 0.1

class WattsStrogatz:
    """docstring for WattsStrogatz.
    Parámetros:
        - G (networkx empty Graph):
        - N (entero): Cantidad de nodos
        - m (entero): Cantidad de conexiones entre nodos
        - p (float): Probabilidad de desconexión
    """
    def __init__(self, G, N, m, p):
        self.G = G
        self.N = N
        self.m = m
        self.p = p

    def inicializa_graph(self):
        """
        El método  inicializa_graph inicializa la gráfica
        con m conexiones entre los nodos vecinos
        """
        self.G.add_nodes_from([x for x in range(self.N)])
        # Agregamos las conexiones
        for i in range(self.N):
            for j in range(1,(self.m+1)):
                label = (i + j) % (self.N)
                self.G.add_edge(i,label)

    def Watts_Strogatz_model(self):
        """
        El método  Watts_Strogatz_model ejecuta el Modelo
        Watts-Strogatz con una probabilidad de desconexión p
        """
        nodos = set(range(self.N))
        for i in range(self.N):
            for j in range(1,(self.m+1)):
                label = (i + j) % (self.N)
                epsilon = random.uniform(0, 1)
                if epsilon < self.p:
                    candidatos = nodos - {i} - set(self.G[i])
                    j_p = np.random.choice(list(candidatos))
                    G.remove_edge(i,label)
                    G.add_edge(i,j_p)


### Generamos una instancia de la clase
WSG = WattsStrogatz(G,N,m,p,)

### Inicializamos y visualizamos la gráfica
WSG.inicializa_graph()
nx.draw_networkx(WSG.G, pos=nx.circular_layout(WSG.G),node_size=[16]*N,width=[0.4]*N,with_labels=False, node_color="r")
plt.show()

### Modelo Watts Strogatz
WSG.Watts_Strogatz_model()
nx.draw(WSG.G, node_size=[16]*N ,width=[0.4]*N, node_color="r")
plt.show()
