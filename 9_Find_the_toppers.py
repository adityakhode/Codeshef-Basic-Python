t=int(input())
for test in range(t):
  n=int(input())
  l1=[]
  l2=[]
  for stud in range(n):
    name, marks=map(str, input().split())
    l1.append(name)
    l2.append(float(marks))

  m=max(l2)
  l3=[]
  for x in range(n):
    if l2[x]==m:
        
      l3.append(l1[x])
  l3.sort()
  for s in l3:
    print(s)
