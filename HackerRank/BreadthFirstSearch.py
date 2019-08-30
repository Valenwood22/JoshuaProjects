class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1

    def _dfs(self, vertex):
        global time
        vertex.color = 'red'
        vertex.discovery = time
        time +=1
        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
            vertex.color = 'blue'
            vertex.finish = time
            time +=1

    def dfs(self,vertex):
        global time
        time = 1
        self._dfs(vertex)


'''

            A --- B     C
            |     |     |
            |     |     |
      D --- E     F --- G
       \   /     / \   /
         H --- I     J


'''
if __name__=="__main__":
    myGraph = Graph()
    a = Vertex('A')
    myGraph.add_vertex(a)
    myGraph.add_vertex(Vertex('B'))
    for i in range(ord('A'), ord('K')):
        myGraph.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
    for edge in edges:
        myGraph.add_edge(edge[:1], edge[1:])

    myGraph.dfs(a)
    myGraph.print_graph()