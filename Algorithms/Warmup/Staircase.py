"""
This is a staircase of size n = 4:

   #
  ##
 ###
####

Input Format:
-------------
A single integer, , denoting the size of the staircase.

Output Format:
--------------
Print a staircase of size  using # symbols and spaces.
Note: The last line must have  spaces in it.
"""
def staircase(n: int) -> str:
    for i in range(1, n+1):
        print((n-i)*" " + (i)*"#")

if __name__ == '__main__':
    n = int(input())
    staircase(n)