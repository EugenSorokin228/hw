some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]


def item_valid(item):
    if type(item) == int and item > 500:
        return True
    else:
        return False


result = list(filter(item_valid, some_data))
print(result)