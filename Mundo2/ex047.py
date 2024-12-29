# Displays all even numbers between 1 and 50, with a delay between outputs.
# Uses a for loop and checks divisibility by 2 to filter even numbers.

import time

for i in range(50):
    i += 2
    if i % 2 == 0:
        print(i)
        time.sleep(1)
    else:
        pass