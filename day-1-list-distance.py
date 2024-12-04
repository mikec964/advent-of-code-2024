location_ids1: list[int] = [3, 4, 2, 1, 3, 3]
location_ids2: list[int] = [4, 3, 5, 3, 9, 3]


def load_lists(filename = "day-1-input.txt") -> tuple[list[int], list[int]]:
    """Read a file with two numbers per row, return a list per column.
    
    Columns are separated by white space."""

    with open(filename, "r") as f:
        list_text:list[str] = f.readlines()
    list1: list[int] = []
    list2: list[int] = []
    for line in list_text:
        left, right = line.split()
        list1.append(int(left))
        list2.append(int(right))
    return list1, list2


def calc_list_distance(list1: list[int], list2: list[int]) -> int:
    total_distance:int = 0
    list1_sorted: list[int] = sorted(list1)
    list2_sorted: list[int] = sorted(list2)
    for idx in range(0, len(list1)):
        distance: int = abs(list1_sorted[idx] - list2_sorted[idx])
        if idx < 10:
            print(f"...{list1_sorted[idx]} - {list2_sorted[idx]} = {distance}")
        total_distance += distance
    return total_distance


def calc_list_similarity(list1: list[int], list2: list[int]) -> int:
    """Similarity score per line is left item * number of occurrances in right list."""
    total_similarity: int = 0
    for idx, left_item in enumerate(list1):
        similarity = left_item * list2.count(left_item)
        if idx < 10:
            print(f"...{left_item}, {list2.count(left_item)}, {similarity}")
        total_similarity += similarity
    return total_similarity


print(f"Difference {calc_list_distance(location_ids1, location_ids2)}")
print(f"Similarity {calc_list_similarity(location_ids1, location_ids2)}")

locations1, locations2 = load_lists()
print(f"Difference {calc_list_distance(locations1, locations2)}")
print(f"Similarity {calc_list_similarity(locations1, locations2)}")
