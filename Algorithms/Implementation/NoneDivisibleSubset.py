def nds(S: list, k: int) -> int:
    if cross_m(S, k):
        return len(S)
    else:
        Y = []
        for i in range(len(S)-1):
            X = S[:i]
            X.extend(S[i+1:])
            Y.append(max(nds(X, k)))
        return max(Y)

def cross_m(S: list, k: int) -> bool:
    if S == []:
        return True
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if (S[i] + S[j]) % k == 0:
                return False
    return True

if __name__ == '__main__':
    n, k = (int(i) for i in input().split())
    S = [int(i) for i in input().split()]
    print(nds(S, k))