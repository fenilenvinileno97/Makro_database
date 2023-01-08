
def write_data(filepath='./files/data.txt'):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()

    with open(filepath, "w", encoding = 'utf-8') as file:
        for line in lines:
            words = line.split()
            file.write(" ".join(words) + "\n")

overwrite_data = write_data(filepath= './files/data.txt')
print(overwrite_data)

