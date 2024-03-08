def calculate_paper(dims):
    sides = [(dims[0] * dims[1]), (dims[1] * dims[2]), (dims[0] * dims[2])]
    return (2*sum(sides) + min(sides)) 

def calculate_ribbon(dims):
    volume = (dims[0] * dims[1] * dims[2])
    return 2 * sum(dims) - 2 * max(dims)  + volume

def total_paper():
    with open("input.txt", 'r') as file:
        data = [line.split() for line in file]
    file.close()
    data = [val_set.split('x') for ele in data for val_set in ele]
    data = [[int(dim) for dim in ele] for ele in data]
    total_paper = [calculate_paper(element) for element in data]
    total_ribbon = [calculate_ribbon(element) for element in data]
    return sum(total_paper), sum(total_ribbon)

results = total_paper()
print(f'total paper neeeded:{results[0]}\ntotal ribbon needed:{results[1]}')