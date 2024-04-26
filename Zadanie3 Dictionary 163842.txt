1.
sample_dict = {'apple': 20, 'banana': 10, 'orange': 30, 'grape': 15}

sorted_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

sorted_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", sorted_asc)
print("Descending order:", sorted_desc)

2.
original_dict = {'a': 1, 'b': 2, 'c': 3}

original_dict['d'] = 4

print("Updated dictionary:", original_dict)

3.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

concatenated_dict = {}

concatenated_dict.update(dict1)
concatenated_dict.update(dict2)
concatenated_dict.update(dict3)

print("Concatenated dictionary:", concatenated_dict)

4.
my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

5.
my_dict = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over keys:")
for key in my_dict:
    print(key)

print("\nIterating over values:")
for value in my_dict.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

6.
def generate_dictionary(n):
    # Use dictionary comprehension to generate the dictionary
    return {x: x*x for x in range(1, n+1)}

n = int(input("Enter a number (n): "))

result_dict = generate_dictionary(n)

print("Generated dictionary:")
print(result_dict)

7.
square_dict = {num: num ** 2 for num in range(1, 16)}

print(square_dict)

8.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)

print(dict1)

9.
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(key, ':', value)

10.
my_dict = {'a': 10, 'b': 20, 'c': 30}


total_sum = 0


for value in my_dict.values():
    total_sum += value


print("Total sum:", total_sum)

11.
my_dict = {'a': 10, 'b': 20, 'c': 30}


total_product = 1


for value in my_dict.values():
    total_product *= value


print("Total product:", total_product)

12.
my_dict = {'a': 1, 'b': 2, 'c': 3}


my_dict.pop('b')


print("Dictionary after removing 'b':", my_dict)

13.
keys = ['a', 'b', 'c']
values = [1, 2, 3]


mapped_dict = dict(zip(keys, values))


print("Mapped Dictionary:", mapped_dict)

14.
y_dict = {'banana': 3, 'apple': 2, 'orange': 1}


sorted_dict = dict(sorted(my_dict.items()))


print("Sorted Dictionary by Key:", sorted_dict)

15.
my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}


max_value = max(my_dict.values())


max_key = max(my_dict, key=my_dict.get)


min_value = min(my_dict.values())


min_key = min(my_dict, key=my_dict.get)


print("Maximum Value:", max_value)
print("Key corresponding to Maximum Value:", max_key)
print("Minimum Value:", min_value)
print("Key corresponding to Minimum Value:", min_key)

16.
class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

obj = MyClass(1, 2, 3)

obj_dict1 = vars(obj)

obj_dict2 = obj.__dict__

print("Dictionary using vars():", obj_dict1)
print("Dictionary using __dict__:", obj_dict2)

17.
def remove_duplicates(input_dict):
    unique_dict = {}
    
    for key, value in input_dict.items():
        # Check if the value is not already in the unique dictionary
        if value not in unique_dict.values():
            # If not, add it to the unique dictionary
            unique_dict[key] = value
    
    return unique_dict

input_dict = {'a': 4, 'b': 6, 'c': 3, 'd': 5, 'e': 4}
print("Original:", input_dict)

unique_dict = remove_duplicates(input_dict)
print("Dups removed:", unique_dict)

18.
def is_dict_empty(input_dict):
    return len(input_dict) == 0

empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

print("Is empty_dict empty?", is_dict_empty(empty_dict))
print("Is non_empty_dict empty?", is_dict_empty(non_empty_dict))

19.
def combine_dictionaries(d1, d2):
    combined_dict = d1.copy()  # Make a copy of the first dictionary
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = combine_dictionaries(d1, d2)
print("Combined Dictionary:", combined_dict)

20.
def distinct_values(dictionary):
    
    unique_values = set(dictionary.values())
    return unique_values


sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

distinct_vals = distinct_values(sample_dict)
print("Distinct Values:", distinct_vals)





