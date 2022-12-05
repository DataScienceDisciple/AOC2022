import numpy as np


def map_input_structure_to_dict(raw_crate_list):
    crate_dict = {}
    crate_array = np.array([list(line[1::4]) for line in raw_crate_list]).T
    for i, row in enumerate(crate_array, start=1):
        crate_dict[i] = [el for el in row if el.strip()]
    return crate_dict


def map_moves_to_list(raw_moves):
    return [list(map(int, line.strip().split(' ')[1::2])) for line in raw_moves]


def move_crates(crate_dict, current_move, task):
    if task == 1:
        crate_dict[current_move[2]].extend(crate_dict[current_move[1]][-current_move[0]:][::-1])
    elif task == 2:
        crate_dict[current_move[2]].extend(crate_dict[current_move[1]][-current_move[0]:])
    del crate_dict[current_move[1]][-current_move[0]:]
    return crate_dict


def solution(task):
    structure_file = open('data/5-structure.in')
    moves_file = open('data/5-moves.in')
    raw_crate_list = structure_file.readlines()[::-1]
    raw_moves = moves_file.readlines()
    crate_dict = map_input_structure_to_dict(raw_crate_list)
    move_list = map_moves_to_list(raw_moves)
    for current_move in move_list:
        crate_dict = move_crates(crate_dict, current_move, task)
    return ''.join([column[-1] for column in crate_dict.values()])


print(solution(task=1))
print(solution(task=2))
