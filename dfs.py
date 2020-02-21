# directed graph without loop
directed_graph = {
        'A':{'B'}, 
        'B':{'C','D'}, 
        'C':{'E', 'F'}, 
        'D':{'G','H'},
        'I':{'J'}
        }


# undirected graph without loop
undirected_graph = {
        'A':{'B'}, 
        'B':{'A','C','D'}, 
        'C':{'B','E','F'},
        'D':{'B','G','H'}, 
        'E':{'C'}, 
        'F':{'C'}, 
        'G':{'D'},
        'H':{'D'}
        }

# directed graph with acyclic loop
directed_graph_loop = {
        'A':{'B'}, 
        'B':{'D'}, 
        'C':{'B','E'}, 
        'D':{'G','H'},
        'I':{'J'},
        'F':{'C'},
        'G':{'F'} 
        }


# recursive dfs
# check from a vertex
def recur_dfs(graph, vertex, res):
    seen = set() # record seen vertexes
    def _dfs(v):
        if v in seen:
            return
        seen.add(v)
        res.append(v)
        if v not in graph: return
        for c in graph[v]:
            _dfs(c)
    _dfs(vertex)

def recur_bfs(graph, vertice, res):
    seen = set()
    def _bfs(v):
        todo = []
        for i in v:
            if i in seen: continue
            seen.add(i)
            res.append(i)
            if i not in graph: continue
            todo.extend(graph[i])
        if len(todo) > 0:
            _bfs(todo)
    _bfs([vertice])


# iterative dfs
# start from a vertex
def iter_dfs(graph, vertex, res):
    seen = set()
    q = [vertex]
    while len(q) > 0:
        t = q.pop()
        if t in seen: continue
        seen.add(t)
        res.append(t)
        if t not in graph: continue
        for c in graph[t]:
            q.append(c)
    
def iter_bfs(graph, vertex, res):
    seen = set()
    q = [vertex]
    while len(q) > 0:
        t = q.pop(0)
        if t in seen: continue
        seen.add(t)
        res.append(t)
        if t not in graph: continue
        for c in graph[t]:
            q.append(c)


if __name__ == '__main__':

    print('dfs directed graph with loop --------------------')
    res = []
    recur_dfs(directed_graph_loop, 'A', res)
    print(res)

    res = []
    iter_dfs(directed_graph_loop, 'A', res)
    print(res)

    print('bfs directed graph with loop --------------------')
    res = []
    recur_bfs(directed_graph_loop, 'A', res)
    print(res)

    res = []
    iter_bfs(directed_graph_loop, 'A', res)
    print(res)

    print('dfs undirected graph ----------------------------')
    res = []
    recur_dfs(undirected_graph, 'A', res)
    print(res)
    res = []
    iter_dfs(undirected_graph, 'A', res)
    print(res)


    print('bfs undirected graph ----------------------------')
    res = []
    recur_bfs(undirected_graph, 'A', res)
    print(res)
    res = []
    iter_bfs(undirected_graph, 'A', res)
    print(res)
