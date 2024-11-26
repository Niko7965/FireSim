IGNITE_THRESHOLD = 100
EXTINGUISH_THRESHOLD = 20

FLAT_COOLDOWN = 20

FLAMINESS_COOLDOWN_COEFFICIENT = 0
FLAMINESS_FLAME_TRANSFER_COEFFICIENT = 0.001

FLAT_FLAME_LOSS = 1
FLAMINESS_LOSS_COEFFICIENT = 0.01


class Node:
    def __init__(self, x, y, flaminess):
        self.lit = False
        self.in_cooldown = False
        self.cooldown = 0
        self.current_flame = 0
        self.flaminess = flaminess
        self.x = x
        self.y = y
        self.neighbors = []

    def update(self):
        if self.in_cooldown:
            self.cooldown -= 1

            if self.cooldown == 0:
                self.in_cooldown = False
            else:
                return

        if self.lit and self.current_flame < EXTINGUISH_THRESHOLD:
            self.lit = False
            self.in_cooldown = True
            self.cooldown = FLAT_COOLDOWN + self.flaminess * FLAMINESS_COOLDOWN_COEFFICIENT
            return

        if not self.lit and self.current_flame > IGNITE_THRESHOLD:
            self.lit = True

        if self.lit:
            self.current_flame -= FLAT_FLAME_LOSS + self.flaminess * FLAMINESS_LOSS_COEFFICIENT

            for neighbor in self.neighbors:
                self.send_flame_to_neighbour(neighbor)

    def ignite(self):
        self.current_flame = IGNITE_THRESHOLD + 1

    def add_flame(self, flame):
        self.current_flame += flame

    def add_neighbor(self, neighbour):
        self.neighbors.append(neighbour)

    def put_on_cooldown(self, cooldown):
        if cooldown > self.cooldown:
            self.cooldown = cooldown
            self.in_cooldown = True

    def send_flame_to_neighbour(self, neighbor):
        if not neighbor.is_lit() and not neighbor.is_on_cooldown():
            neighbor.add_flame(self.current_flame * self.flaminess * FLAMINESS_FLAME_TRANSFER_COEFFICIENT)

    def get_current_flame(self):
        return self.current_flame

    def is_lit(self):
        return self.lit

    def is_on_cooldown(self):
        return self.in_cooldown
