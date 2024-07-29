def length_and_insert(lst):
    lengths = [len(item) for item in lst]
    return lengths

strings = ["apple", "banana", "cherry"]
lengths = length_and_insert(strings)
print("Lengths of strings:", lengths)
