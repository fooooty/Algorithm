import sys

#sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
ans = [10e9] * (n + 1)
check = [0] * (n + 1)
k = int(sys.stdin.readline())
for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append([b, c])
nextidx = [k, 0]
ans[k] = 0
while True:
  idx = nextidx[0]
  nextidx = [0, 10e9]
  check[idx] = 1
  for i in graph[idx]:
    ans[i[0]] = min(ans[i[0]], ans[idx] + int(i[1]))
  cnt = 0
  for i in range(1, n + 1):
    if check[i] == 0 and ans[i] != 10e9 and nextidx[1] > ans[i]:
      cnt = 1
      nextidx = [i, ans[i]]
  if cnt == 0:
    break
for i in range(1, 1 + n):
  if ans[i] == 10e9:
    print("INF")
  else:
    print(ans[i])
