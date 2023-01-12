
def adds(string):
    return str(string.split()) + "\n"
        
    


def write_data(filepath='./files/data.txt'):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()

    with open(filepath, "w", encoding = 'utf-8') as file:
        for line in lines:
            modify_line = adds(line)
            file.write(modify_line)
            
    return 'Changes are done'

overwrite_data = write_data(filepath= './files/data.txt')
print(overwrite_data)

