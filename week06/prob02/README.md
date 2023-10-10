## Problem Statement: The third occurrence

Given a string that may or may not contain the letter of interest, please return the index location of the third occurrence of the letter 'f.' If the string contains fewer than three occurrences of the letter 'f,' please return -1. If the string does not contain the letter 'f' at all, please return -2.

*Your task is to implement the following function:*
```python
def find3rd(istr, ch):
    # write your code here

data = [
    ("hello world, welcome to programming!", "o"),
    ("The quick brown fox jumps over the lazy dog", "x"),
    ("OpenAI's GPT-3 is an amazing language model", "a"),
    ("12345 67890 12345 67890", "5"),
    ("programming is fun and challenging", "d"),
]

def example1():
    global data
    for d in data:
        result = find3rd(d[0], d[1])
        print(result)

if __name__ == "__main__":
    example1()
```

*Testing in the Command Prompt:*
```shell
[prob02]$ python main.py 
17
-1
23
-1
-1
```

*Testing with testing script:*
```shell
[prob02]$ python testing.pyc
"hello world, welcome to programming!", 'o'
"The quick brown fox jumps over the lazy dog", 'x'
"OpenAI's GPT-3 is an amazing language model", 'a'
"12345 67890 12345 67890", '5'
"This is a test string with spaces", 's'
"Python is a versatile programming language", 'v'
"aaaaa", 'a'
"abcdefg", 'c'
"programming is fun and challenging", 'g'
"programming is fun and challenging", 'm'
"programming is fun and challenging", 'z'
"programming is fun and challenging", 'n'
"programming is fun and challenging", 'i'
"programming is fun and challenging", 'u'
"programming is fun and challenging", 'f'
"programming is fun and challenging", 'a'
"programming is fun and challenging", 'p'
"abcdefg", 'f'
"The quick brown fox jumps over the lazy dog", 'q'
"OpenAI's GPT-3 is an amazing language model", 'm'
"programming is fun and challenging", 'l'
"programming is fun and challenging", 'e'
"programming is fun and challenging", 'r'
"programming is fun and challenging", 't'
"programming is fun and challenging", 'h'
"programming is fun and challenging", 'c'
"programming is fun and challenging", 'k'
"programming is fun and challenging", 'y'
"programming is fun and challenging", 'd'
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

