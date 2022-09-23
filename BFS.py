
#code taken from LINK = https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/ tried this but could not work well
#final resource = https://www.educative.io/answers/how-to-implement-a-breadth-first-search-in-python


graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'H'],
        'D' : ['I', 'J'],
        'E' : ['G1', 'K'],
        'F' : ['L', 'M'],
        'H' : ['N', 'G2'],
        'I' : [],
        'J' : [],
        'K' : [],
        'L' : [],
        'M' : [],
        'N' : [],
        'G1' : [],
        'G2' : []}

visited = []
queue = []


def BFS(visited, graph, node):
        
        
        #learn about children and how that works with AI algos 

        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

BFS(visited, graph, 'A')




