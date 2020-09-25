"""
Given an array of integers, find the sum of its elements.

Input format:
The first line contains an integer, n, denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Sample input:
6
1 2 3 4 10 11

Sample output:
31
"""
def simple_array_sum(arr: list, n: int) -> object:
    print(sum(arr))

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]

    simple_array_sum(arr, n)