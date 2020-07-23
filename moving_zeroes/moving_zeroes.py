"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # Your code here

    # Mutate original arr (return arr)
    # Move any zero values to the end of list (remove & append?)
    # Single pass time complexity O(1)

    for value in arr:
        # if value is 0 remove from current position and place at list end
        if value == 0:
            arr.remove(value)
            arr.append(value)

    return arr

    # optimize:
    # switch order without removing / appending


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
