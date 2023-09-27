def calc_tax(amount, tax_rate):
    return amount * (tax_rate / 100.)


def calc_tax_2(amount, tax_rate):

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, (int, float)):
        raise TypeError('The tax_rate value must be int or float type.')
    if not 0. < tax_rate < 1.:
        raise ValueError('The tax_rate value must be between 0 and 1.')

    return amount * tax_rate
