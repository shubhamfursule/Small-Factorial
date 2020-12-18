b=[]
for T in range(0,int(input())):
    integer = int(input())
 
    a=1
    while integer!=0:
        a*=integer
        integer-=1
    b.append(a)
for j in range(len(b)):   
    print(b[j])