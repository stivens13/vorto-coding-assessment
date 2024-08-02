import sys

from helper import euclidean_distance, calculate_route_distance, parse_input, calculate_total_cost


def greedy_insertion(loads):
    drivers = []

    total_cost = calculate_total_cost(drivers)
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
