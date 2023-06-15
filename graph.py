airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ')

routes = [
    ['PHX', 'LAX'],
    ['PHX', 'JFK'],
    ['JFK', 'OKC'],
    ['JFK', 'HEL'],
    ['JFK', 'LOS'],
    ['MEX', 'LAX'],
    ['MEX', 'BKK'],
    ['MEX', 'LIM'],
    ['MEX', 'EZE'],
    ['LIM', 'BKK'],
]

graph = {} 

# Add node
def addNode(airport):
    graph[airport] = []

# Add edge, undirected
def addEdge(origin, destination):
    graph.get(origin).append(destination)
    graph.get(destination).append(origin)

for i in airports:
    addNode(i)

for i in routes:
    addEdge(*i)


for line in graph:
    print(line, "--->",graph[line])

# znajdź czy jest połączenie z PHX -> BKK
# porównaj Breadth-first Search (BFS) (przeszukiwanie wszerz) 
# i Depth-first Search (DFS) (przeszukiwanie w głąb) 

from collections import deque

queue = deque()
queue += graph['PHX']
searched = []

while queue:
    print(queue)
    port = queue.popleft()
    if not port in searched:
        if port is 'BKK':
            queue = False
            print("znalazłem", port)
        else:
            queue += graph[port]
            queue.append(port)