from typing import List

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets: List[int], length: int) -> List[int]:
    """
    Function to reconstruct a given trip

    Args:
        tickets: List[int]
        length: int

    Returns:
        List: int

    """
    # initialize an empty dictionary:
    cache = {}
    # initionlize an empty list for the length of the tickets list:
    route = [None] * length
    # Here we set up our dictionary(cache).
    # Loop over each ticket in the list and add source as the
    # key and destination as the value:
    for ticket in range(length):
        # if current ticket source is 'NONE',
        if tickets[ticket].source == "NONE":
            # add destination to route instance:
            route[0] = tickets[ticket].destination
        # We hash each ticket such that the starting location
        # is the key and the destination is the value
        cache[tickets[ticket].source] = tickets[ticket].destination
    # For each ticket in the list set the destination to route list
    # then set the source of the next trip to previous trip
    # destination.
    # Then, when constructing the entire route, the ith location
    # in the route can be found by checking the hash table for the
    # i-1th location
    for trip in range(length):
        if route[trip - 1] is not None:
            route[trip] = cache[route[trip - 1]]

    return route

