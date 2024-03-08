def dict_expansion(dict, coords):
    if(coords not in dict):
        dict[coords] = 1
    else:
        dict[coords] += 1

def case_switchboard(instr, pos_x, pos_y):
    match instr:
        case '>':
            pos_x += 1
        case '<':
            pos_x -= 1
        case '^':
            pos_y += 1
        case 'v':
            pos_y -= 1
    return (pos_x, pos_y)

def solution():
    with open('input.txt', 'r') as file:
        data = file.read()
    file.close()
    pos_x = 0
    pos_y = 0
    pos_robo_x = 0
    pos_robo_y = 0
    i = 0
    visited_dict = {(0,0):1}
    for instr in data:
        if i%2 == 0:
            pos_x, pos_y = case_switchboard(instr, pos_x, pos_y)
            dict_expansion(visited_dict, (pos_x, pos_y))
        if  i%2 == 1:
            pos_robo_x, pos_robo_y = case_switchboard(instr, pos_robo_x, pos_robo_y)
            dict_expansion(visited_dict, (pos_robo_x, pos_robo_y))
        i += 1
    return len(visited_dict)

print(solution())