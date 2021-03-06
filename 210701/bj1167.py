# bfs / dfs 구현 방법 수정 예정 코드 


import sys
from collections import deque

N = int(sys.stdin.readline().strip())
graph = {i: deque() for i in range(1, N + 1)}

for i in range(1, N + 1):
    _input = list(map(int, sys.stdin.readline().strip().split(" ")))
    for j in range(1, len(_input) // 2):
        graph[_input[0]].append([_input[2 * j - 1], _input[2 * j]])


def bfs(start):
    visited = [-1] * (N + 1)
    _queue = deque()
    _queue.append(start)
    visited[start] = 0
    _max = [0, 0]

    while _queue:
        parent_node = _queue.popleft()
        for e, w in graph[parent_node]:
            if visited[e] == -1:
                visited[e] = visited[parent_node] + w
                _queue.append(e)
                if _max[0] < visited[e]:
                    _max = visited[e], e
    return _max


second_input = bfs(1)[1]
anw = bfs(second_input)[0]
print(anw)
