import sys

from helper import euclidean_distance, calculate_route_distance, parse_input

def greedy_insertion(loads):
    return [], 0

def main():
    if len(sys.argv) != 2:
        return

    file_path = sys.argv[1]
    loads = parse_input(file_path)
    drivers, total_cost = greedy_insertion(loads)

if __name__ == "__main__":
    main()
