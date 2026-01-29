# Distribution Analysis

def distribution_analysis (list_of_numbers):
    if type(list_of_numbers) != list or len(list_of_numbers) == 0: # Validate if input is a list or not
        return "Invalid input"

    total_elements = len(list_of_numbers)
    unique_elements = sorted(set(list_of_numbers)) # Get unique elements (delete duplicates)

# Building the dictionary
    result_dictionary = {}
    for key_value in unique_elements:
        less_or_equal_elements_count = 0
        for element in list_of_numbers:
            if element <= key_value:
                less_or_equal_elements_count += 1

        less_or_equal_elements_percentage = less_or_equal_elements_count / total_elements * 100
        result_dictionary[key_value] = less_or_equal_elements_percentage
    return result_dictionary

numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(numbers))
