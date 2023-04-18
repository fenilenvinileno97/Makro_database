#!/usr/bin/env python3
from fractions import Fraction
import re
import csv

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
    
header = ['Local code', 'Reagent name', 'CAS number', 'Chemical category', 'Location', 'Observation', 'Available quantity', 'Total quantity', 'Container size']

def open_data(filepath, writepath):
    with open(filepath, 'r', encoding='ISO-8859-1') as f:
        lines = csv.DictReader(f, delimiter = ',', fieldnames = header)
        next(lines)

        transformed_lines = [row for row in lines]
        for row in transformed_lines:
            row['Available quantity'] = get_ranges_string(fix_function(row['Available quantity'])).strip()
        
    with open(writepath, 'w', encoding = 'utf-8') as out_write:
        writer = csv.DictWriter(out_write, fieldnames=header)
        
        writer.writeheader()
        writer.writerows(transformed_lines)
        print("new.csv file created/written")
        # n = 0
        # for line in transformed_lines:
        #     n+=1
        #     print(str(n) + ".", line['Available quantity'])
        
# open_data("./files/data.txt")
# open_data("./files/db.csv", "./files/data.txt")
open_data("./files/db.csv", "./files/new.csv")