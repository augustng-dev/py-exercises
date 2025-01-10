def sort_words(words):
    return ','.join(sorted(words.split(',')))

print(sort_words('banana,apple,grape,orange'))