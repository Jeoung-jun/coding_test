# 재귀를 이용한 DFS의 구현
def DFS_recur(G,v, discovered = []):
    discovered.append(v)
    for w in G[v]:
        if w not in discovered:
            DFS_recur(G,w,discovered)
    return discovered

#stack을 이용한 DFS의 구현
def DFS_stack(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v][::-1]:
                stack.append(w)
    return discovered

graph = {
    1: [2,3,4],
    2: [5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

print(DFS_recur(graph, 1))
print(DFS_stack(1))