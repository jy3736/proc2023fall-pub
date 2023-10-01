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
            p1 = [random.randint(-10, 10) for _ in range(3)]
            p2 = [random.randint(-10, 10) for _ in range(3)]
            expected_output = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5
            expected_output = round(expected_output, 2)
            print(f"{str(p1):15} {str(p2):15}")
            p1s = " ".join([str(x) for x in p1])
            p2s = " ".join([str(x) for x in p2])
            input_numbers = f"{p1s}\n{p2s}\n"
            # Run the script with the generated input using subprocess
            process = subprocess.Popen(['python', target], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input=input_numbers)
            
            # Calculate the expected result based on the input
            actual_output = round(float(stdout.strip()), 2)

            # Assert that the actual output matches the expected output
            self.assertEqual(actual_output, expected_output)

def pre_test():
    global target
    if not os.path.exists(target):
        sys.exit(2)

if __name__ == '__main__':
    pre_test()
    unittest.main()
