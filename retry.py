@retry(max_attempts=5, delay=1)
def flaky_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Something went wrong")
    return "Success!"

print(flaky_function())
