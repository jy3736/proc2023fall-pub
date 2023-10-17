## Counting Unique Elements in Unordered Lists Without Using Sets

In this Python programming task, your objective is to create a script that can determine the count of unique elements within an unsorted list. The catch is that you should achieve this without employing Python's `set` data structure.

To clarify further, the term `unordered list` refers to a list where the items are not arranged in any specific order, and there may be repetitions of elements. The aim is to find out how many distinct elements are present in the list and calculate the count of these unique elements.

*Your task is to implement the following function:*
```python
#!/usr/bin/env python3

def count_unique(numstr):
    #----------------------
    # wwrite your code here
    #----------------------

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
```

*Testing in the Command Prompt:*
```shell
[prob03]$ python main.py 
9
1
2
3
2
4
5
5
15
```

*Testing with testing script:*
```shell
[prob03]$ python testing.py
"1 2 3 4 5 6 7 8 9"
"1 1 1 1 1 1 1 1"
"1 2 1 2 1 2 1 2"
"1 2 3 1 2 3 1 2 3"
"1 1 1 1 2"
"1 2 2 3 3 4"
"1 1 1 2 2 2 3 3 3"
"2 2 3 3 4 4 5 5 6"
...
... omitted for brevity
...
"2 2 2 2 2 2 2 2 2 2 2 2 2 2 2"
"3 3 3 3 3 3 3 3 3 3 3 3 3 3 3"
"4 4 4 4 4 4 4 4 4 4 4 4 4 4 4"
"6 6 6 6 6 6 6 6 6 6 6 6 6 6 6"
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

