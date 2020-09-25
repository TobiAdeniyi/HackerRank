"""
Given an array of integers, calculate the ratios of its elements 
that are positive, negative, and zero. Print the decimal value 
of each fraction on a new line with 6 places after the decimal.

Input Format:
-------------
The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].

Output Format:
--------------
Print the following 3 lines, each to 6 decimals:
1) proportion of positive values
2) proportion of negative values
3) proportion of zeros

Sample Input:
-------------
6
-4 3 -9 0 4 1

Sample Output:
--------------
0.500000
0.333333
0.166667
"""
def plus_minus(arr: list, n: int) -> tuple:
    a, b = 0, 0
    for i in range(n):
        a += arr[i] > 0
        b += arr[i] < 0
    return (a, b, n-a-b)

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    for j in plus_minus(arr, n):
        print("{:.6f}".format(float(j/n)))