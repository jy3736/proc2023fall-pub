#!/usr/bin/env python3

# import required libraries/modules

def procTags(istr):
    pass
    # Write your code here!

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