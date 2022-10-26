

# binary search tree
from secrets import randbelow


def searching(length, answer):
    for i in range(length):
        if length[i] == answer:
            return i
    return -1


searching(5, 2)
