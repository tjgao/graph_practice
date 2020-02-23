# there is a cycle
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
directed_graph_loop2 = {
        'A':{'B'}, 
        'B':{'D','C'}, 
        'C':{'E'}, 
        'D':{'G','H'},
        'I':{'J'},
        'F':{'C'},
        }


# bfs way
# check if there is no cycle
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
# the graph can be a forest, so we need to mark nodes with different colors
# 0, not visited, 1, being visited now, 2, visited before
def has_cycle2(graph):
    seen = dict()
    def _dfs(graph, seen, vertex):
        if seen.get(vertex, 0) == 1: 
            return True
        seen[vertex] = 1
        res = False
        if vertex in graph:
            for x in graph[vertex]:
                if _dfs(graph, seen, x):
                    res = True
                    break
        seen[vertex] = 2
        return res

    for e in graph:
        if len(e) > 0 and seen.get(e[0], 0) == 0 and _dfs(graph, seen, e[0]):
            return True
    return False

# union find
# for directed graph, union find may not work, as there may be more than one
# edges come out or go into a node.
# it is ok to use union find to detect weak cycles (ignore directions), but not
# strong cycles
# another big advantage is, union find can dynamically detect cycle in undirected graph
# without creating a full graph beforehand
class UF:
    def __init__(self, path_compress=True):
        self.root = dict()
        self.rank = dict()
        self.path_comp = path_compress

    def findRoot(self, vertex):
        v = vertex
        while v != None:
            vertex = v 
            v = self.root.get(vertex, None) 
        return vertex

    def connect(self, a, b):
        ra, rb = self.findRoot(a), self.findRoot(b)
        if ra == rb:
            return False
        else:
            if self.path_comp:
                rk1, rk2 = self.rank.get(ra, 0), self.rank.get(rb, 0)
                if rk1 < rk2:
                    self.root[ra] = rb
                elif rk1 > rk2:
                    self.root[rb] = ra
                else:
                    self.root[rb] = ra
                    self.rank[ra] = rk1 + 1
            else:
                self.root[b] = a
        return True

def has_cycle3(graph):
    uf = UF()
    for e in graph:
        if len(graph[e]) > 0:
            for x in graph[e]:
                if not uf.connect(e, x):
                    return True
    return False


if __name__ == '__main__':
    ret = has_cycle(directed_graph_loop)
    print("bfs: directed_graph_loop has loop: ", ret)

    ret = has_cycle(directed_graph_loop2)
    print("bfs: directed_graph_loop2 has loop: ", ret)


    ret = has_cycle2(directed_graph_loop)
    print("dfs: directed_graph_loop has loop: ", ret)

    ret = has_cycle2(directed_graph_loop2)
    print("dfs: directed_graph_loop2 has loop: ", ret)

    ret = has_cycle3(directed_graph_loop)
    print("union find: directed_graph_loop has loop: ", ret)

    ret = has_cycle3(directed_graph_loop2)
    print("union find: directed_graph_loop2 has loop: ", ret)


