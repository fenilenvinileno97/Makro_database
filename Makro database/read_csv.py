#!/usr/bin/env python3
import csv
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


header = ['Local code', 'Reagent name', 'CAS number', 'Chemical category', 'Location', 'Observation', 'Available quantity', 'Total quantity', 'Container size']

def read_csv(filepath):
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter = ',', fieldnames = header)
        next(reader)
        for row in reader:
            # print((row['Available quantity']))
            print(fix_function(row['Available quantity']))


read_csv("./files/example.csv")