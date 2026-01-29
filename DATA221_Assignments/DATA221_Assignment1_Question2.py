# Nested Dictionaries from Strings

def Nested_Dictionaries_from_Strings(list_of_strings):
# Build the nested dictionary
    nested_dictionary = {}
    for word in list_of_strings:
        word_length = len(word)
        if word_length % 2 == 0:
            word_length_parity = "even"
        else:
            word_length_parity = "odd"
        nested_dictionary[word] = {
            "length": word_length,
            "parity": word_length_parity,
        }
    return nested_dictionary

example_strings = ["data", "science"]
print(Nested_Dictionaries_from_Strings(example_strings))