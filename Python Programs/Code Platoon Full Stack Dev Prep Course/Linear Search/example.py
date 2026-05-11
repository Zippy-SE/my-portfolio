import linear_search

# Example 1: Using linear_search (finds first occurrence)
numbers = [10, 20, 30, 40, 50, 30]
result = linear_search.linear_search(30, numbers)
print(f"First occurrence of 30 is at index: {result}")
# Output: First occurrence of 30 is at index: 2

# Example 2: Search for something that doesn't exist
result = linear_search.linear_search(99, numbers)
print(f"Search for 99: {result}")
# Output: Search for 99: None

# Example 3: Using global_linear_search (finds all occurrences)
bananas_list = list("bananas")
print(bananas_list)
# Output: ['b', 'a', 'n', 'a', 'n', 'a', 's']

all_a_indices = linear_search.global_linear_search("a", bananas_list)
print(f"All occurrences of 'a': {all_a_indices}")
# Output: All occurrences of 'a': [1, 3, 5]

# Example 4: Global search with no matches
no_match = linear_search.global_linear_search("x", bananas_list)
print(f"All occurrences of 'x': {no_match}")
# Output: All occurrences of 'x': []

# Example 5: Global search with multiple duplicates
numbers2 = [5, 2, 5, 8, 5, 1, 5]
fives = linear_search.global_linear_search(5, numbers2)
print(f"All occurrences of 5: {fives}")
# Output: All occurrences of 5: [0, 2, 4, 6]