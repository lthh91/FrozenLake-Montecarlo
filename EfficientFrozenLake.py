import numpy as np
import random


class FrozenLakeAgent:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = 0

    def moveTo(self, dx, dy, point):
        self.x += dx
        self.y += dy
        self.points += point

    def reset(self):
        self.x = 0
        self.y = 0


class FrozenLake:
    def __init__(self, length):
        lake = np.empty((length, length))
        lake.fill(-1) # Negative value for lengthening the road
        for _ in range(length):
            x, y = np.random.randint(0, length, 2)
            # Exclude already-holed cells, goal cell and leave at least one possible way to get to the goal
            while lake[x, y] == -1000 or (x, y) == (length-1, length-1) or (x, y) == (0, 0) or ((x, y) == (length-1, length-2) and (x, y) == (length-2, length-1)):
                x, y = np.random.randint(0, length, 2)
            lake[x, y] = -1000
        lake[length-1, length-1] = 1000
        self.lake = lake
        self.length = length-1
        self.agent = FrozenLakeAgent()

    def inside(self, x, y):
        if x > self.length or x < 0 or y > self.length or y < 0:
            return False
        return True

    def step(self, direction):
        dx = 0
        dy = 0
        if direction.lower() == 'left':
            dx = -1
        elif direction.lower() == 'right':
            dx = 1
        elif direction.lower() == 'up':
            dy = -1
        elif direction.lower() == 'down':
            dy = 1
        if self.inside(self.agent.x+dx, self.agent.y+dy):
            self.agent.moveTo(dx, dy, self.lake[self.agent.x+dx, self.agent.y+dy])
            return True
        return False

    def gameover(self):
        if self.lake[self.agent.x, self.agent.y] == -1000 or self.lake[self.agent.x,self.agent.y] == 1000:
            return True
        else:
            return False

    def display(self):
        print(self.lake)


lake = FrozenLake(3)
lake.display()
points = []
strategies = []

for _ in range(100):
    end_game = False
    steps = []
    lake.agent.reset()
    while not end_game:
        direction = random.choice(['left', 'right', 'up', 'down'])
        if lake.step(direction):
            steps.append(direction)
            point = lake.agent.points
            end_game = lake.gameover()
            if end_game and point > -1000:
                points.append(point)
                strategies.append(steps)
                print('Done a game')
        # print(lake.agent.x, lake.agent.y)

print(points)
points = np.array(points)
print(strategies[np.argmax(points)])
