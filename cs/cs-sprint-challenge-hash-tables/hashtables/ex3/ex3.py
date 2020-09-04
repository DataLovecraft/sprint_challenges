from typing import List

def intersection(arrays: List[List[int]]) -> List[int]:
    """
    Function to find the intersection between multiple lists of integers.

    """
    cache = {}
    # First step is to populate our dict with the numbers and their count:
    for subarrays in arrays:
        for num in subarrays:
            # if the number is in the cache:
            if num in cache:
                # raise num count by one:
                cache[num] += 1
            # if the number is not in the cache:
            else:
                # add the number to the cache:
                cache[num] = 1
            # cache should look like:
            # {1: 3, 2: 3, 3: 1, 4: 1, 5: 1, 12: 1, 7: 2, 9: 1, 99: 1}
    # Now we can use the dict to search for all values that equal to 3
    result = []
    for key in cache:
        if cache[key] == len(arrays):
            result.append(key)  # and append them to our results list
    # return results
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
