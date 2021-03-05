"""
Sample Input
------------
3
0
1
4

Sample Output
-------------
1
2
7
"""


def utopian_tree(n: int) -> int:
    tree_height = 1
    for j in range(n):
        if j % 2 != 0:
            tree_height += 1
        else:
            tree_height *= 2
    return tree_height


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        print(utopian_tree(n))
