"""
An arcade game player wants to climb to the top of the leaderboard and track their 
ranking. The game uses Dense Ranking, so its leaderboard works like this:

• The player with the highest score is ranked number  on the leaderboard.
• Players who have equal scores receive the same ranking number, and the 
    next player(s) receive the immediately following ranking number.
"""
def climbing_leaderboard(N: list, M: list) -> list:
    X = list(set(N))
    X.sort(reverse=True)
    J = []
    j = len(X)
    for m in M:
        while (j>0) and (m >= X[j-1]):
            j -= 1
        J.append(j+1)
    return J

if __name__ == '__main__':
    n = int(input())
    N = [int(i) for i in input().split()]

    m = int(input())
    M = [int(i) for i in input().split()]
    
    J = climbing_leaderboard(N, M)
    for j in J:
        print(j)