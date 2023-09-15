# cook your dish here
'''
This script is code stub for CodeChef problem code DIST1_PY
Filename:      DIST1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

 
# Import any required module/s
#from math import sqrt

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):
    Distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(Distance,2)





# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the x1, y1, x2 and y2 values
    for i in range(test_cases):
        x1, y1, x2, y2 = map(int, input().split())
        distance = compute_distance(x1, y1, x2, y2)
        print(distance)
    
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance

