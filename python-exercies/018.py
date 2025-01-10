def f(n):
    if n == 0:
        return 1
    else:
        return f(n - 1) + 100

# Example usage
print(f(5))