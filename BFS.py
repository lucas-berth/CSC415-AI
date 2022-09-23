
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


def BFS(visited, graph, node, goal):
        
        
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
        #tried to add logic to check the current node with goal
        #if visited[s] == goal:
        #    print("success")
       #     return

BFS(visited, graph, 'A', 'F')


#Also did not get this one to work which was disappointing 
#I think the logic is almost there, just need to add in logic to compare to whatever node is being evaluated.

