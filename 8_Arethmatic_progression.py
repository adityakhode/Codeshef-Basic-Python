def generate_AP(a, d, n):
    current_value = a
    AP=[]
    for i in range(0, n):
        AP.append(current_value)
        current_value = current_value + d
    return AP

T = int(input())
for u in range(0,T):
    a, d, n = map(int, input().split())
    fAP=generate_AP(a,d,n)
    for i in range(0,n):
        print(fAP[i], end=' ')
    print('')
    
    sAP=list(map(lambda x:x*x, fAP))
    for i in range(0,n):
        print(sAP[i], end=' ')
    print('')
    
    sum=0
    for z in range(0,n):
        sum+=sAP[z]
    print(sum)
