"""

Complete the function solveMeFirst to compute the sum of two integers.

Sample input:
2
3

Sample output:
5

"""
def solve_me_first(a: int, b: int) -> int:
    print(a+b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    solve_me_first(a, b)