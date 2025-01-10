def sum_of_series(n):
    # return n*4 + n*30 + n*200 + n*1000
    return sum(int(str(n) * i) for i in range(1, 5))

print(sum_of_series(7)) 