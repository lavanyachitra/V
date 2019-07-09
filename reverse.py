bl=int(input())
lb=list(map(int,input().split()))
v1=[]
for j in lb:
  m=bin(j)
  v1.append(m)
n=sorted(v1)
n.reverse()
for i in n:
  print(int(i,2))
