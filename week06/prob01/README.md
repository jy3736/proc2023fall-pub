## Problem Statement: Find the First and Last Occurrence

Write a Python function that takes a string as input and finds the index locations of the first and last appearance of a specific character. If the character occurs only once, then return its index. If the character does not occur in the string, return None.

Your task is to complete the `findCh` function to solve this problem.

*Your task is to implement the following function:*
```python
def findCh(istr, ch):
    # write your code here
    
# Example usage:
def example1():
    result = findCh("programming is fun and challenging", "g")
    print(result)
    result = findCh("programming is fun and challenging", "x")
    print(result)
    result = findCh("programming is fun and challenging", "s")
    print(result)

if __name__ == "__main__":
    example1()
```

*Testing in the Command Prompt:*
```shell
[prob01]$ python main.py 
3 33
None
13
```

*Testing with testing script:*
```shell
[prob01]$ python testing.pyc 
"programming is fun and challenging", 'g'
"programming is fun and challenging", 'x'
"programming is fun and challenging", 's'
"hello world", 'o'
"abracadabra", 'a'
"racecar", 'r'
"x", 'x'
"programming is fun and challenging", 'z'
"hello world", 'x'
"hello", 'l'
"mississippi", 'i'
"", 'x'
"programming is fun and challenging", 'f'
"programming is fun and challenging", 'u'
"abracadabra", 'c'
"racecar", 'c'
"x", 'y'
"programming is fun and challenging", 'p'
"hello world", 'h'
"hello", 'o'
"mississippi", 's'
"programming is fun and challenging", 'n'
"programming is fun and challenging", 'm'
"abracadabra", 'b'
"racecar", 'e'
"x", 'z'
"programming is fun and challenging", 't'
"hello world", 'w'
"hello", 'e'
"mississippi", 'm'
"programming is fun and challenging", 'c'
"programming is fun and challenging", 'd'
"abracadabra", 'd'
"racecar", 'a'
"x", 'a'
"programming is fun and challenging", 'v'
"hello world", 'r'
"hello", 'h'
"mississippi", 'p'
"programming is fun and challenging", 'k'
"programming is fun and challenging", 'q'
"abracadabra", 'r'
"racecar", 'l'
"x", 'b'
"programming is fun and challenging", 'y'
"hello world", 'g'
"hello", 'i'
"mississippi", 'x'
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

