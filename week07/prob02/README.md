## Identifying Consecutive Number Pairs with Matching Signs, Avoiding Overlaps

To make the task clearer, your goal is to examine a list of numbers and identify adjacent pairs of elements that share the same sign. If no such pairs are found, the output should be an empty list. You should create a function called `sign_pairs` that accepts a string of numbers as input and produces a list of lists, each containing pairs of adjacent numbers with matching signs. Ensure that these pairs `do not overlap`.

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
[prob02]$ python main.py 
[[3, 4], [6, 7]]
[]
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
[]
[]
[]
[[-1, -2], [-3, -4], [-5, -6], [-7, -8], [-9, -10]]
```

*Testing with testing script:*
```shell
[prob01]$ python testing.py
[prob02]$ python testing.py
"1 -2 3 4 -5 6 7 8 -9 10"
"1 -2 3 -5 6 -7 8 -9 10"
"1 2 3 4 5 6 7 8 9 10"
"1 -2 3 -4 5 -6 7 -8 9 -10"
...
... omitted for brevity
...
"0 1 0 1 0 2 0 2 0 3 0 3 0 4 0 4 0 5 0 5 0 5 0 0 0"
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

