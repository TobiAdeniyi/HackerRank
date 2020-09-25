"""
ou are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year
of their total age. They will only be able to blow out the 
tallest of the candles. Count how many candles are tallest.

Sample Input 0:
---------------
4
3 2 1 3

Sample Output 0:
----------------
2
"""
import time
def birthday_cake_candles1(candles: list, n: int) -> int:
    tallest = candles[0]
    count = 0
    for i in range(1, n):
        candle = candles[i]
        if candle == tallest:
            count += 1
        elif candle > tallest:
            tallest = candle
            count = 1
    return count

def birthday_cake_candles2(candles: list, n: int) -> int:
    tallest = max(candles)
    return sum([i==tallest for i in candles])

if __name__ == '__main__':
    n = int(input())
    candles = [int(i) for i in input().split()]

    t0 = time.time()
    bcc1 = birthday_cake_candles1(candles, n)
    t1 = time.time()
    bcc2 = birthday_cake_candles2(candles, n) 
    t2 = time.time()

    print("Function 1: {} in {}".format(bcc1, t1-t0))
    print("Function 2: {} in {}".format(bcc2, t2-t1))