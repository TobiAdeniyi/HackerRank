"""
Given five positive integers, find the minimum and maximum
values that can be calculated by summing exactly four of the
five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.

Sample Input:
-------------
1 2 3 4 5

Sample Output:
--------------
10 14
"""
def min_max_sum(arr: list) -> tuple:
    x = [sum(arr) - i for i in arr]
    return min(x), max(x)

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    a, b = min_max_sum(arr)
    print("{} {}".format(a, b))