import os
import sys
from collections import *

n = int(input())
a = input()
b = input()

vis = set()


def push(s):
    if s not in vis:
        vis.add(s)
        q.append(s)


def change(s, i, j):
    s_a = '1' + s
    i = j * 10 ** (n - i)
    s_b = eval(s_a + str('+') + str(i))
    s_b = str(s_b)
    s_c = s_b[1:]
    return s_c


q = deque()
push(a)
cnt = -1
while q:
    cnt += 1
    for _ in range(len(q)):
        s = q.popleft()
        if s == b: print(cnt);sys.exit()
        for i in range(1, n + 1):
            for j in [-1, 1]:
                s_new = change(s, i, j)
                push(s_new)






