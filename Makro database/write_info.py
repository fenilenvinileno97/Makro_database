#!/usr/bin/env python3
from fractions import Fraction
import re

def fix_function(input_string):
    regexp = r"[<>=~][0-9]"
    match = re.search(regexp, input_string)
    if match:
        first_char = match.group()[0]
        input_string = input_string.replace(first_char, first_char + " ")
        return input_string
    else:
        return input_string

try:
    def get_ranges_string(input_string):
        
        input_list = input_string.replace(";", "").split()

        for s in input_list:

            if "<" in input_list:
                s = float(Fraction(input_list[1])) - \
                    0.1*float(Fraction(input_list[1]))
                s *= float((input_list[2]))
                return "{a:.2f} {b}\n".format(a=s, b=input_list[3])

            elif "<=" in input_list:
                s = float(Fraction(input_list[1])) - \
                    0.05*float(Fraction(input_list[1]))
                s *= float((input_list[2]))
                return "{a:.2f} {b}\n".format(a=s, b=input_list[3])

            elif "~" in input_list:
                s = float(Fraction(input_list[1])) - \
                    0.01*float(Fraction(input_list[1]))
                s *= float((input_list[2]))
                return "{a:.2f} {b}\n".format(a=s, b=input_list[3])

            elif ">=" in input_list:
                s = float(Fraction(input_list[1])) + \
                    0.05*float(Fraction(input_list[1]))
                s *= float((input_list[2]))
                return "{a:.2f} {b}\n".format(a=s, b=input_list[3])

            elif ">" in input_list:
                s = float(Fraction(input_list[1])) + \
                    0.1*float(Fraction(input_list[1]))
                s *= float((input_list[2]))
                return "{a:.2f} {b}\n".format(a=s, b=input_list[3])
            
            else:
                return input_string
            
except TypeError:
    print('Enter a valid input')

def open_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(filepath, 'w', encoding = 'utf-8') as w:
        for row in lines:
            transformed_line = get_ranges_string(fix_function(row))
            w.write(transformed_line)
        print("Written file")
        
open_data("./files/data.txt")