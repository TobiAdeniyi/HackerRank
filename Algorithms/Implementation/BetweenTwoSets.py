"""
You will be given two arrays of integers and asked to determine 
all integers that satisfy the following two conditions:

1) The elements of the first array are all factors of the integer being considered
2) The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. 
You must determine how many such numbers exist.

Sample Input:
-------------
2 3
2 4
16 32 96

Sample Output:
--------------
3

Explanation:
------------
2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element 
of a is a factor and each is a factor of all elements of b.
"""
def between_two_sets(a, b):
    k = 0
    for i in range(a[-1], b[0]+1, a[-1]):
        if all(i%j == 0 for j in a) and all(j%i ==0 for j in b):
            k += 1
    return k

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    print(between_two_sets(arr, brr))