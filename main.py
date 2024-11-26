from time import sleep

import pygame

from circuitloader import load_circuit
from drawing import Graphics
from graph import Graph

graphics = Graphics()
graph: Graph = load_circuit('circuit.png')
graphics.update(graph.nodes)

graph.nodes[0].ignite()
graph.nodes[1].put_on_cooldown(40)

tick_no = 0

while True:
    pygame.event.get()
    sleep(0.1)

    for node in graph.nodes:
        node.update()

    tick_no += 1
    print(tick_no)

    graphics.update(graph.nodes)

input("Press any key to end")
