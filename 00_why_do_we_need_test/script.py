def total_price(net_price, tax_rate, discount=False):
    if not discount:
        return int(net_price * (1 + tax_rate / 100.))
    else:
        return int(net_price * (1 + tax_rate / 100.) * .9)


print(total_price(1000, 23))
print(total_price(1000, 23, True))
