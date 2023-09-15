#testcases

T=int(input())

#palindrome_flag=1
for i in range(T):
    palindrome_flag=1
    x=str(input("Enter the string = "))
    y=len(x)
    for j in range(0 , int(len(x)/2)):
        if x[j] != x[len(x)-j-1]:
            palindrome_flag=0
            break
    if(palindrome_flag==1):
        
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


#check output 





