import sys

from helper import euclidean_distance, calculate_route_distance, parse_input, calculate_total_cost

MAX_DRIVE_TIME = 720

def greedy_insertion(loads):
    depot = (0, 0)
    drivers = []
    remaining_loads = set(loads)

    while remaining_loads:
        route = []
        current_distance = 0
        current_location = depot

        while remaining_loads and current_distance <= MAX_DRIVE_TIME:
            best_load = None
            best_increase = float('inf')

            for load in remaining_loads:
                increase = euclidean_distance(current_location, load.pickup) + euclidean_distance(load.pickup, load.dropoff)
                if current_distance + increase + euclidean_distance(load.dropoff, depot) <= MAX_DRIVE_TIME:
                    if increase < best_increase:
                        best_increase = increase
                        best_load = load

            if best_load is None:
                break

            route.append(best_load)
            current_distance += best_increase
            current_location = best_load.dropoff
            remaining_loads.remove(best_load)

        drivers.append(route)

    total_cost = 500 * len(drivers) + sum(calculate_route_distance(driver) for driver in drivers)
    return drivers, total_cost

def main():
    if len(sys.argv) != 2:
        return

    file_path = sys.argv[1]
    loads = parse_input(file_path)
    drivers, total_cost = greedy_insertion(loads)

    for driver in drivers:
        load_ids = [load.load_id for load in driver]
        print(f"[{','.join(map(str, load_ids))}]")

if __name__ == "__main__":
    main()
