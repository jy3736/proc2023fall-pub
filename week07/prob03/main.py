#!/usr/bin/env python3

def count_unique(numstr):
    pass
    #--------------------------
    # write your code here
    #--------------------------

#---------------------------------------------------------------------
# you can modify the following to test your code more thoroughly
#---------------------------------------------------------------------
data = [
    "1 2 3 4 5 6 7 8 9",
    "1 1 1 1 1 1 1 1",
    "1 2 1 2 1 2 1 2",
    "1 2 3 1 2 3 1 2 3",
    "1 1 1 1 2",
    "1 2 2 3 3 4",
    "1 2 3 4 5 1 2 3 4",
    "1 2 3 4 1 2 3 4 5",
    "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
]


        
def main():
    global data
    for test_case in data:
        result = count_unique(test_case)
        print(result)
        
if __name__ == '__main__':
    main()