import math

from PIL import Image

from graph import Graph


def load_circuit(filename):
    value_matrix = value_matrix_from_file(filename)
    return value_matrix_to_graph(value_matrix)


def value_matrix_from_file(filename):
    with Image.open(f'Circuits/{filename}') as img:
        pixels = img.load()

        value_matrix = [[0 for y in range(img.size[1])] for x in range(img.size[0])]

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                (a, b, c, _) = pixels[x, y]
                value_matrix[x][y] = int(math.sqrt(a * a + b * b + c * c))

    return value_matrix


def try_add_edge(graph, value_matrix, x1, y1, x2, y2):
    if value_matrix[x1][y1] > 0 and value_matrix[x2][y2] > 0:
        graph.add_edge(x1, y1, x2, y2)


def value_matrix_to_graph(value_matrix):
    graph = Graph()

    height = len(value_matrix[0])
    width = len(value_matrix)

    for x in range(width):
        for y in range(height):
            if value_matrix[x][y] > 0:
                graph.add_node(x, y, value_matrix[x][y])

    for x in range(width):
        for y in range(height):
            up = y < height - 1
            down = y > 0
            left = x > 0
            right = x > width - 1

            if up:
                try_add_edge(graph, value_matrix, x, y, x, y + 1)
            if up and left:
                try_add_edge(graph, value_matrix, x, y, x - 1, y + 1)
            if up and right:
                try_add_edge(graph, value_matrix, x, y, x + 1, y + 1)
            if down:
                try_add_edge(graph, value_matrix, x, y, x, y - 1)
            if down and left:
                try_add_edge(graph, value_matrix, x, y, x - 1, y - 1)
            if down and right:
                try_add_edge(graph, value_matrix, x, y, x + 1, y - 1)
            if left:
                try_add_edge(graph, value_matrix, x, y, x - 1, y)
            if right:
                try_add_edge(graph, value_matrix, x, y, x + 1, y)

    return graph
