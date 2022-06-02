import random

def generate_sorted_random_list(n):
    random_list = []
    for i in range(0, n):
        n = random.randint(1, 300)
        random_list.append(n)
    return sorted(random_list)

def generate_random_list(n):
    random_list = []
    for i in range(0, n):
        n = random.randint(1, 300)
        random_list.append(n)
    return random_list