## Problem Statement: Capitalize Every Word in a String

You are provided with a string, and your task is to capitalize the initial letter of each word within the string.

*Your task is to implement the following function:*
```python
def capEachWord(istr):
    # write your code here

data = [
    "hello world",
    "my name is bob",
    "i like to eat food",
    "i like to play games",
    "i like to code",
    "i like to sleep",
    "i like to watch tv",
    "i like to watch movies",
]

def example1():
    global datas
    for d in data:
        ostr = capEachWord(d)
        print(ostr)

if __name__ == "__main__":
    example1()
```

*Testing in the Command Prompt:*
```shell
[prob03]$ python main.py 
Hello World
My Name Is Bob
I Like To Eat Food
I Like To Play Games
I Like To Code
I Like To Sleep
I Like To Watch Tv
I Like To Watch Movies
```

*Testing with testing script:*
```shell
[prob03]$ python testing.pyc
"good morning everyone"
"the quick brown fox"
"jumped over the lazy dog"
...
... (truncated for brevity)
...
"gratitude brings happiness"
"count your blessings"
"take time to meditate"
"find inner peace"
"random acts of kindness"
"spread positivity"
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

