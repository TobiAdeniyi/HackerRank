import os
"""
Sample Input
------------
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output
-------------
9
"""


def designer_viewer(h: list, word: str) -> int:
    # 1)  Convert word to lower case
    word = word.lower()
    # print(word)

    # 2)  Convert word to unicode representation - 97
    coded = [ord(char) - 97 for char in word]
    # print(coded)

    # 3)  For each chr in word find corresponding number in h
    height_collection = [h[i] for i in coded]
    # print(height_collection)

    # 4)  Return max number * length of word
    return max(height_collection) * len(word)


if __name__ == '__main__':
    # none return value
    h = list(int(i) for i in input().rstrip().split())
    word = input()
    result = designer_viewer(h, word)
    print(result)
