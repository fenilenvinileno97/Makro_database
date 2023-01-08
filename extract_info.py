#how to read data from a .csv file in Python scripts?

def read_data(filepath = './files/data.txt'):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        return lines
    
data = read_data(filepath= './files/data.txt')
print(data)


