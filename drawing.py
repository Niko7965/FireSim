import pygame

from node import Node

PIXEL_SIZE = 20

COOLDOWN_COLOR = (0, 0, 255)
UNLIT_COLOR = (0, 255, 0)


def node_color(node: Node):
    if node.is_on_cooldown():
        return COOLDOWN_COLOR
    if not node.is_lit():
        return UNLIT_COLOR

    value = min(node.get_current_flame(), 255)
    return value, 0, 0


class Graphics:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))

    def update(self, nodes: list[Node]):
        self.window.fill((0, 0, 0))

        for node in nodes:
            pygame.draw.rect(self.window, node_color(node),
                             (node.x * PIXEL_SIZE, node.y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE), 0)
        pygame.display.update()
