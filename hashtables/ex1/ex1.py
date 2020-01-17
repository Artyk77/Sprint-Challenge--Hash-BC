#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # loop through all weights and insert weight as key, index as value
    for i in range(0, len(weights)):
      hash_table_insert(ht, weights[i], i)

    # loop through all weights again, retrieve items whose index is difference between limit and current weight
    answer = None
    for j in range(0, len(weights)):
      compWeight = hash_table_retrieve(ht, limit - weights[j])
      if compWeight:
        # sort in descending order
        if compWeight > j:
          answer = (compWeight, j)
        else:
          answer = (j, compWeight)
        # once a pair is found, break
        break

    return answer
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")