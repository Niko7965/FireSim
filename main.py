from time import sleep

import pygame
from pygame_screen_record import ScreenRecorder

from circuitloader import load_circuit
from drawing import Graphics
from graph import Graph

graphics = Graphics()
graph: Graph = load_circuit('circuitupdated.png')
graphics.update(graph.nodes)

# graph.nodes[0].ignite()
# graph.nodes[1].put_on_cooldown(40)

tick_no = 0

recorder = ScreenRecorder()
recorder.start_rec(30)

try:
    while True:
        pygame.event.get()
        sleep(0.1)

        for node in graph.nodes:
            node.update()

        tick_no += 1
        print(tick_no)

        graphics.update(graph.nodes)
except KeyboardInterrupt:
    recorder.stop_rec().stop_rec()
    recorder.save_recording("Mallis_first_record1ng.mp4")
    pygame.quit()
