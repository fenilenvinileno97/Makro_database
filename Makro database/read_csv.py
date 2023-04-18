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

def read_csv(filepath, writepath):
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter = ',', fieldnames = header)
        next(reader)
        
        transformed_lines = [row for row in reader]
        for row in transformed_lines:
            row['Available quantity'] = fix_function(row['Available quantity']).strip()

    with open(writepath, 'w', encoding = 'utf-8') as out_write:
        writer = csv.DictWriter(out_write, delimiter = ',', fieldnames=header)
        
        writer.writeheader()
        writer.writerows(transformed_lines)
        print("new.csv file created/written")

read_csv("./files/reagent_database_2023.csv", "./files/new.csv")

