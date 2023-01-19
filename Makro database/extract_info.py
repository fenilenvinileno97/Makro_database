#how to read data from a .csv file in Python scripts?

def is_list(obj):
    if isinstance(obj, list):
        return True
    elif isinstance(obj, str):
        return obj
    return False


def read_data(filepath = './files/data.txt'):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        # lines = f.readlines()
        # return lines
        line = f.read()
        print(line)
    
data = read_data(filepath= './files/data.txt')
print(data)


