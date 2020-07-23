"""
Input: a List of integers
Returns: a List of integers
"""


def product_of_all_other_numbers(arr):
    # Your code here

    # Goal: runtime complexity of O(n)
    # Goal: multiply current value with every value (not self) and put product into a new list
    # Goal: Do not use / 2

    length = len(arr)
    # create output list
    # copy length of input with default values of 0
    output_list = [0] * length
    # variable used as temp storage for individual multiply
    product = 1

    # product is in global scope and will be 1 when the loop starts
    for value in range(length):
        # copying individual value from input array
        product = product * arr[value]

    for value in range(length):
        # assigning value to output list each loop
        # defaults to float
        # output_list[value] = int(product / arr[value])
        output_list[value] = product // arr[value]

    return output_list

    # while len(output) !== len(arr)?
    # or run for item in arr?

    # use list comprehension to target !value ?

    # optimize:
    # keep loops, multiply in a different way (no division)


if __name__ == "__main__":
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [
        2,
        6,
        9,
        8,
        2,
        2,
        9,
        10,
        7,
        4,
        7,
        1,
        9,
        5,
        9,
        1,
        8,
        1,
        8,
        6,
        2,
        6,
        4,
        8,
        9,
        5,
        4,
        9,
        10,
        3,
        9,
        1,
        9,
        2,
        6,
        8,
        5,
        5,
        4,
        7,
        7,
        5,
        8,
        1,
        6,
        5,
        1,
        7,
        7,
        8,
    ]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )
