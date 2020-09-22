from collections import Counter

def pairsofgloves(n,ar):
    n = Counter(ar)
    return sum(i//2 for i in n.values())

n = input()
ar = list(map(int,input().split()))
print(pairsofgloves(n,ar))