import linear_search


# --- Tests for linear_search ---

def test_linear_search_finds_first_occurrence():
    assert linear_search.linear_search(5, [1, 2, 3, 4, 5, 6]) == 4

def test_linear_search_finds_at_beginning():
    assert linear_search.linear_search(1, [1, 2, 3, 4, 5]) == 0

def test_linear_search_finds_at_end():
    assert linear_search.linear_search(5, [1, 2, 3, 4, 5]) == 4

def test_linear_search_not_found():
    assert linear_search.linear_search(10, [1, 2, 3, 4, 5]) is None

def test_linear_search_empty_list():
    assert linear_search.linear_search(1, []) is None

def test_linear_search_string_in_list():
    assert linear_search.linear_search("apple", ["banana", "apple", "cherry"]) == 1

def test_linear_search_duplicate_returns_first():
    # Should return the index of the FIRST occurrence
    assert linear_search.linear_search("a", ["a", "b", "a", "c"]) == 0

def test_linear_search_single_element_found():
    assert linear_search.linear_search(42, [42]) == 0

def test_linear_search_single_element_not_found():
    assert linear_search.linear_search(99, [42]) is None


# --- Tests for global_linear_search ---

def test_global_linear_search_multiple_occurrences():
    bananas_list = list("bananas")
    assert linear_search.global_linear_search("a", bananas_list) == [1, 3, 5]

def test_global_linear_search_single_occurrence():
    assert linear_search.global_linear_search(3, [1, 2, 3, 4, 5]) == [2]

def test_global_linear_search_not_found():
    assert linear_search.global_linear_search(10, [1, 2, 3, 4, 5]) == []

def test_global_linear_search_all_same():
    assert linear_search.global_linear_search("x", ["x", "x", "x"]) == [0, 1, 2]

def test_global_linear_search_empty_list():
    assert linear_search.global_linear_search(1, []) == []

def test_global_linear_search_at_start_and_end():
    assert linear_search.global_linear_search("z", ["z", "a", "b", "z"]) == [0, 3]

def test_global_linear_search_consecutive():
    assert linear_search.global_linear_search(2, [1, 2, 2, 2, 3]) == [1, 2, 3]

def test_global_linear_search_strings():
    words = ["hello", "world", "hello", "python", "hello"]
    assert linear_search.global_linear_search("hello", words) == [0, 2, 4]

def test_global_linear_search_none_value():
    # Edge case: searching for None
    assert linear_search.global_linear_search(None, [1, None, 2, None]) == [1, 3]