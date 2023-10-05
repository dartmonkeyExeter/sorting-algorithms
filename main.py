import random
from timeit import default_timer as timer


def insertion_sort(items):
    num_items = len(items)
    for index in range(1, num_items):
        item_to_insert = items[index]
        position = index - 1
        while position >= 0 and items[position] > item_to_insert:
            items[position + 1] = items[position]
            position = position - 1

        items[position + 1] = item_to_insert
    return items


def bubble_sort(bubble_items):
    length = len(bubble_items)
    swapped = True
    while swapped:
        swapped = False
        for i in range(length - 1):
            if bubble_items[i] > bubble_items[i + 1]:
                bubble_items[i], bubble_items[i + 1] = bubble_items[i + 1], bubble_items[i]
                swapped = True
        length -= 1  # Reduce the range of iterations in subsequent passes
        if not swapped:  # Early termination if no swaps were made
            break
    return bubble_items


def main():
    items = [random.randint(-1000, 1000) for _ in range(10000)]
    start = timer()
    insertion_sort(items)
    end = timer()
    print("Time taken to execute insertion sort (seconds):", end - start)  # Time in
    start = timer()
    bubble_items = [random.randint(-1000, 1000) for _ in range(10000)]
    bubble_sort(bubble_items)
    end = timer()
    print("Time taken to execute bubble sort (seconds):", end - start)  # Time in


if __name__ == "__main__":
    main()
