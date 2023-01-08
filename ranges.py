from fractions import Fraction
    
def is_list(obj):
    if isinstance(obj, list):
        return True
    elif isinstance(obj, str):
        return obj
    return False


def get_ranges_list(input_list):
    counter = 0
    modified_list = []
    
    for elements in input_list:
        counter += 1
        modified_list.append(get_ranges_string(elements.replace(",", "").split()))
        
    counter = ["Container no. {}".format(x)
               for x in range(1, len(modified_list)+1)]
    modified_list = [(x, y) for x, y in zip(counter, modified_list)]
    modified_dict = {key: value for key, value in modified_list}
    
    return modified_dict


def get_ranges_string(input_string):

    if is_list(input_string) == input_string:
        input_list = input_string.replace(",", "").split()

    elif is_list(input_string) == True:
        input_list = []
        for key in input_string:
            input_list.append(key)

    for s in input_list:

        if "<" in input_list:
            s = float(Fraction(input_list[1])) - \
                0.1*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif "<=" in input_list:
            s = float(Fraction(input_list[1])) - \
                0.05*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif "~" in input_list:
            s = float(Fraction(input_list[1])) - \
                0.01*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif ">=" in input_list:
            s = float(Fraction(input_list[1])) + \
                0.05*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif ">" in input_list:
            s = float(Fraction(input_list[1])) + \
                0.1*float(Fraction(input_list[1]))
            s *= int(input_list[2])
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])
        
def write_data(filepath='./files/data.txt'):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()

    with open(filepath, "w", encoding = 'utf-8') as file:
        for line in lines:
            if is_list(line) == True:
                words = get_ranges_list(line)
                print(words)
            elif is_list(line) == line:
                words = get_ranges_string(line)
                file.write(words)

def run():
    data = write_data(filepath='./files/data.txt')
    print(data)
    
if __name__ == '__main__':
    run()