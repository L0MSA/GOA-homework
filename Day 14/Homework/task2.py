int_list = [1, 2, 3, 4, 5]
last_element = int_list.pop()
print("Last element:", last_element)
print("Updated list:", int_list)

str_list = ["apple", "banana", "cherry"]
first_element = str_list.pop(0)
print("First element:", first_element)
print("Updated list:", str_list)

char_list = ['a', 'b', 'c', 'd', 'e']
element_at_index_2 = char_list.pop(2)
print("Element at index 2:", element_at_index_2)
print("Updated list:", char_list)

tuple_list = [(1, 2), (3, 4), (5, 6)]
last_tuple = tuple_list.pop()
print("Last tuple:", last_tuple)
print("Updated list:", tuple_list)

empty_list = []
try:
    element = empty_list.pop()
except IndexError as e:
    print("Error:", e)
