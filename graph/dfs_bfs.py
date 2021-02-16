import random

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = 0
        self.neighbours = []

    def addNeighbour(self, other):
        if other not in self.neighbours:
            self.neighbours.append(other)
        # else:
        #     print('Wezly', self.name, ' ', other.name, ' są już połączone')

    def wypiszSosiadow(self):
        print("Wszyscy sąsiedzi węzała: ",self.name," -> ", end=' ')
        for somsiad in self.neighbours:
            print(somsiad.name, end=', ')
        print('')


class Graph (object):
    def __init__(self, directed=0):
        self.directed = directed
        self.wezly = []

    def dodajWezel(self, wezel):
        self.wezly.append(wezel)

    def v(self):
        return len(self.wezly)

    def addNode(self, nodeName):
        newNode = Node(nodeName)
        self.wezly.append(newNode)

    def wypiszWezly(self):
        print("Wszystkie wezly grafu: ", end=' ')
        for wezel in self.wezly:
            print(wezel.name, end=', ')
        print('')

    def dodajKrawedz(self, wezel1, wezel2):

        if type(wezel1) != Node:
            wezel1 = self.znajdzWezel(wezel1)

        if type(wezel1) != Node:
            wezel2 = self.znajdzWezel(wezel2)

        if wezel1 in self.wezly and wezel2 in self.wezly:
            if self.directed == 0:
                wezel1.addNeighbour(wezel2)
                wezel2.addNeighbour(wezel1)
            else:
                wezel1.addNeighbour(wezel2)
        # else:
        #     print("Oba wezły musza być w grafie aby je połączyć")

    def znajdzWezel(self, nodeName):
        for wezel in self.wezly:
            if wezel.name == nodeName:
                return wezel

    def addEdge(self, nameNode1, nameNode2):

        wezel1 = self.znajdzWezel(nameNode1)
        wezel2 = self.znajdzWezel(nameNode2)

        if wezel1 in self.wezly and wezel2 in self.wezly:
            if self.directed == 0:
                wezel1.addNeighbour(wezel2)
                wezel2.addNeighbour(wezel1)
            else:
                wezel1.addNeighbour(wezel2)
        # else:
        #     print("Oba wezły musza być w grafie aby je połączyć")

    def dfs(self, wezel1, visited, first=0):

        if first == 0:
            print("\nDFS: ", end=' ')

        if wezel1 not in visited:
            print(wezel1.name, end=' ')
            visited.add(wezel1)
            for somsiad in wezel1.neighbours:
                self.dfs(somsiad, visited, 1)

    def bfs(self, node, visited):

        print("\nBFS: ", end=' ')
        queue = []

        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s.name, end=" ")

            for somsiad in s.neighbours:
                if somsiad not in visited:
                    visited.append(somsiad)
                    queue.append(somsiad)


    def addNodes(self, n):
        for x in range(n):
            self.addNode(x)


    def randomEdges(self, n):

        for x in range(n):
            node1 = random.randint(0, self.v())
            node2 = random.randint(0, self.v())
            if node1 == node2:
                x -= 1
            else:
                self.addEdge(node1, node2)
                # print('dodano krawedz')

    def printAllNeighbour(self):
        for node in self.wezly:
            node.wypiszSosiadow()


def grafNieskierowany():
    print("\n\nGRAF NIESKIEROWANY")

    undirected = Graph(0)

    undirected.addNodes(20)
    undirected.randomEdges(30)

    undirected.wypiszWezly()
    undirected.printAllNeighbour()

    undirected.dfs(undirected.znajdzWezel(4), visited=set())
    undirected.bfs(undirected.znajdzWezel(4),  visited=[])


def grafSkierowany():
    print("\n\nGRAF SKIEROWANY")

    directed = Graph(1)

    directed.addNodes(20)
    directed.randomEdges(30)

    directed.wypiszWezly()
    directed.printAllNeighbour()

    directed.dfs(directed.znajdzWezel(3),  visited=set())
    directed.bfs(directed.znajdzWezel(3),  visited=[])


if __name__ == '__main__':
    grafNieskierowany()
    grafSkierowany()
