"""
A file containing graph solution to a word play problem

For example to determine whether 'motyka' and 'karma' can
be adjusted in such order that a word starts with the last
character of the previous word
"""

from collections import defaultdict


class Graph:
    """
    Object representation of an oriented graph
    """

    def __init__(self, vertices: dict):
        self.vertices = list(vertices.keys())
        self.degress = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Adds an edge between two verices
        """
        self.graph[u].append(v)

    def path_exists(self):
        """
        Determines if a path exists within the graph
        The method uses Hierholzers algorithm
        """

        # find starting and ending vertex
        start = None
        end = None
        temp = None

        for v in self.vertices:
            degs = self.degress[v]
            if degs[0] == degs[1] + 1:
                if start is None:
                    start = v
                else:
                    return False
            if degs[0] + 1 == degs[1]:
                if end is None:
                    end = v
                else:
                    return False
            elif degs[0] == degs[1]:
                if start is None:
                    temp = v

        if start is not None and end is not None:
            self.add_edge(end, start)
        else:
            start = temp

        # Hierholzer algo
        path = set()
        stack = [start]
        while stack:
            if not self.graph[stack[-1]]:
                path.add(stack[-1])
                stack.pop()
            else:
                stack.append(self.graph[stack[-1]][0])
                self.graph[stack[-2]].pop(0)

        if path.__len__() == self.graph.__len__():
            return True

        return False


def get_data(name):
    """
    Reads the data from a file and transforms it into a more readable format
    """
    _doors: dict = {}
    with open(name, 'r') as file:
        for i in range(int(file.readline())):
            _doors[i] = []
            for _ in range(int(file.readline())):
                word = file.readline().strip()
                _doors[i].append((word[0], word[-1]))
    return _doors


def to_graph(row: list):
    """
    Converts a row of vertices to a graph object
    """
    vertices = {}
    for e_start, e_end in row:
        if e_start in vertices:
            vertices[e_start][0] += 1
        else:
            vertices[e_start] = [1, 0]

        if e_end in vertices:
            vertices[e_end][1] += 1
        else:
            vertices[e_end] = [0, 1]

    graph = Graph(vertices)
    for e_start, e_end in row:
        graph.add_edge(e_start, e_end)

    return graph


def resolve(filename, verbal=False):
    """
    Resolves the given data by a file and then writes the results to a file `vysledky.txt`
    """
    data = get_data(filename)
    with open('vysledky.txt', 'w') as file:
        for row in data.values():
            res = str(len(row)) + " " + str(to_graph(row).path_exists())
            if verbal:
                print(res)
            file.write(res + "\n")


def simple_visual_test():
    """
    A function to provide a quick feedback, only for testing purposes
    """
    resolve('small.txt', True)
    resolve('large.txt', True)
    resolve('test_limit_positive.txt', True)


if __name__ == '__main__':
    simple_visual_test()
