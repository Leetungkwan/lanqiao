import os
import sys
from time import *

def check(k):
    vis = [0] * (length + 1)
    for i in range(1, n + 1):
        if k >= s[i]:
            for j in range(l[i] - (k - s[i]), l[i] + (k - s[i]) + 1):
                if 0 <= j < length + 1:
                    vis[j] = 1
    if vis == [1] * (length + 1):
        return 1
    else:
        return 0


n, length = map(int, input().split())

l = [0] * (n + 1)
s = [0] * (n + 1)
for i in range(1, n + 1):
    l[i], s[i] = map(int, input().split())

L = 0
R = int(10 ** 6)
while L < R:
    mid = (L + R + 1) // 2
    if check(mid):
        R = mid - 1
    else:
        L = mid

print(L + 1)



'''
3 10
1 1
6 5
10 2
'''