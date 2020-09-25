"""
Given a square matrix, calculate the absolute 
difference between the sums of its diagonals.

Input Format:
-------------
The first line contains a single integer, n, the number 
of rows and columns in the square matrix arr. 
Each of the next n lines describes a row, arr[i], and 
consists of n space-separated integers arr[i][j].

Output Format:
--------------
Return the absolute difference between the sums of 
the matrix's two diagonals as a single integer.

Sample Input:
-------------
3
11 2 4
4 5 6
10 8 -12

Sample Output:
--------------
15
"""
def diagonal_difference(arr: list, n: int) -> int:
    l2r, r2l = 0, 0
    for i in range(n):
        l2r += arr[i][i]
        r2l += arr[i][n-i-1]
    return abs(l2r - r2l)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append([int(i) for i in input().split()])
    
    diff = diagonal_difference(arr, n)
    print(diff)