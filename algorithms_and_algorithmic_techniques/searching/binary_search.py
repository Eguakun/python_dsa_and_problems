# Time complexity of merge sort
# O( log(n))

import random


class Search:
    def binary_search(self, array, target):
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                return array[mid]
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


s = Search()




