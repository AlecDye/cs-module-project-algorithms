"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(nums, k):
    # Your code here

    # need to run a loop on 3 items at a time
    # find the largest value within those 3 values
    # return array with largests values from each loop

    max_values = []

    window = [0] * k

    for items in range(0, len(nums) - k + 1):
        # nums list at position items initialized at to items + k
        window = nums[items : items + k]
        # max built in will select the desired largest values
        max_values.append(max(window))

    return max_values


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
