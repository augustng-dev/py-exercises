def generate_square_dict(n):
    return {i: i**2 for i in range(1, n+1)}

print(generate_square_dict(8))