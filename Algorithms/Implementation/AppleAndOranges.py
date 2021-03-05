"""
Sam's house has an apple tree and an orange tree that yield an 
abundance of fruit. Using the information given below, determine 
the number of apples and oranges that land on Sam's house.

In the diagram below:

The red region denotes the house, where s is the start point, 
and t is the endpoint. The apple tree is to the left of the 
house, and the orange tree is to its right.

Assume the trees are located on a single point, where the 
apple tree is at point a, and the orange tree is at point b.

When a fruit falls from its tree, it lands d units of distance 
from its tree of origin along the x-axis. *A negative value of 
d means the fruit fell d units to the tree's left, and a positive 
value of d means it falls d units to the tree's right. *

Sample Input:
-------------
7 11
5 15
3 2
-2 2 1
5 -6

Sample Output:
--------------
1
1
"""
def apple_and_oranges(A: list, B: list, C: tuple) -> object:
    X = sum([C[0] <= a <= C[1] for a in A])
    Y = sum([C[0] <= b <= C[1] for b in B])
    return X, Y

if __name__ == '__main__':
    s, t = (int(i) for i in input().split())
    a, b = (int(i) for i in input().split())
    _, _ = (int(i) for i in input().split())
    
    A = [int(i)+a for i in input().split()]
    B = [int(i)+b for i in input().split()]

    X, Y = apple_and_oranges(A, B, (s, t))
    print(X)
    print(Y)