# Excercises to learn how to prove TDD. Most functions take arguments without validation due to task content.

def map_longest(words):
    if type(words) != list or not words:
        return 0
    else:
        lengths = []
        for word in words:
            lengths.append(len(word))
        return max(lengths)


def filter_ge_four_char(words):
    return [word for word in words if len(word) >= 4]


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def count_string(items):
    counter = 0
    return sum([counter+1 for item in items if isinstance(item, str)])


def remove_duplicates(items):
    return list(set(items))


def is_distinct(items):
    return len(set(items)) == len(items)


class Laptop:
    def __init__(self, brand, model, price):
        if not isinstance(brand, str):
            raise TypeError('The brand attribute must be a string.')
        else:
            self.brand = brand

        self.model = model

        if not isinstance(price, (int, float)):
            raise TypeError('The price attribute must be a positive int or float.')
        elif price <= 0:
            raise ValueError('The price attribute must be a value larger than 0.')
        else:
            self._price = price

    def __repr__(self):
        return f"Laptop(brand='{self.brand}', model='{self.model}')"

    @property
    def price(self):
        return self._price


