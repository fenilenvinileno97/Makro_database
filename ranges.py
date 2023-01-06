from fractions import Fraction

def is_list(obj):
    if isinstance(obj, list):
        return True
    elif isinstance(obj, str):
        return obj
    return False

def get_ranges(input_string):
    
    if is_list(input_string) == input_string:
        input_list = input_string.replace(",", "").split()
        return input_list
    
    for s in input_list:
        if "<" in input_list:
            s = float(Fraction(input_list[1]))-0.1*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}".format(a = s, b = input_list[3])
        
        elif "<=" in input_list:
            s = float(Fraction(input_list[1]))-0.05*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}".format(a = s, b = input_list[3])

        elif "~" in input_list:
            s = float(Fraction(input_list[1]))-0.01*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}".format(a = s, b = input_list[3])

        elif ">=" in input_list:
            s = float(Fraction(input_list[1]))+0.05*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}".format(a = s, b = input_list[3])

        elif ">" in input_list:
            s = float(Fraction(input_list[1]))+0.1*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}".format(a = s, b = input_list[3])            
        

# input_one = ["< 1/4, 500 g", "~ 1/2, 400 g", ">= 3/4, 900"]
input_two = "<= 1/4, 500 g"
input_two_list = input_two.replace(",", "").split()

print(get_ranges(input_two_list))