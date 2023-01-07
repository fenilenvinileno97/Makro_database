#how to read data from a .csv file in Python scripts?

def read_data(filepath = './files/data.txt'):
    counter = 0
    with open(filepath, 'r', encoding = 'utf-8') as f:
        for line in f:
            counter += 1
            print(line.strip())
        return counter

def more_two():
    counter = 0
    data = read_data(filepath = './files/data.txt')
    if counter > 2:
        print('Lines are more than two')
        
more_two()



