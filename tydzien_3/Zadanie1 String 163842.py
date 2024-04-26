1. 
user_input = input("Enter a string: ")

length = len(user_input)

print("The length of the string is:", length)

2.
def count_characters(string):
    char_frequency = {}

    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

sample_string = 'Wczoraj zepsul mi sie samochod, to chyba amortyzator'
result = count_characters(sample_string)
print(result)

3.
def first_and_last_two(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]

sample_strings = ['Alicja', 'Ala', 'A']
for string in sample_strings:
    result = first_and_last_two(string)
    print(f"Probka: '{string}' => Wynik: '{result}'")

4.
def change_char(string):
    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')
    return modified_string

sample_string = 'restarcik'
result = change_char(sample_string)
print("Probka:", sample_string)
print("Wynik:", result)

5.
def swap_first_two(string1, string2):
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]
    return swapped_string1 + ' ' + swapped_string2

string1 = '123'
string2 = '456'
result = swap_first_two(string1, string2)
print("Probka:", string1, ",", string2)
print("Wynik:", result)

6.
def add_ing_or_ly(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'

sample_string1 = 'abc'
sample_string2 = 'string'
result1 = add_ing_or_ly(sample_string1)
result2 = add_ing_or_ly(sample_string2)
print("Probka:", sample_string1)
print("Wynik:", result1)
print("Probka:", sample_string2)
print("Wynik:", result2)

7.
def replace_not_poor(string):
    index_not = string.find('not')
    index_poor = string.find('poor')

    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        return string[:index_not] + 'good' + string[index_poor + 4:]
    else:
        return string


probka_1 = 'The lyrics is not that poor!'
probka_2 = 'The lyrics is poor!'
wynik_1 = replace_not_poor(probka_1)
wynik_2 = replace_not_poor(probka_2)
print("Probka 1:", probka_1)
print("Wynik 1:", wynik_1)
print("Probka 2:", probka_2)
print("Wynik 2:", wynik_2)

8.
def find_longest_word(words_list):
    if not words_list:
        return None, 0
    
    longest_word = words_list[0]
    longest_length = len(longest_word)

    for word in words_list:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)

    return longest_word, longest_length

words_list = ["Python", "programming", "Exercises", "longest", "word"]
longest_word, length = find_longest_word(words_list)
print("Najdluzszy wyraz:", longest_word)
print("Dlugosc najdluzszego wyrazu:", length)

9.
def remove_nth_character(string, n):
    if not string:
        return "String is empty"
    
    if n < 0 or n >= len(string):
        return "Index out of range"
    
    return string[:n] + string[n+1:]

string = "Python"
n = 3
result = remove_nth_character(string, n)
print("String after removing the", n, "th character:", result)

10.
def exchange_first_last_char(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]

input_string = "analfabetyzm"
result = exchange_first_last_char(input_string)
print("Original string:", input_string)
print("String with exchanged first and last characters:", result)

11.
def remove_odd_index_chars(s):
    return s[::2]

original_string = "abcdefg"
result = remove_odd_index_chars(original_string)
print("Original string:", original_string)
print("String with odd index characters removed:", result)

12.
def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = "This is a test sentence. This sentence is just a test."
word_occurrences = count_word_occurrences(sentence)
print("Occurrences of each word in the given sentence:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")

13.
user_input = input("Podaj tekst: ")

print("Tekst w duzych literach:", user_input.upper())

print("Tekst w malych literach:", user_input.lower())

14.
words_input = input("Podaj ciag slow oddzielonych przecinkami: ")

words_list = words_input.split(',')

unique_words = set(word.strip() for word in words_list)

sorted_unique_words = sorted(unique_words)
print("Posortowane unikalne slowa:", ', '.join(sorted_unique_words))

15.
def add_tags(tag, word):
    """
    Creates an HTML string with tags around the given word or phrase.

    :param tag: HTML tag to add
    :param word: Word or phrase
    :return: HTML string with tags
    """
    return f"<{tag}>{word}</{tag}>"

print(add_tags('i', 'Python'))  # Output: <i>Python</i>
print(add_tags('b', 'Python Tutorial'))  # Output: <b>Python Tutorial</b>

16.
def insert_string_middle(s, word):
    """
    Inserts a string in the middle of another string.

    :param s: Original string
    :param word: String to be inserted
    :return: Resulting string with the word inserted in the middle
    """
    middle_index = len(s) // 2
    return s[:middle_index] + word + s[middle_index:]

print(insert_string_middle('[[]]', 'Python'))  # Output: [[Python]]<<>>
print(insert_string_middle('{{}}', 'PHP'))  # Output: {{PHP}}

17.
def insert_end(s):
    """
    Returns a string made of 4 copies of the last two characters of a specified string.

    :param s: Input string
    :return: Resulting string
    """
    if len(s) < 2:
        return "String length must be at least 2"
    else:
        last_two_chars = s[-2:]
        return last_two_chars * 4

print(insert_end('Python'))  # Output: onononon
print(insert_end('Exercises'))  # Output: eseseses

18.
def first_three(s):
    """
    Returns a string made of the first three characters of a specified string.
    If the length of the string is less than 3, returns the original string.

    :param s: Input string
    :return: Resulting string
    """
    if len(s) < 3:
        return s
    else:
        return s[:3]

print(first_three('ipy'))  # Output: ipy
print(first_three('python'))  # Output: pyt

19.
def last_part_of_string(s, char):
    """
    Returns the last part of a string before a specified character.

    :param s: Input string
    :param char: Specified character
    :return: Last part of the string before the specified character
    """
    return s.rsplit(char, 1)[0]

string1 = "https://www.w3resource.com/python-exercises"
char1 = "-"
print(last_part_of_string(string1, char1)) 

string2 = "https://www.w3resource.com/python"
char2 = "/"
print(last_part_of_string(string2, char2))  

20.
def reverse_string_if_multiple_of_four(s):
    """
    Reverse a string if its length is a multiple of 4.

    :param s: Input string
    :return: Reversed string if its length is a multiple of 4, otherwise returns the original string
    """
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s

string1 = "python"
print(reverse_string_if_multiple_of_four(string1)) 

string2 = "abcd"
print(reverse_string_if_multiple_of_four(string2)) 


