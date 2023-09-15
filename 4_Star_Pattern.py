t=int(input())
for r in range(t):
    n=int(input())
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            if j%5==0:
                print("#",endl="")
            else:
                print("*",end="")
        print()