#!/usr/bin/env python3

def find3rd(istr, ch):
    pass
    # Write your code here!

# --------------------------------------------------------------------
# The following code is intended for your personal testing purposes. 
# Feel free to modify it to meet your requirements.
# --------------------------------------------------------------------

data = [
    ("hello world, welcome to programming!", "o"),
    ("The quick brown fox jumps over the lazy dog", "x"),
    ("OpenAI's GPT-3 is an amazing language model", "a"),
    ("12345 67890 12345 67890", "5"),
    ("programming is fun and challenging", "d"),
]

def main():
    global data
    for d in data:
        result = find3rd(d[0], d[1])
        print(result)

if __name__ == "__main__":
    main()