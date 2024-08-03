from models import Load
from math import sqrt

def euclidean_distance(point1, point2):
    return sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

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

def print_routes(drivers):
    for driver in drivers:
        load_ids = [load.load_id for load in driver]
        print(f"[{','.join(map(str, load_ids))}]")
