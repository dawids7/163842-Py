20.
def access_index(lst):
    """
    Access the index of each element in a list.

    :param lst: Input list
    """
    for index, value in enumerate(lst):
        print(f"Index: {index}, Value: {value}")

my_list = ['apple', 'banana', 'orange', 'grape']
access_index(my_list)

21.
def list_to_string(char_list):
    """
    Convert a list of characters into a string.

    :param char_list: List of characters
    :return: String
    """
    string = ''.join(char_list)
    return string

characters = ['n', 'i', 'e', ' ', 'm', 'a', ' ', 't', 'o', ' ', 'j', 'a', 'k', ' ', 'm', 'a', 'm', 'a']
result = list_to_string(characters)
print("Result:", result)

22.
def find_index(item, my_list):
    """
    Find the index of an item in a specified list.

    :param item: Item to find the index of
    :param my_list: Specified list
    :return: Index of the item in the list, or -1 if not found
    """
    try:
        index = my_list.index(item)
        return index
    except ValueError:
        return -1

my_list = ['apple', 'banana', 'cherry', 'apple', 'orange']
item_to_find = 'banana'
index = find_index(item_to_find, my_list)
if index != -1:
    print(f"The index of '{item_to_find}' in the list is: {index}")
else:
    print(f"'{item_to_find}' not found in the list.")

23.
def flatten_list(lst):
    """
    Flatten a shallow list.

    :param lst: List to flatten
    :return: Flattened list
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = flatten_list(nested_list)
print("Original nested list:", nested_list)
print("Flattened list:", flat_list)

24.
def append_lists(list1, list2):
    """
    Append list2 to list1 using the + operator.

    :param list1: First list
    :param list2: Second list to append
    :return: Combined list
    """
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = append_lists(list1, list2)
print("Combined list:", combined_list)

25.
import random

def select_random_item(input_list):
    """
    Select a random item from the given list.

    :param input_list: Input list
    :return: Randomly selected item
    """
    return random.choice(input_list)

my_list = [1, 2, 3, 4, 5]
random_item = select_random_item(my_list)
print("Randomly selected item:", random_item)

26.
def are_circularly_identical(list1, list2):
    circular_list = list1 + list1
    # Check if list2 is a substring of the circular list
    if len(list1) != len(list2):
        return False
    return ''.join(map(str, list2)) in ''.join(map(str, circular_list))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 1, 2, 3]
list3 = [3, 1, 2, 4, 5]
print("Are list1 and list2 circularly identical?", are_circularly_identical(list1, list2))
print("Are list1 and list3 circularly identical?", are_circularly_identical(list1, list3))

27.
def second_smallest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements"
    
    sorted_numbers = sorted(numbers)
    
    return sorted_numbers[1]

numbers = [5, 2, 8, 3, 1, 9, 4]
print("Second smallest number:", second_smallest(numbers))

28.
def second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements"
    
    sorted_numbers = sorted(numbers, reverse=True)
    
    return sorted_numbers[1]

numbers = [5, 2, 8, 3, 1, 9, 4]
print("Second largest number:", second_largest(numbers))

29.
def unique_values(lst):
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list

lst = [1, 2, 3, 3, 4, 5, 5, 6]
print("Original list:", lst)
print("Unique values:", unique_values(lst))

30.
from collections import Counter

def element_frequency(lst):
    frequency = Counter(lst)
    return frequency

lst = [1, 2, 3, 3, 4, 5, 5, 6]
print("Original list:", lst)
print("Frequency of elements:", element_frequency(lst))

31.
def count_elements_in_range(lst, start, end):
    count = sum(1 for x in lst if start <= x <= end)
    return count

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
start_range = 30
end_range = 70
print("Original list:", lst)
print("Count of elements within range [{}, {}]: {}".format(start_range, end_range, count_elements_in_range(lst, start_range, end_range)))

32.
def contains_sublist(main_list, sublist):
    for i in range(len(main_list)):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6]
sublist1 = [2, 3, 4]
sublist2 = [6, 7, 8]

print(contains_sublist(main_list, sublist1)) 
print(contains_sublist(main_list, sublist2)) 

33.
def generate_sublists(lst):
    sublists = []
    n = len(lst)
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublists.append(lst[start:end])
    return sublists

original_list = [1, 2, 3]
print(generate_sublists(original_list))

34.
def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    for i in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[i]:
            primes.append(i)

    return primes

limit = int(input("Enter the limit to compute prime numbers: "))
print("Prime numbers up to", limit, "are:", sieve_of_eratosthenes(limit))

35.
def concatenate_with_range(lst, n):
    result = []
    for i in range(1, n + 1):
        for item in lst:
            result.append(item + str(i))
    return result

sample_list = ['a', 'b']
n = 5

print("Sample list:", sample_list)
print("n =", n)
print("Sample Output:", concatenate_with_range(sample_list, n))

36.
identification = input("Enter an identification number or string: ")

print("Identification:", identification)

37.
def find_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_items = set1.intersection(set2)
    
    return list(common_items)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_items = find_common_items(list1, list2)
print("Common items:", common_items)

38.
def change_position(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

sample_list = [0, 1, 2, 3, 4, 5]
result = change_position(sample_list)
print("Result:", result)

39.
def convert_to_single_integer(lst):
    str_list = [str(num) for num in lst]
    concatenated_string = ''.join(str_list)
    result = int(concatenated_string)
    return result

sample_list = [11, 33, 50]
result = convert_to_single_integer(sample_list)
print("Result:", result)

40.
def split_list_by_first_character(word_list):
    result_dict = {}
    for word in word_list:
        first_char = word[0]
        if first_char in result_dict:
            result_dict[first_char].append(word)
        else:
            result_dict[first_char] = [word]
    return result_dict

sample_list = ['apple', 'banana', 'orange', 'ant', 'cat', 'dog']
result = split_list_by_first_character(sample_list)
print("Result:", result)



