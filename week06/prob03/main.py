#!/usr/bin/env python3

def capEachWord(istr):
    pass
    # Write your code here!

# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

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


def main():
    global datas
    for d in data:
        ostr = capEachWord(d)
        print(ostr)

if __name__ == "__main__":
    main()