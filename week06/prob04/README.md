## Problem Statement: Replace Only Odd Occurrences of `h`

Given a string, replace every occurrence of the letter 'h' with the letter 'H,' except for the even-numbered occurrences, such as 2, 4, 6, ....

*Your task is to implement the following function:*
```python
def replaceOdd(istr):
    # write your code here

# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

data = [
    "hello world",
    "hello "*10,
    "hH"*10,
    "Hello",
    "hHhHhHhH",
    "123h456h789",
    "abcdefg",
    "hhhhhhhhhhhhhhhhhhhh",
    "HhHhHhHhHhHhHhHhHh",
    "1h2h3hHHH4h5hHHH6h7h8hHHH9h"
]    

def main():
    for ss in data:
        result = replaceOdd(ss)
        print(result)

if __name__ == "__main__":
    main()
```

*Testing with testing script:*
```shell
[prob04]$ python main.py 
Hello world
Hello hello Hello hello Hello hello Hello hello Hello hello 
HHhHHHhHHHhHHHhHHHhH
Hello
HHhHHHhH
123H456h789
abcdefg
HhHhHhHhHhHhHhHhHhHh
HHHhHHHhHHHhHHHhHH
1H2h3HHHH4h5HHHH6h7H8hHHH9H
```

*Testing in the Command Prompt:*
```shell
[prob04]$ python testing.py 
"hello world"
"this is a test"
"hhh"
"hhhh"
"HHH"
...
... omitted for brevity
...
"hHhHhHhHhHhHh"
"HhHhHhH"
"HhhHhHhH"
"hHhHhHhHhHhHhHhH"
"HhHhHhHhHhHhH"
"HhHhHhHhHhHhHhH"
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

