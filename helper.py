from models import Load
from math import sqrt

def euclidean_distance(point1, point2):
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def calculate_total_cost(drivers):
    return 500 * len(drivers) + sum(calculate_route_distance(driver) for driver in drivers)

def calculate_route_distance(route, depot=(0, 0)):
    total_distance = 0
    current_location = depot
    for load in route:
        total_distance += euclidean_distance(current_location, load.pickup)
        total_distance += euclidean_distance(load.pickup, load.dropoff)
        current_location = load.dropoff
    total_distance += euclidean_distance(current_location, depot)
    return total_distance

def parse_input(file_path):
    loads = set()
    with open(file_path, 'r') as file:
        for line in file.readlines()[1:]:
            parts = line.strip().split()
            load_id = int(parts[0])
            pickup = tuple(map(float, parts[1].strip('()').split(',')))
            dropoff = tuple(map(float, parts[2].strip('()').split(',')))
            distance = euclidean_distance(pickup, dropoff)
            loads.add(Load(load_id, pickup, dropoff, distance))
    return loads

