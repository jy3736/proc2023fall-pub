## Finding Adjacent Number Pair(s) with the Same Sign

In a provided list of numbers, your objective is to identify and print adjacent pairs of elements that have the same sign. If there are no such pairs, the output should be empty list. You have to implement the function `sign_pairs` that takes a string of numbers as input and returns a list of lists of pairs of adjacent numbers with the same sign.

*Your task is to implement the following function:*
```python
#!/usr/bin/env python3

def sign_pairs(numbers):
    #----------------------
    # write your code here
    #----------------------

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
```

*Testing in the Command Prompt:*
```shell
[prob01]$ python main.py 
[[3, 4], [6, 7], [7, 8]]
[]
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]
[]
[]
[]
[[-1, -2], [-2, -3], [-3, -4], [-4, -5], [-5, -6], [-6, -7], [-7, -8], [-8, -9], [-9, -10]]
```

*Testing with testing script:*
```shell
[prob01]$ python testing.py
"1 -2 3 4 -5 6 7 8 -9 10"
"1 -2 3 -5 6 -7 8 -9 10"
"1 2 3 4 5 6 7 8 9 10"
...
... omitted for brevity
...
"1 0 1 0 2 0 2 0 3 0 3 0 4 0 4 0 5 0 5 0 5 0 0 0 0"
"1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 8 8 8 9"
"1 -1 1 2 -2 2 3 -3 3 4 -4 4 5 -5 5 6 -6 6 7 -7 7 8 -8 8"
"0 1 0 1 0 2 0 2 0 3 0 3 0 4 0 4 0 5 0 5 0 5 0 0 0 0"
"1 0 1 0 2 0 2 0 3 0 3 0 4 0 4 0 5 0 5 0 5 0 0 0 0 0"
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

