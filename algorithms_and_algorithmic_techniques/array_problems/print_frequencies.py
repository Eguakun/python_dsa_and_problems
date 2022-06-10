from collections import Counter
from algorithms_and_algorithmic_techniques.helpers import get_a_list as g
def freq(array, element):


    c = Counter(array)
    if element not in c:
        return -1

    return c[element]

array = [1,2,3,4,5,5,5,5,5,5,5, 3, 4]


print(freq(array,-8))