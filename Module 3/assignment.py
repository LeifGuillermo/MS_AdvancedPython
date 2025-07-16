from collections import Counter

def calculate_statistics(numbers):
    """
    Calculates the mean, median, and mode of a list of numbers.

    Parameters:
        numbers (list): A list of numeric values.

    Returns:
        dict: A dictionary with keys 'mean', 'median', and 'mode'.
              If the list is empty, all values are None.
              If there is no unique mode (all values appear the same number of times), 'mode' is None.
    """
    if not numbers:
        return {"mean": None, "median": None, "mode": None}

    # Filter out non-numeric values
    numeric_numbers = [x for x in numbers if isinstance(x, (int, float))]
    if not numeric_numbers:
        return {"mean": None, "median": None, "mode": None}

    # Calculate mean
    mean = sum(numeric_numbers) / len(numeric_numbers)

    # Calculate median
    sorted_numbers = sorted(numeric_numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    # Calculate mode
    counts = Counter(sorted_numbers)
    max_count = max(counts.values())
    mode_candidates = [num for num, count in counts.items() if count == max_count]
    # If all values appear the same number of times, mode is None
    if len(mode_candidates) == len(counts):
        mode = None
    else:
        mode = mode_candidates[0] if len(mode_candidates) == 1 else None

    return {"mean": mean, "median": median, "mode": mode}

print(calculate_statistics([1,2,3,4,4,5,5,5]))
print(calculate_statistics([1,2,3]))
print(calculate_statistics([]))
