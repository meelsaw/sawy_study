import numpy as np


def floyd_min_dist(dist, i, j, k):
    if k < 0:
        return dist[i][j]
    return min(dist[i][j], dist[i][k] + dist[k][j])


def floyd_main(input_graph):
    num_point = len(input_graph)
    dist = [[np.inf] * num_point for n in range(num_point)]

    for i in range(num_point):
        for j in range(num_point):
            if i == j:
                dist[i][j] = 0
            elif input_graph[i][j] != np.inf:
                dist[i][j] = input_graph[i][j]

    for k in range(num_point):
        for i in range(num_point):
            for j in range(num_point):
                dist[i][j] = floyd_min_dist(dist, i, j, k)

    return dist


example = [
    [0, 5, np.inf, np.inf],
    [50, 0, 15, 5],
    [30, np.inf, 0, 15],
    [15, np.inf, 5, 0]
]

result = floyd_main(example)
for r in result:
    print(r)


# Unit tests
def test_floyd():
    graph = [
        [0, 3, np.inf, 7],
        [8, 0, 2, np.inf],
        [5, np.inf, 0, 1],
        [2, np.inf, np.inf, 0]
    ]

    test = floyd_main(graph)

    # Testing values
    assert test[0][1] == 3
    assert test[0][2] == 5
    assert test[0][3] == 6
    assert test[1][3] == 3
    assert test[2][3] == 1


if __name__ == '__main__':
    test_floyd()
    print("All tests passed.")