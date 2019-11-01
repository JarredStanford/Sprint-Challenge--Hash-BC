#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """



    for index, weight in enumerate(weights):
        if hash_table_retrieve(ht, (limit-weight)) is not None:
            return [index, hash_table_retrieve(ht, (limit - weight))]
        hash_table_insert(ht, weight, index)
    

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
