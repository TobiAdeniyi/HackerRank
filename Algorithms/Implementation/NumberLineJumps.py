"""
Sample Input:
-------------
0 3 4 2

Sample Output:
--------------
YES
"""
def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return "YES"
    elif v1 == v2:
        return "NO"
    z = (x2-x1)*(v2-v1) < 0
    y = ((x2-x1)/(v1-v2))%1 == 0
    return "YES"*(y and z) + "NO"*((1-y) or (1-z)) 

if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)