# floyd_warshall algorithm
# 1. 初始化距離矩陣
# 2. 更新距離矩陣
# 3. 輸出距離矩陣
# this is a bad algorithm, it's not efficient O(n^3)


def floyd_warshall(graph):
    n = len(graph)
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in graph:
        dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
