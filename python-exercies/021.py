import random

def generate_even_numbers():
    return random.sample([i for i in range(150, 251) if i % 2 == 0], 5)

# Example usage
print(generate_even_numbers())