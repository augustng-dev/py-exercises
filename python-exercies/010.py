def binary_divisible_by_5(s):
    return ",".join([b for b in s.split(",") if int(b, 2) % 5 == 0]) 

print(binary_divisible_by_5('1101,1010,1111,1001'))