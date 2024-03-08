def where_to():
    move = 0
    with open("input.txt", 'r') as file:
        data = file.read()
    file.close()
    for i in data:
        if i == '(':
            move += 1
        if i == ')':
            move -= 1
    return move

def first_basement():
    with open("input.txt", 'r') as file:
        data = file.read()
    print(len(data))
    cur_floor = 0
    for i in range(len(data)):
        if data[i] == '(':
            cur_floor += 1
        if data[i] == ')':
            cur_floor -= 1
        if  cur_floor == -1:
            return i+1
        
print(where_to())
print('\n')
print(first_basement())