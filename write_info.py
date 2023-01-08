
def is_list(obj):
    if isinstance(obj, list):
        return True
    elif isinstance(obj, str):
        return obj
    return False


def write_data(filepath='./files/data.txt'):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()

    with open(filepath, "w", encoding = 'utf-8') as file:
        file.writelines(lines)
            
    return 'Changes are done'

overwrite_data = write_data(filepath= './files/data.txt')
print(overwrite_data)

