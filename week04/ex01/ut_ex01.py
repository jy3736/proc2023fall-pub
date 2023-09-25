import unittest
import subprocess
import random

class TestMainScript(unittest.TestCase):
    
    def test_script_output(self):
        for test_case in range(10):
            # Generate random input data
            n = random.randint(1, 10)
            input_data = str(n) + '\n'
            expected_output = 1
            for _ in range(n):
                num = random.randint(1, 100)
                input_data += str(num) + '\n'
                expected_output *=num
            expected_output = str(expected_output) 
            print('Input data:', input_data.replace('\n', ', '))
            
            # Run the script with the random input data and capture its output
            process = subprocess.Popen(
                ['python', 'main.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=input_data)
            actual_output = stdout.strip()
            
            # Check if the actual output matches the expected output
            self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
