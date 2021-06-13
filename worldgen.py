from voxel import *
from opensimplex import OpenSimplex
from time import sleep

y = 1
engine = Engine(input("Token? "))
noise = OpenSimplex(int(input("Seed? ")))
SEA_LEVEL = 4

for i in range(30):
    for j in range(30):
        height = int(5 * noise.noise2d(i * 0.12, j * 0.12) + 4)
        beach = height < SEA_LEVEL + 1

        while y < height:
            engine.move(UP)
            y += 1
            sleep(1)
            voxel = Voxels.BROWN
            if y == height:
                voxel = Voxels.YELLOW if beach else Voxels.LIME
            engine.set(DOWN, voxel)
            sleep(1)
        while y < SEA_LEVEL:
            engine.move(UP)
            y += 1
            sleep(1)
            engine.set(DOWN, Voxels.CYAN)
            sleep(1)
        engine.move(EAST)
        sleep(1)
        while y > 1:
            engine.move(DOWN)
            y -= 1
            sleep(1)
    engine.move(NORTH)
    sleep(1)
    for j in range(30):
        engine.move(WEST)
        sleep(1)
