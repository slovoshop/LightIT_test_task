# -*- coding: utf-8 -*-

""" Program in Python 3.6.4
    Calculating the roman value of an arabic number.
    
    Note: 3999 (MMMCMXCIX) - the maximum number
    that can be written in Roman numerals,
    without violating the rules of Shvartsman
    (the rules of writing Roman numerals).
    More than three digits in a row can not be.
"""


def convert_digit(digit, i, v, ix):
    """ Function returns a roman character
        in a given digit of the arabic number """
    
    return (
        ix                  if digit == 9 else
        v + i * (digit - 5) if digit >= 5 else
        i + v               if digit == 4 else
        i * digit              
    )


def convert_arabic_to_roman():

    arabic = input("Enter the arabic number in range 1-3999: ")
    
    try:
        arabic = int(arabic)
    except ValueError:
        pass

    if not (isinstance(arabic, int) and arabic in range(1, 4000)):
        print('Invalid input format: {}. Reenter'.format(arabic))
        convert_arabic_to_roman()
        return
        
    result = 'M' * (arabic // 1000) +\
             convert_digit((arabic // 100) % 10, 'C', 'D', 'CM') +\
             convert_digit((arabic //  10) % 10, 'X', 'L', 'XC') +\
             convert_digit( arabic         % 10, 'I', 'V', 'IX') 

    print('Roman value of an arabic number: {}'.format(result))


convert_arabic_to_roman()
