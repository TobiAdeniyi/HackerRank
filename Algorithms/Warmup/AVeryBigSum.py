"""
In this challenge, you are required to calculate and 
print the sum of the elements in an array, keeping in 
mind that some of those integers may be quite large.

Input Format:
-------------
The first line of the input consists of an integer n.
The next line contains n space-separated integers contained in the array.

Output Format:
--------------
Return the integer sum of the elements in the array.

Sample Input:
-------------
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output:
-------
5000000015
"""
def very_big_sum(arr: list, n: int) -> int:
    return sum(arr)

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(very_big_sum(arr, n))