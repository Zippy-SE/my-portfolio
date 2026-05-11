def linear_search(target, arr):
    """
    Searches for target in arr and returns the index of the first occurrence.
    Returns None if target is not found.
    """
    index = 0
    for element in arr:
        if element == target:
            return index
        index += 1
    return None


def global_linear_search(target, arr):
    """
    Searches for target in arr and returns a list of all indices where target appears.
    Returns an empty list if target is not found.
    """
    result = []
    index = 0
    for element in arr:
        if element == target:
            result.append(index)
        index += 1
    return result


