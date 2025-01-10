def count_letters_digits(sentence):
    counts = {"LETTERS": 0, "DIGITS": 0}
    for char in sentence:
        if char.isalpha():
            counts["LETTERS"] += 1
        elif char.isdigit():
            counts["DIGITS"] += 1
    return counts

print(count_letters_digits('Data123 Science 2024'))