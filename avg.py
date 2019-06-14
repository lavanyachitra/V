xz=int(input())
nl=list(map(int,input().split()))
avg=0
for i in range(len(nl)):
    avg+=nl[i]
print(avg//xz)
