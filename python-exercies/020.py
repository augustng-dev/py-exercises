import random

def generate_random_numbers():
    return random.sample(range(150, 251), 5)

# Example usage
print(generate_random_numbers())