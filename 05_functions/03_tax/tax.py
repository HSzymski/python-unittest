def calc_tax(amount, tax_rate, age):

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, (int, float)):
        raise TypeError('The tax_rate value must be int or float type.')
    if not 0. < tax_rate < 1.:
        raise ValueError('The tax_rate value must be between 0 and 1.')

    if not isinstance(age, (int, float)):
        raise TypeError('The age value must be int or float type.')
    if not age >= 0:
        raise ValueError('The age value must be positive.')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))
