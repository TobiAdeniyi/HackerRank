"""
Alice and Bob each created one problem for HackerRank. 
A reviewer rates the two challenges, awarding points on a 
scale from 1 to 100 for three categories: 
problem clarity, originality, and difficulty.

The rating for Alice's challenge is the triplet:
a = (a[0], a[1], a[2]), 
and the rating for Bob's challenge is the triplet:
b = (b[0], b[1], b[2]).

Input Format:
-------------
The first line contains 3 space-separated integers,
a[0], a[1], and a[2], the respective values in triplet a.

The second line contains 3 space-separated integers,
b[0], b[1], and b[2], the respective values in triplet b.

Sample Input 0:
---------------
5 6 7
3 6 10

Sample Output 0:
----------------
1 1
"""
def compare_the_triplets(a: list, b: list) -> tuple:
    n, m = 0, 0
    for i in range(len(a)):
        n += a[i] > b[i]
        m += a[i] < b[i]
        return n, m
    
if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    b = [int(j) for j in input().split()]

    if len(a) == len(b):
        n, m = compare_the_triplets(a, b)
        print("{} {}".format(n, m))
    else:
        print("Input Error: len(a) != len(b)")