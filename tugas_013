# tugas 13
def bfs(graph, start):
    visited = []
    queue = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited
     

graph = {
    'Amin': ['Mike', 'Nick', 'Wasim'],
    'Wasim': ['Imran', 'Amin'],
    'Imran': ['Wasim', 'Faras'],
    'Faras': ['Imran'],
    'Mike': ['Amin'],
    'Nick': ['Amin']
}

#___________________________________________________________


graph = {
    'Rektor': ['Warek 1', 'Warek 2'],
    'Warek 1': ['Rektor'],
    'Warek 2': ['Kaprodi 1', 'Kaprodi 2', 'Kaprodi 3', 'Rektor'],
    'Kaprodi 1': ['Dosen A', 'Dosen B', 'Dosen C', 'Warek 2'],
    'Kaprodi 2': ['Dosen D', 'Dosen E', 'Warek 2'],
    'Kaprodi 3': ['Dosen F', 'Dosen G', 'Warek 2'],
    'Dosen A': ['Kaprodi 1'],
    'Dosen B': ['Kaprodi 1'],
    'Dosen C': ['Kaprodi 1'],
    'Dosen D': ['Kaprodi 2',],
    'Dosen E': ['Kaprodi 2'],
    'Dosen F': ['Kaprodi 3'],
    'Dosen G': ['Kaprodi 3']
}

bfs(graph, 'Rektor')
     
['Rektor',
 'Warek 1',
 'Warek 2',
 'Kaprodi 1',
 'Kaprodi 2',
 'Kaprodi 3',
 'Dosen A',
 'Dosen B',
 'Dosen C',
 'Dosen D',
 'Dosen E',
 'Dosen F',
 'Dosen G']

graph = {
    '0': ['9', '7', '11'],
    '9': ['10', '8', '0'],
    '7': ['11', '6', '3', '0'],
    '11': ['7', '0'],
    '10': ['1', '9'],
    '8': ['1', '12', '9'],
    '6': ['5', '7'],
    '3': ['2', '4', '7'],
    '1': ['10', '8'],
    '12': ['8', '2'],
    '2': ['3', '12'],
    '4': ['3'],
    '5': ['6']
}

bfs(graph, '0')

#___________________________________________________
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
     

graph = {
    'Amin': ['Mike', 'Nick', 'Wasim'],
    'Wasim': ['Imran', 'Amin'],
    'Imran': ['Wasim', 'Faras'],
    'Faras': ['Imran'],
    'Mike': ['Amin'],
    'Nick': ['Amin']
}

dfs(set(), graph, 'Amin')
#_________________________________________________


graph = {
    'Rektor': ['Warek 1', 'Warek 2'],
    'Warek 1': ['Rektor'],
    'Warek 2': ['Kaprodi 1', 'Kaprodi 2', 'Kaprodi 3', 'Rektor'],
    'Kaprodi 1': ['Dosen A', 'Dosen B', 'Dosen C', 'Warek 2'],
    'Kaprodi 2': ['Dosen D', 'Dosen E', 'Warek 2'],
    'Kaprodi 3': ['Dosen F', 'Dosen G', 'Warek 2'],
    'Dosen A': ['Kaprodi 1'],
    'Dosen B': ['Kaprodi 1'],
    'Dosen C': ['Kaprodi 1'],
    'Dosen D': ['Kaprodi 2',],
    'Dosen E': ['Kaprodi 2'],
    'Dosen F': ['Kaprodi 3'],
    'Dosen G': ['Kaprodi 3']
}

dfs(set(), graph, 'Dosen A')
     
Dosen A
Kaprodi 1
Dosen B
Dosen C
Warek 2
Kaprodi 2
Dosen D
Dosen E
Kaprodi 3
Dosen F
Dosen G
Rektor
Warek 1

graph = {
    '0': ['9', '7', '11'],
    '9': ['10', '8', '0'],
    '7': ['11', '6', '3', '0'],
    '11': ['7', '0'],
    '10': ['1', '9'],
    '8': ['1', '12', '9'],
    '6': ['5', '7'],
    '3': ['2', '4', '7'],
    '1': ['10', '8'],
    '12': ['8', '2'],
    '2': ['3', '12'],
    '4': ['3'],
    '5': ['6']
}

dfs(set(), graph, '0')
