from collections import deque

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            '8th and 41st': 1,
            '9th and 41st': 1,
            'Dryer and 41st': 1,
            '10th and 41st': 1,
            '11th and 41st': 1,
            '12th and 41st': 1,
            '12th and 42nd': 1,
            '11th and 42nd': 1,
            '10th and 42nd': 1,
            '9th and 42nd': 1,
            '8th and 42nd': 1,
            '8th and 43rd': 2,
            '9th and 43rd': 2,
            '10th and 43rd': 2,
            '11th and 43rd': 2,
            '12th and 43rd': 2,
            '12th and 44th': 2,
            '11th and 44th': 2,
            '10th and 44th': 2,
            '9th and 44th': 2,
            '8th and 44th': 2,
            '8th and 45th': 2,
            '9th and 45th': 2,
            '10th and 45th': 2,
            '11th and 45th': 2,
            '12th and 45th': 2,
            '12th and 46th': 2,
            '11th and 46th': 2,
            '10th and 46th': 2,
            '9th and 46th': 2,
            '8th and 46th': 2,
            '8th and 47th': 2,
            '9th and 47th': 2,
            '10th and 47th': 2,
            '11th and 47th': 2,
            '12th and 47th': 2,
            '11th and 48th': 1,
            '10th and 48th': 1,
            '9th and 48th': 1,
            '8th and 48th': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None



#this is where we will plug in the map
#find a way to properly store the streets and corners (nodes)
adjacency_list = {
    '8th and 41st': [('8th and 42nd', 1), ('9th and 41st', 3.5)],
    '9th and 41st': [('9th and 42nd', 1), ('Dryer and 41st', 3.5)],
    'Dryer and 41st': [('Dryer and 42nd', 1), ('10th and 41st', 3.5)],
    '10th and 41st': [('10th and 42nd', 1), ('11th and 41st', 3.5)],
    '11th and 41st': [('11th and 42nd', 1), ('12th and 41st', 3.5)],
    '12th and 41st': [('12th and 42nd', 1)],
    '12th and 42nd': [('12th and 43rd', 1), ('11th and 42nd', 3.5)],
    '11th and 42nd': [('11th and 43rd', 1), ('10th and 42nd', 3.5)],
    '10th and 42nd': [('10th and 43rd', 1), ('9th and 42nd', 3.5)],
    '9th and 42nd': [('9th and 43rd', 1), ('8th and 42nd', 3.5)],
    '8th and 42nd': [('8th and 43rd', 1)],
    '8th and 43rd': [('8th and 44th', 1), ('9th and 43rd', 3.5)],
    '9th and 43rd': [('9th and 44th', 1), ('10th and 43rd', 3.5)],
    '10th and 43rd': [('10th and 44th', 1), ('11th and 43rd', 3.5)],
    '11th and 43rd': [('11th and 44th', 1), ('12th and 43rd', 3.5)],
    '12th and 43rd': [('12th and 44th', 1)],
    '12th and 44th': [('12th and 45th', 1), ('11th and 44th', 3.5)],
    '11th and 44th': [('11th and 45th', 1), ('10th and 44th', 3.5)],
    '10th and 44th': [('10th and 45th', 1), ('9th and 44th', 3.5)],
    '9th and 44th': [('9th and 45th', 1), ('8th and 44th', 3.5)],
    '8th and 44th': [('8th and 45th', 1)],
    '8th and 45th': [('8th and 46th', 1), ('9th and 45th', 3.5)],
    '9th and 45th': [('9th and 46th', 1), ('10th and 45th', 3.5)],
    '10th and 45th': [('10th and 46th', 1), ('11th and 45th', 3.5)],
    '11th and 45th': [('11th and 46th', 1), ('12th and 45th', 3.5)],
    '12th and 45th': [('12th and 46th', 1)],
    '12th and 46th': [('12th and 47th', 1), ('11th and 46th', 3.5)],
    '11th and 46th': [('11th and 47th', 1), ('10th and 46th', 3.5)],
    '10th and 46th': [('10th and 47th', 1), ('9th and 46th', 3.5)],
    '9th and 46th': [('9th and 47th', 1), ('8th and 46th', 3.5)],
    '8th and 46th': [('8th and 47th', 1)],
    '8th and 47th': [('8th and 48th', 1), ('9th and 47th', 3.5)],
    '9th and 47th': [('9th and 48th', 1), ('10th and 47th', 3.5)],
    '10th and 47th': [('10th and 48th', 1), ('11th and 47th', 3.5)],
    '11th and 47th': [('11th and 48th', 1), ('11th and 47th', 3.5)],
    '12th and 47th': [('11th and 48th', 3.5)],
    '11th and 48th': [('10th and 48th', 3.5)],
    '10th and 48th': [('9th and 48th', 3.5)],
    '9th and 48th': [('8th and 48th', 3.5)]
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('8th and 42nd', '12th and 46th')