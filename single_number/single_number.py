"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""
# Runtime complexity of O(1) expected


def single_number(arr):
    # Goal: Runtime of O(1)
    # init local array to store checked values?
    # store values in local array
    output_list = []
    # on next passes check if current value is already in array
    # remove array value if true?
    for value in arr:
        # check if value is in list
        # if value is already in the list remove it (duplicate value)
        if value in output_list:
            output_list.remove(value)
        # for all values, add to list
        else:
            output_list.append(value)

    return output_list[0]  # need to target start position in list not entire list

    # error: int object is not iterable -> loop runs on arr not len(arr)


if __name__ == "__main__":
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
