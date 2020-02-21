
directed_graph_loop = {
        'A':{'B'}, 
        'B':{'D'}, 
        'C':{'B','E'}, 
        'D':{'G','H'},
        'I':{'J'},
        'F':{'C'},
        'G':{'F'} 
        }

directed_graph_loop2 = {
        'A':{'B'}, 
        'B':{'D','C'}, 
        'C':{'E'}, 
        'D':{'G','H'},
        'I':{'J'},
        'F':{'C'},
        'G':{'F'} 
        }


# bfs way
# check if there is acylic loop
# using iterative bfs
# it ignores vertice that leads to cycle
# and count the number of non-cycle vertex
def has_cycle(graph):
    # calc indegrees
    indegrees = dict()
    for e in graph:
        val = indegrees.get(e, 0)
        indegrees[e] = val
        for v in graph[e]:
            val = indegrees.get(v, 0)
            indegrees[v] = val + 1

    q = [x for x in indegrees if indegrees[x] == 0]
    cnt = 0
    while len(q) > 0:
        t = q.pop(0)
        cnt += 1
        if t in graph:
            for x in graph[t]:
                indegrees[x] -= 1
                if indegrees[x] == 0:
                    q.append(x)
    return cnt != len(indegrees)
    

# dfs way
def has_cycle2(graph):
    def _dfs(graph, seen, vertex):
        if vertex in seen: return
        seen[vertex] = 1



if __name__ == '__main__':
    ret = has_cycle(directed_graph_loop)
    print("directed_graph_loop has loop: ", ret)

    ret = has_cycle(directed_graph_loop2)
    print("directed_graph_loop2 has loop: ", ret)
