def find_nearest_element(array, target):
    if not array:
        raise ValueError
    nearest_element = min(array, key = lambda x: abs(x - target))
    return nearest_element