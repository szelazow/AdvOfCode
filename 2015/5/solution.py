def is_nice_old(element):
    vowels = 'aeiou'
    same_adjacent = False
    vowel_count = 0
    prev = ''
    for symbol in element:
        if symbol in vowels:
            vowel_count += 1
        if (prev + symbol) in ['ab', 'cd', 'pq', 'xy']:
            return False
        if symbol == prev:
            same_adjacent = True
        prev = symbol
    if vowel_count >= 3 and same_adjacent:
        return True
    else:
        return False

def is_nice_new(element):                       #get two subsequent symbols, search remaining elements for matching pair
    two_non_adj = False
    two_one_gap = False
    for i in range(1,len(element)):
        seeked_pair = (element[i-1], element[i])
        for j in range(i, len(element)):
            if j == (i + 2):
                if element[i] == element[j]:
                    two_one_gap = True
                    if two_non_adj == two_one_gap == True:
                        return True                #  i   j 
            if j >= i + 2:                         #|ab||cd|efg
                if seeked_pair == (element[j-1], element[j]): 
                    two_non_adj = True
                    if two_non_adj == two_one_gap == True:
                        return True
    else:
        return False

def solution(total_text):
    nice_old = 0
    nice_new = 0
    for element in total_text:
        if is_nice_old(element):
            nice_old += 1
        if is_nice_new(element):
            nice_new += 1
    return nice_old, nice_new


line_list = []
 

with open('input.txt', 'r') as file:
    for line in file:
        line_list.append(line)
file.close()

results = solution(line_list)
print(f'Results\nOld rules: {results[0]}\t\tNew rules: {results[1]}')
print(is_nice_new('qjhvhtzxzqqjkmpb'))
print(is_nice_new('xxyxx'))
print(is_nice_new('uurcxstgmygtbstg'))
print(is_nice_new('ieodomkazucvgmuy'))
print(is_nice_new('abababaabababababababababaabababababba'))