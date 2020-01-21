#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    index = 0
    for w in weights:
        hash_table_insert(ht, w, index)
        index += 1
    
    for w in range(length):
        if hash_table_retrieve(ht, limit - weights[w]) is not None:
            if hash_table_retrieve(ht, weights[w]) > hash_table_retrieve(ht, limit-weights[w]):
                greater = weights[w]
                less = limit - weights[w]
            else:
                greater = limit - weights[w]
                less = weights[w]
                print(f'greater: {greater}, less: {less}')
                print(hash_table_retrieve(ht, greater))

            return [hash_table_retrieve(ht, greater), hash_table_retrieve(ht, less)]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
