def unique_sorted_words(s):
    return " ".join(sorted(set(i for i in s.split(" "))))

print(unique_sorted_words('dog cat apple cat banana dog'))