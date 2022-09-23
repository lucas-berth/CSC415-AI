from collections import defaultdict


#code taken from LINK = https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/

graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'H'],
        'D' : ['I', 'J'],
        'E' : ['G1', 'K'],
        'F' : ['L', 'M'],
        'H' : ['N', 'G2'],
        'I' : ['D'],
        'J' : ['D'],
        'K' : ['E'],
        'L' : ['F'],
        'M' : ['F'],
        'N' : ['H'],
        'G1' : ['E'],
        'G2' : ['H']}

queue = []
visited = []

def BFS(graph, visited, node):
        
        queue = []
        visited = []
        #learn about children and how that works with AI algos 

        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            #int(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



    
BFS(visited, graph, 'A')




