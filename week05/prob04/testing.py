import unittest
import subprocess
import random
import sys
import os
import re
import py_compile

target = "main.py"

def variance(numbers):
    if len(numbers) < 2:
        return None
    mean = sum(numbers) / len(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / (len(numbers) - 1)
    return variance

class TestDivisibilityChecker(unittest.TestCase):

    def test_random_inputs(self):
        global target
            
        for _ in range(100):
            nums = [random.randint(1, 100) for _ in range(random.randint(5, 15))]
            expected_output = round(variance(nums), 2)
            print(nums)
            input_numbers = ' '.join([str(_) for _ in nums])
            process = subprocess.Popen(['python', target], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input=input_numbers)
            
            # Calculate the expected result based on the input
            actual_output = round(float(stdout.strip()),2)
            
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
    musthave = ['__name__', '__main__', 'def variance(']
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
