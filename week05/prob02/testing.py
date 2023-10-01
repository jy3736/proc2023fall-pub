import unittest
import subprocess
import random
import sys
import os
import py_compile

target = "main.py"

class TestDivisibilityChecker(unittest.TestCase):

    def test_random_inputs(self):
        global target
            
        for _ in range(100):
            # Generate a random input with space-separated integers
            a = random.randint(0,30)
            n = random.randint(0,30)
            expected_output = a**n
            print(f"{a:3} {n:3}")
            input_numbers = f"{a}\n{n}\n"
            # Run the script with the generated input using subprocess
            process = subprocess.Popen(['python', target], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input=input_numbers)
            
            # Calculate the expected result based on the input
            actual_output = int(stdout.strip())

            # Assert that the actual output matches the expected output
            self.assertEqual(actual_output, expected_output)

def pre_test():
    global target
    if not os.path.exists(target):
        print(f"Error: File '{target}' not found.")
        sys.exit(2)

def validate():
    global target
    forbidden_tokens = ['for', 'while', '**', 'import', 'math', 'math.pow', 'pow(']
    with open('main.py', 'r') as file:
        script_content = file.read()
    for token in forbidden_tokens:
        if token in script_content:
            print(f"Error: Forbidden token '{token}' found in script.")
            sys.exit(4)

if __name__ == '__main__':
    pre_test()
    validate()
    unittest.main()
