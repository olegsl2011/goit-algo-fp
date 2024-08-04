import random


def random_unique_int_list(min_len, max_len, min_val, max_val):
    if min_len < 0 or max_len < min_len or min_val > max_val:
        raise ValueError("Invalid input parameters")

    length = random.randint(min_len, max_len)
    return random.sample(range(min_val, max_val), length)
