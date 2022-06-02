from algorithms_and_algorithmic_techniques.helpers import get_a_list

# Time complexity: O(n * log(n))
# Sorts based on known total ordering principle of data
# Divide and Conquer Algorithm
# Breaks Down problem into multiple subproblems recursively until they bevome simple to solve.

# Merge Sort:
# 1 - Split Array in Half
# 2 - Call Merge Sort on each half to sort them recursively
# 3 - Merge both sorted halves into one sorted array

def merge_sort(arr):

    if len(arr) > 1:

        # from beginning to midpoint
        left_arr = arr[:len(arr)//2]

        # from midpoint to end of the array
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        leftmost_element_in_left_array = 0
        leftmost_element_in_right_array = 0
        index_in_merged_array = 0

        while leftmost_element_in_left_array < len(left_arr) and leftmost_element_in_right_array < len(right_arr):
            if left_arr[leftmost_element_in_left_array] < right_arr[leftmost_element_in_right_array]:
                arr[index_in_merged_array] = left_arr[leftmost_element_in_left_array]
                leftmost_element_in_left_array += 1
            else:
                arr[index_in_merged_array] = right_arr[leftmost_element_in_right_array]
                leftmost_element_in_right_array += 1
            index_in_merged_array += 1

        while leftmost_element_in_left_array < len(left_arr):
            arr[index_in_merged_array] = left_arr[leftmost_element_in_left_array]

            leftmost_element_in_left_array += 1
            index_in_merged_array += 1

        while leftmost_element_in_right_array < len(right_arr):
            arr[index_in_merged_array] = right_arr[leftmost_element_in_right_array]
            leftmost_element_in_right_array += 1
            index_in_merged_array += 1
        return arr








arr_test = get_a_list.generate_random_list(10)
print(merge_sort(arr_test))



