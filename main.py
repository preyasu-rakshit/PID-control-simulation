import pygame
import sys
from objects import Rocket, PID
from matplotlib import pyplot as plt
import numpy as np

width = 1280
height = 720
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PID")
clock = pygame.time.Clock()

target = height/3
dt = 1/60
kp = 0.4
ki = 0.3    
kd = 0.02
rocket = Rocket(width/2, 2*height/3, target)
controller = PID(rocket, kp, ki, kd, target, 1/60)

poses = np.array([])
times = np.array([])

def graph(x, y):
    plt.plot(x, y)
    plt.show()

f = 0
time = 0
while f < 250:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0, 0, 0))
    pygame.draw.aaline(screen, (0, 255, 0), (0,target), (1280, target))
    rocket.update(screen)
    controller.update()
    pygame.display.flip()
    poses = np.append(poses, height - rocket.y)
    times = np.append(times, time)
    f += 1
    time += dt
    clock.tick(60)

graph(times, poses)