#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # loop through all the tickets
    for i in range(0, len(tickets)):
        
      # set the first ticket's destination as the first leg in the route
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
      # otherwise, insert the legs in the hash-table for retrieval later
        else:
            hash_table_insert(
                hashtable, tickets[i].source, tickets[i].destination)


    # loop through the tickets again, finding all the legs whose source is the previous destination
    # save that leg's destination as the next leg in the route
    for j in range(1, len(route)):
        stop = hash_table_retrieve(hashtable, route[j - 1])
        route[j] = stop

    return route
