'''lis = ['1', '-4', '3', '-6', '7']
res = [eval(i) for i in lis]
print("Modified list is: ", res)'''

'''for i in range(0, len(test_list)):
    test_list[i] = int(test_list[i])'''

T=int(input())

for i in range(T):
     L=int(input())#length 

     str1 = str(input())
     values=[int(x) for x in str1.split()]
    
     reverse_list=values[::-1]
     print(' '.join(map(str,reverse_list)))
    
     L1=[x+3 for x in values[3::3]]
     print(' '.join(map(str,L1)))
     
     L2=[x-7 for x in values[5::5]]
     print(' '.join(map(str,L2)))
     
     sum1=sum(values[3:8])
     print(sum1)

    

        
    
        
    
