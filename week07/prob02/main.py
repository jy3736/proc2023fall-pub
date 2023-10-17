#!/usr/bin/env python3

def sign_pairs(numbers):
    pass
    #--------------------------
    # write your code here
    #--------------------------

#---------------------------------------------------------------------
# you can modify the following to test your code more thoroughly
#---------------------------------------------------------------------
data = [
    "1 -2 3 4 -5 6 7 8 -9 10",
    "1 -2 3 -5 6 -7 8 -9 10",
    "1 2 3 4 5 6 7 8 9 10",
    "1 -2 3 -4 5 -6 7 -8 9 -10",
    "1 -2 3 -4 5 -6 7 -8 9 -10 11",
    "1 -2 3 -4 5 -6 7 -8 9 -10 11 -12",
    "-1 -2 -3 -4 -5 -6 -7 -8 -9 -10",
 ]

        
def main():
    global data
    for test_case in data:
        result = sign_pairs(test_case)
        print(result)
        
if __name__ == '__main__':
    main()