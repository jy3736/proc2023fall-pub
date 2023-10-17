## Sorting a Specific Range of Integers in a String

Create a function named mysort(dat, start, end) to sort a specific range of integers within a string without altering the original string. The input parameters for this function are:

- `dat`: The string contains integers arranged in a random order.
- `start`: The index at which you want to begin sorting (inclusive).
- `end`: The index at which you want to stop sorting (exclusive).

The function's objective is to sort the integers within the dat string, including those starting from the start index up to, but not including, the integer at the end index. It should return a new string containing the sorted integers from the specified range, while preserving the original string's content.

The function should return the original string in the following cases:
- When `start` is greater than or equal to `end`.
- When `start` is less than 0.
- When `end` is greater than the length of the string.

*Your task is to implement the following function:*
```python
#!/usr/bin/env python3

def mysort(dat, start, end):
    pass
    # write your code here

#---------------------------------------------------------------------
# you can modify the following to test your code more thoroughly
#---------------------------------------------------------------------
data = ['18 64 54 4 36 55 28 10 82 94 59 78 88 18 37 39 75', 
        '34 21 83 94 20 95 7 73 95 17 100 16 56 46 33 66 31 31 100 63', 
        '43 41 97 76 15 42 18 67 9 30 44 13 5 10 4 90 53 19 44 17 36 35', 
        '77 8 54 32 37 7 60 0', 
        '7 13 70 60 12 32 71 38 68 18 37 98 38 44 31 87 44 13 89', 
        '51 78 49 51 35 99 54 83 43 100 58 25 61 85 43 33 11 12 18 8 100 12 44 84', 
        '53 50 44 73 18 56 16 21 29 62 15 78 10 82 55 7 6 19 10 21 15', 
        '53 33 49 91 32 22 84 45 31 79 22 44 93 19', 
        '32 44 9 37 81 5 95 24 49 55 46 18 13 15 31 65 78 39 38 42 1 54 68 80 94', 
        '100 44 40 92 29 99 17 2 27 96 23 26 48 65 77 23 17 17 83'
        ]

def main():
    global data
    for test_case in data:
        result = mysort(test_case,5,15);
        print(result)
        
if __name__ == '__main__':
    main()
```

*Testing in the Command Prompt:*
```shell
[prob05]$ python main.py 
18 64 54 4 36 10 18 28 37 55 59 78 82 88 94 39 75
34 21 83 94 20 7 16 17 33 46 56 73 95 95 100 66 31 31 100 63
43 41 97 76 15 4 5 9 10 13 18 30 42 44 67 90 53 19 44 17 36 35
77 8 54 32 37 7 60 0
7 13 70 60 12 18 31 32 37 38 38 44 68 71 98 87 44 13 89
51 78 49 51 35 25 43 43 54 58 61 83 85 99 100 33 11 12 18 8 100 12 44 84
53 50 44 73 18 10 15 16 21 29 55 56 62 78 82 7 6 19 10 21 15
53 33 49 91 32 22 84 45 31 79 22 44 93 19
32 44 9 37 81 5 13 15 18 24 31 46 49 55 95 65 78 39 38 42 1 54 68 80 94
100 44 40 92 29 2 17 23 26 27 48 65 77 96 99 23 17 17 83
```

*Testing with testing script:*
```shell
[prob05]$ python testing.pyc
"31 39 42 74 96 37 3 79 38 85 20 68 56 63 21 80 69" 1 21
"42 59 34 87 29 12 59 41 43 54 23 76 71 82 7 28 57 98 5 81" 0 11
"64 63 63 38 95 93 53 36 28 75 23 45 16 45 37 14 45 67 11 31 47 25 4 84" 0 24
"35 7 22 16 40 58" 7 25
...
... omitted for brevity
... 
"36 5 83 39 24 25 99 67 77" 8 8
"84 93 34 36 49 88 89 59 58 98 13 24 27" 0 17
"53 17 32 95 45 55 98 80 68 13" 10 5
"91 42 12 4 63 54 93 62 60 54 1 19 97 21 2 32 97 72 74 28 5 84 73 16" 0 29
"11 46 11 83 52 64 87 17 35" 10 6
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
```

