'''
This script is code stub for CodeChef problem code IFFOR1_PY
Filename:      IFFOR1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    T = int(input())

for j in range(T):
    n=int(input())
    for i in range(n):
        if (i==0):
            print(3,end=" ")
        else:
            if(i!=0 and i%2==1):
                print (i**2,end=" ")
            elif(i!=0 and i%2==0):
                print(i*2,end=" ")
            else:
                i=i+3
    print()
        
