from utils import retry
import random

@retry(max_attempts=3, delay=1)
def test_func():
    print("Trying...")
    if random.random() < 0.7:
        raise Exception("Oops, fail!")
    return "Yay, success!"

print(test_func())
