"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    # Your code here

    # cases for eating 1, 2, or 3 cookies at a time
    # case 1: eat 1 cookie or if there aren't any cookies
    if n <= 1:
        return 1
    # case 2: eat 2 cookies
    elif n == 2:
        return 2
    # case 3: eat 3 cookies and call recursion to try to eat more than 3 cookie total
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    # test throws error, expecting a 2nd argument in the parameters?


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
