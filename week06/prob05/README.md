## Problem Statement: Processing Tags to Render Custom-Built Text

In this problem, you will need to write a text pre-processing function that takes a string of text and returns a string of text with the following modifications:

1. All text between `<c>` and `</c>` tags should be converted to capital letters.
2. All text between `<r>` and `</r>` tags should be reversed.


*Your task is to implement the following function:*
```python
# import required modules

def procTags(istr):
    # write your code here

# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

data = [
    "<c>programming</c>123456789<r>987654321</r>python",
    "<c>university</c>9876543<r>7654321</r>education",
    "<c>engineering</c>12345<r>54321</r>innovation",
    "<c>technology</c>1234<r>4321</r>advancement",
    "<c>electronic</c>123<r>321</r>innovations",
]

def main():
    global data
    for i, td in enumerate(data, start=1):
        print(f"{i}: {td}")
        result = procTags(td)
        print(result)

if __name__ == "__main__":
    main()
```

*Testing in the Command Prompt:*
```shell
[prob05]$ python main.py 
1: <c>programming</c>123456789<r>987654321</r>python
PROGRAMMING123456789123456789python
2: <c>university</c>9876543<r>7654321</r>education
UNIVERSITY98765431234567education
3: <c>engineering</c>12345<r>54321</r>innovation
ENGINEERING1234512345innovation
4: <c>technology</c>1234<r>4321</r>advancement
TECHNOLOGY12341234advancement
5: <c>electronic</c>123<r>321</r>innovations
ELECTRONIC123123innovations
```

*Testing with testing script:*
```shell
[prob05]$ python testing.py 
 1: "<c>programming</c>123456789<r>987654321</r>python"
 2: "<c>university</c>9876543<r>7654321</r>education"
 3: "<c>engineering</c>12345<r>54321</r>innovation"
...
... omitted for brevity
...
26: "<c>automation</c>12<r>21</r>efficiency"
27: "<c>experiments</c>123456789<r>987654321</r>results"
28: "<c>networking</c>9876543<r>7654321</r>connectivity"
29: "<c>programming</c>12345<r>54321</r>coding"
30: "<c>verification</c>1234<r>4321</r>testing"
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
