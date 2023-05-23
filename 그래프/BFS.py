'''
BFS는 재귀로 구현할 수 없으며, queue로만 구현이 가능함을 기억해야함
'''

def BFS_queue(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
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

print(BFS_queue(1))