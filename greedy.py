import sys

from helper import euclidean_distance, parse_input, print_routes

# GreedyInsertion provides algorithm for solving VRP
class GreedyInsertion:
    def __init__(s, loads, max_drive_time=720):
        s.loads = loads
        s.depot = (0, 0)
        s.max_drive_time = max_drive_time

    # calculate_routes is an entrypoint to GreedyInsertion and leverages the logic
    def calculate_routes(s):
        drivers = []
        remaining_loads = s.loads

        while remaining_loads:
            route, current_location, current_distance = s.find_optimal_route(
                remaining_loads,
                current_location=s.depot,
                current_distance=0,
                route=[])

            drivers.append(route)

        return drivers

    # find_optimal_route calculates remaining loads to find next best route for a driver
    def find_optimal_route(s, remaining_loads, current_location, current_distance, route):
        while remaining_loads and current_distance <= s.max_drive_time:
            best_load, best_increase = s.find_best_load(remaining_loads, current_location, current_distance)

            if best_load is None:
                break

            route.append(best_load)
            current_distance += best_increase
            current_location = best_load.dropoff
            remaining_loads.remove(best_load)

        return route, current_location, current_distance

    # find_best_load calculates next best load in a route
    def find_best_load(s, remaining_loads, current_location, current_distance):
        best_load = None
        best_increase = float('inf')
        for load in remaining_loads:
            increase = euclidean_distance(current_location, load.pickup) + load.distance
            if current_distance + increase + euclidean_distance(load.dropoff, s.depot) <= s.max_drive_time:
                if increase < best_increase:
                    best_increase = increase
                    best_load = load
        return best_load, best_increase

def main():
    if len(sys.argv) != 2:
        return

    # reads file path from program's input
    file_path = sys.argv[1]
    # reads and loads data into set of Type[Load]
    loads = parse_input(file_path)
    # init solver algorithm
    greedy = GreedyInsertion(loads)
    # start algorithm and get list of driver routes
    drivers = greedy.calculate_routes()
    # print routes in required format
    print_routes(drivers)


if __name__ == "__main__":
    main()
