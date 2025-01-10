import math

def calculate_q_values(d_values):
    C, H = 50, 30
    return ','.join(str(round(math.sqrt((2 * C * float(D)) / H))) for D in d_values.split(','))

print(calculate_q_values('5,50,500'))