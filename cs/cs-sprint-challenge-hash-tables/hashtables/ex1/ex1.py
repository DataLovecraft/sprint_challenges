from typing import List, Tuple

def get_indices_of_item_weights(weights: List[int], length: int, limit: int) -> Tuple[int, int]:
    """
    Function finds two items whose sum of weights equals the weight list.

    Args:
        weights: List[int]
        length: int
        limit: int

    Returns:
        Tuple: int

    """
    # local var to init a empty python dict:
    cache = {}

    # iterate through list: 0(n)
    for elem in range(len(weights)):
        # compute the difference of weights for each element in
        # the list:
        diff_weights = limit - weights[elem]
        # add to cache: 0(1)
        if diff_weights in cache:
            # if the difference is in the cache:
            # the weight of a set A refers to elements not in A.
            weight = cache[diff_weights]
            # higher valued index placed in the `zeroth` index
            # smaller valued index placed in the `first` index
            weight_limit = (elem, weight)
            return weight_limit
        else:
            # store each weight's index as its value:
            cache[weights[elem]] = elem
    # If such a pair doesn’t exist for the given inputs return None:
    return None

assert get_indices_of_item_weights(weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21) == (3, 1)
