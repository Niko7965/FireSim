import math

from PIL import Image

from graph import Graph


def load_circuit(filename):
    value_matrix, blue_nodes, green_nodes = value_matrix_from_file(filename)
    graph = value_matrix_to_graph(value_matrix)
    for node_x, node_y in blue_nodes:
        graph.ignite_node(node_x, node_y)

    for node_x, node_y in green_nodes:
        graph.cooldown_node(node_x, node_y, 40)

    return graph


def value_matrix_from_file(filename):
    with Image.open(f'Circuits/{filename}') as img:
        pixels = img.load()

        blue_nodes = []
        green_nodes = []

        value_matrix = [[0 for y in range(img.size[1])] for x in range(img.size[0])]

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                (r, g, b, _) = pixels[x, y]
                if r == 0 and g == 255 and b == 0:
                    green_nodes.append((x, y))
                if r == 0 and g == 0 and b == 255:
                    blue_nodes.append((x, y))
                value_matrix[x][y] = int(math.sqrt(r * r + g * g + b * b))

    return value_matrix, blue_nodes, green_nodes


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
