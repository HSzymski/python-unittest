amount = 1000
tax_rate = .15

assert amount >= 0, 'The amount should not be negative'
assert 0 < tax_rate < 1, 'Tax rate should be between 0 and 1'

width = int(input('Enter width of the rectangle: '))
assert width > 0, 'The width value must be positive'
hight = int(input('Enter hight of the rectangle: '))
assert hight > 0, 'The hight value must be positive'

area = width * hight
print(area)
