import numpy as np

def process_line(line):                     
    match line.split(' '):
        case ['turn', onoff, p1, 'through', p2]:
            p1 = [int(x) for x in p1.split(',')]
            p2 = [int(x) for x in p2.split(',')]
            return onoff, p1, p2
        case ['toggle', p1, 'through', p2]:
            p1 = [int(x) for x in p1.split(',')]
            p2 = [int(x) for x in p2.split(',')]
            return 'toggle', p1, p2
        case _:
            raise ValueError()


class SolutionFirst:
    def __init__(self):
        self.lights_array = [[False]*1000 for i in range(1000)]
        self.currently_lit = 0

    def switch(self, cmd, p1, p2):
        mov_x = abs(p1[0] - p2[0]) + 1
        mov_y = abs(p1[1] - p2[1]) + 1
        start_point_x = min(p1[0], p2[0])
        start_point_y = min(p1[1], p2[1])                            
        for i in range(start_point_x, start_point_x + mov_x):
            for j in range(start_point_y, start_point_y + mov_y):
                match cmd:
                    case 'toggle':
                        self.lights_array[i][j] = not self.lights_array[i][j]
                    case 'on':
                        self.lights_array[i][j] = True
                    case 'off':
                        self.lights_array[i][j] = False
    
    def count_on(self):
        on_counter = 0
        for i in range(0, 1000):
            for j in range(0, 1000):
                if self.lights_array[i][j]: on_counter += 1
        return on_counter

class SolutionSecond:
    def __init__(self):
        self.lights_array = [[0]*1000 for i in range(1000)]
        self.currently_lit = 0

    def switch(self, cmd, p1, p2):
        mov_x = abs(p1[0] - p2[0]) + 1
        mov_y = abs(p1[1] - p2[1]) + 1
        start_point_x = min(p1[0], p2[0])
        start_point_y = min(p1[1], p2[1])                            
        for i in range(start_point_x, start_point_x + mov_x):
            for j in range(start_point_y, start_point_y + mov_y):
                match cmd:
                    case 'toggle':
                        self.lights_array[i][j] += 2
                    case 'on':
                        self.lights_array[i][j] += 1
                    case 'off':
                        self.lights_array[i][j] = max(0, self.lights_array[i][j] - 1)
    
    def count_pow(self):
        pow_counter = 0
        for i in range(0, 1000):
            for j in range(0, 1000):
                pow_counter += self.lights_array[i][j]
        return pow_counter

def main():
    LightsArrayOld = SolutionFirst()
    LightsArrayNew = SolutionSecond()
    with open('input.txt', 'r') as file:
        commands = file.read()
    file.close()
    commands = commands.splitlines()
    for command in commands:
        cmd, p1, p2 = process_line(command)
        LightsArrayOld.switch(cmd, p1, p2)
        LightsArrayNew.switch(cmd, p1, p2)
    print(f'Old system: {LightsArrayOld.count_on()} New System: {LightsArrayNew.count_pow()}')
    

main()


'''p1_1, p2_1, com1 = process_line('turn on 0,0 through 999,999')
p1_2, p2_2, com2 = process_line('toggle 0,0 through 999,0')
p1_3, p2_3, com3 = process_line('turn off 499,499 through 500,500')
LightsArray = Solution()
print(LightsArray.count_on())
LightsArray.switch(p1_1, p2_1, com1)
print(LightsArray.count_on())
LightsArray.switch(p1_2, p2_2, com2)
print(LightsArray.count_on())
LightsArray.switch(p1_3, p2_3, com3)
print(LightsArray.count_on())
LightsArray = Solution()
p1_3, p2_3, com3 = process_line('turn on 499,499 through 500,500')
LightsArray.switch(p1_3, p2_3, com3)
print(LightsArray.count_on())'''