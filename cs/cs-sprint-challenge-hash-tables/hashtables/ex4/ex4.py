
from typing import List

def has_negatives(a: List[int]) -> List[int]:
    """
    For an input list of integers, we wish to know which positive numbers have
    corresponding negative numbers in the list.

    Args:
        a: List[int] - A list of integers

    Returns:
        List: int

    >>>has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7  ])
    >>>[1, 3, 4]

    """
    # init empty dict:
    cache = {}
    # init empty list for results:
    result = []
    # for each value in the input list:
    for num in a:
        # if value is not in the cache:
        if num not in cache:
            # insert value and set equal to one:
            cache[num] = 1
    # for every value in the input list
    for num in a:
        # *Multiplying a number by −1 is equivalent to changing
        # the sign on the number

        # if the value multiplied by -1 is in the cache
        # and if the value is greater than zero:
        if (num * -1) in cache and num > 0:
            # append the value to the results list:
            result.append(num)
    # return list with results:
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
