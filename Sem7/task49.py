import math

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(orbits):
    orbits = list(filter(lambda x: x[0] != x[1], orbits))
    max_square = 0
    farthest_orbit = tuple()
    for orbit in orbits:
        square = (math.pi * orbit[0] * orbit[1])
        if square > max_square:
            max_square = square
            farthest_orbit = tuple(orbit)

    return farthest_orbit

print(*find_farthest_orbit(orbits))
