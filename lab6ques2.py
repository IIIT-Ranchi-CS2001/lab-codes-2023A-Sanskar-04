def my_max(input_data):
    if isinstance(input_data, list):
        max_value = input_data[0]
        for item in input_data:
            if item > max_value:
                max_value = item
        return max_value

    elif isinstance(input_data, set):
        max_value = next(iter(input_data))
        for item in input_data:
            if item > max_value:
                max_value = item
        return max_value

    elif isinstance(input_data, tuple):
        max_value = input_data[0]
        for item in input_data:
            if item > max_value:
                max_value = item
        return max_value

    else:
        raise TypeError("Input must be a list, set, or tuple.")


# Example usage:
print(my_max([10, 20, 5, 30, 25]))
print(my_max({10, 20, 5, 30, 25}))
print(my_max((10, 20, 5, 30, 25)))
