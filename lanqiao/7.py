import os
import sys
from collections import *


def bfs(x,y):
  global cnt
  q = deque()
  q.append((x,y))
  while q:
    cnt += 1
    for _ in range(len(q)):
      x,y = q.popleft()
      if mp[k] == vis: print(cnt);sys.exit()
      d = [(-1,0),(0,1),(1,0),(0,-1)]
      for i in range(4):
        nx,ny = x+d[i][0],y+d[i][1]
        if 0<=nx<n and 0<=ny<n:
          if mp[k][nx][ny] == '1':
            mp[k][nx][ny] = '0'
            q.append((nx,ny))



num = int(input())
n = int(input())
mp = []
for u in range(num):
  tmp = [list(input()) for _ in range(n)]
  mp.append(tmp)

vis = [['0']*n for _ in range(n)]


for k in range(num):
  cnt = 0
  for i in range(n):
    for j in range(n):
      if mp[k][i][j] == '1':
        bfs(i,j)


'''
1
3
001
011
111
'''



