# cook your dish here
'''
This script is code stub for CodeChef problem code D2BIN1_PY
Filename:      D2BIN1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Function to calculate Euclidean distance between two points
def dec_to_binary(n):
    if n == 0:
        return "00000000"
    elif n == 1:
        return "00000001"
    else:
        bin_num = dec_to_binary(n // 2)
        bin_num = bin_num + str(n % 2)
        bin_num = bin_num[-8:].rjust(8, '0')
    # Complete this function to return binary equivalent output of the given number 'n' in 8-bit format

    return bin_num


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the n value
    for case in range(1,test_cases+1):
        # take the n input values
        n = int(input())

        # print (n)

        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        bin_num = dec_to_binary(n)
        print(bin_num)