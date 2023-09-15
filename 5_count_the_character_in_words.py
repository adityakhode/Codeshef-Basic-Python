T= int(input())

for i in range(0,T):
    s = input()
    count=0
    s=s.split("@",1)[1]
    for x in [len(x) for x in s.split()]: 
        print(x, end='')
        count=count+1
        if(count!=len(s.split())):
            print(",", end='')
    print('')
