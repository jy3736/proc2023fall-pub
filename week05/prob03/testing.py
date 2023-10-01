import unittest
import subprocess
import random
import sys
import os
import re
import py_compile

target = "main.py"

def expected(R, C):
    s = ""
    for i in range(1, R + 1):
        for j in range(1, C):
            num = (j - 1) * R + i
            s += f"{num} "
        else:
            s += f"{num+R}\n"
    return s

class TestDivisibilityChecker(unittest.TestCase):

    def test_random_inputs(self):
        global target
            
        for _ in range(100):
            r = random.randint(2,15)
            c = random.randint(2,15)
            expected_output = expected(r, c)
            expected_output = re.sub(r'\s+', ' ', expected_output.strip())
            expected_output = re.sub(r' (?=\n)', '\n', expected_output)
            print(f"{r} {c}")
            input_numbers = f"{r} {c}\n"
            # Run the script with the generated input using subprocess
            process = subprocess.Popen(['python', target], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input=input_numbers)
            
            # Calculate the expected result based on the input
            actual_output = re.sub(r'\s+', ' ', stdout.strip())
            actual_output = re.sub(r' (?=\n)', '\n', actual_output)
            
            # Assert that the actual output matches the expected output
            self.assertEqual(actual_output, expected_output)

def pre_test():
    global target
    if not os.path.exists(target):
        print(f"Error: File '{target}' not found.")
        sys.exit(2)

def rm_comments(script):
    pattern = r"(#.*?$|'''(.*?)'''|\"\"\"(.*?)\"\"\")"
    script_without_comments = re.sub(pattern, '', script, flags=re.MULTILINE | re.DOTALL)
    return script_without_comments

def validate():
    global target
    musthave = ['__name__', '__main__', 'def main(']
    with open('main.py', 'r') as file:
        script_content = file.read()
    script_content = rm_comments(script_content)
    for token in musthave:
        if token not in script_content:
            print(f"Error: File '{target}' does not contain '{token}'")
            sys.exit(4)

if __name__ == '__main__':
    pre_test()
    validate()
    unittest.main()
