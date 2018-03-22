# -*- coding: utf-8 -*-

""" Program in Python 3.6.4
    Calculating the numeric value of a Roman numeral.
    Here is an example of calculating:

roman           CXLIV
values          [100, 10, 50, 1, 5]

values[:-1]     [100,      10,      50,     1]
values[1:]      [10,       50,      1,      5]
zip             [(100,10), (10,50), (50,1), (1,5)]
sum               100      -10       50     -1       +5

result          144
"""


def convert_roman_to_arabic():
    roman = input("Enter the roman number: ").upper()
    
    """Check valid input"""
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}    
    invalid = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
    
    if (any(sub in roman for sub in invalid) or
    not any(sign in roman for sign in trans.keys())):
        print('Invalid input format: {}. Reenter'.format(roman))
        convert_roman_to_arabic()
        return
    
    """Calculate the numeric value of a Roman numeral"""
    values = [trans[sign] for sign in roman]
    result = sum(
        val if val >= next_val else -val
        for val, next_val in zip(values[:-1], values[1:])
    ) + values[-1]
    
    print('Numeric value of a Roman numeral: {}'.format(result))


convert_roman_to_arabic()
