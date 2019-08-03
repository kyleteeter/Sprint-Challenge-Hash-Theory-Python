#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Set up base case
    if length == 1:
        result = None

    # Loop through weights and insert into hashtable
    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)
        first_set = weight
        second_set = limit - first_set
        retrieve = hash_table_retrieve(ht, second_set)

        if retrieve is not None:
            if retrieve > i:
                result = (retrieve, i)
            elif retrieve < i:
                result = (i, retrieve)

    return print_answer(result)


def print_answer(answer):
    if answer is not None:
        print((answer[0] + " " + answer[1]))
    else:
        print("None")
