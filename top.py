# topological sort

# there is a cycle
# A--->B---->D---->G---|
#      ^     |---->H   |
#      |               |
# C----|---->E         |
# ^                    |
# |----------------F<--|
# 
# I---->J
directed_graph_loop = {
        'A':{'B'}, 
        'B':{'D'}, 
        'C':{'B','E'}, 
        'D':{'G','H'},
        'I':{'J'},
        'F':{'C'},
        'G':{'F'} 
        }

# no cycle
# A--->B---->D---->G
#      |     |---->H
#      ✓
# F--->C--->E
# 
# I--->J
directed_graph_loop2 = {
        'A':{'B'}, 
        'B':{'D','C'}, 
        'C':{'E'}, 
        'D':{'G','H'},
        'I':{'J'},
        'F':{'C'},
        }

# iterative bfs
# cycle ignored
def bfs_topo_order(graph):
    indegrees = dict()
    for e in graph:
        val = indegrees.get(e,0)
        indegrees[e] = val
        for v in graph[e]:
            val = indegrees.get(v, 0)
            indegrees[v] = val + 1

    q = [x for x in indegrees if indegrees[x] == 0]
    result = []
    while len(q) > 0:
        t = q.pop(0)
        result.append(t)
        if t in graph:
            for x in graph[t]:
                indegrees[x] -= 1
                if indegrees[x] == 0:
                    q.append(x)
    return result

# recursive dfs
# even there is a cycle, it tries to push nodes of cycle in result
# that may not be what we want sometimes.
def dfs_topo_order(graph):
    seen = set()
    result = []
    def dfs(v):
        if v in seen: return
        seen.add(v)
        if graph.get(v, None) is not None:
            for c in graph[v]:
                dfs(c)
        result.append(v)
    for e in graph:
        dfs(e)
    result.reverse()
    return result


if __name__ == '__main__':
    print('bfs topological sort, cycle ignored')
    ret = bfs_topo_order(directed_graph_loop)
    print(ret)
    ret = bfs_topo_order(directed_graph_loop2)
    print(ret)

    print('dfs topological sort, cycle ignored')
    ret = dfs_topo_order(directed_graph_loop)
    print(ret)
    ret = dfs_topo_order(directed_graph_loop2)
    print(ret)
