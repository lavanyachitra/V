z=input()
flag=0
for j in z:
    if(j.isdigit()):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("Yes")
else:
    print("No")
