def count_case(sentence):
    counts = {"UPPER CASE": 0, "LOWER CASE": 0}
    for char in sentence:
        if char.isupper():
            counts["UPPER CASE"] += 1
        elif char.islower():
            counts["LOWER CASE"] += 1
    return counts
    
print(count_case('Hello World!'))