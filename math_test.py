# math_test.py
import time
import sys

print(" Initializing Automated Python Math Test...")
time.sleep(1)

num1 = 5
num2 = 10
expected_sum = 15

print(f"Calculating: {num1} + {num2} ...")
actual_sum = num1 + num2

if actual_sum == expected_sum:
    print(f"Addition Test Passed! Result is {actual_sum}")
    sys.exit(0)  # Exit code 0 means Success
else:
    print(f" Test Failed! Expected {expected_sum} but got {actual_sum}", file=sys.stderr)
    sys.exit(1)  # Exit code 1 means Failure
