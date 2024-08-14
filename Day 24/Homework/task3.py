def manual_count(count_char, symbol):
    count = 0
    
    for char in count_char:
        if char == symbol:
            count += 1
            
    return count

string_to_count = "hello world"
symbol_to_count = "o"
result = manual_count(string_to_count, symbol_to_count)
print(result)
