from fractions import Fraction

# this function defines if an object is a list, if so, returns True and if it's str, returns object
# is_list is a breakpoint to choose between get_ranges_list() or get_ranges_string()


def is_list(obj):
    if isinstance(obj, list):
        return True
    elif isinstance(obj, str):
        return obj
    return False


def get_ranges_list(input_list):

    modified_list = []

    for elements in input_list:
        modified_list.append(get_ranges_string(
            elements.replace(",", "").split()))

    counter = ["Container no. {}".format(x)
               for x in range(1, len(modified_list)+1)]
    modified_list = [(x, y) for x, y in zip(counter, modified_list)]
    modified_dict = {key: value for key, value in modified_list}

    result = []

    for key, value in modified_dict.items():
        argument = "{} : {}".format(
            key, value.replace(",", "").replace("\n", " "))
        result.append(argument)

    return "; ".join(result)


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
            s *= float((input_list[2]))
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif "<=" in input_list:
            s = float(Fraction(input_list[1])) - \
                0.05*float(Fraction(input_list[1]))
            s *= float((input_list[2]))
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif "~" in input_list:
            s = float(Fraction(input_list[1])) - \
                0.01*float(Fraction(input_list[1]))
            s *= float((input_list[2]))
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif ">=" in input_list:
            s = float(Fraction(input_list[1])) + \
                0.05*float(Fraction(input_list[1]))
            s *= float((input_list[2]))
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])

        elif ">" in input_list:
            s = float(Fraction(input_list[1])) + \
                0.1*float(Fraction(input_list[1]))
            s *= float((input_list[2]))
            return "Estimated quantity is {a:.2f} {b}\n".format(a=s, b=input_list[3])
        
def get_ranges_use(input_obj):
    if is_list(input_obj) == True:
        input_list = []
        for key in input_obj:
            input_list.append(key)
        return get_ranges_list(input_obj)

    elif is_list(input_obj) == input_obj:
        return get_ranges_string(input_obj)


def write_data(filepath='./files/data.txt'):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filepath, "w", encoding='utf-8') as file:
        for line in lines:
            transformed_line = get_ranges_use(line)
            file.write(transformed_line)

    return 'Changes were done'


def run():
    data = write_data(filepath='./files/data.txt')
    print(data)


if __name__ == '__main__':
    run()

# a = '>= 4/5, 2 L'
# b = ['< 1/3, 500 g', '~ 4/5 1.5 L', '>= 3/4, 250 g']
# print(get_ranges_use(a))
# print(get_ranges_use(b))
