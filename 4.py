import numpy as np


def map_ranges_to_arrays(raw_pair):
    split_assignments = raw_pair.strip().split(',')
    return np.array([np.array(el.split('-'), dtype=int) for el in split_assignments])


def get_range_difference(range_arrays):
    return np.diff(range_arrays, axis=0)


def solution1():
    file = open('data/4.in', 'r')
    overlap_counter = 0
    for pair in file:
        range_arrays = map_ranges_to_arrays(pair)
        if np.abs(np.sum(np.sign(get_range_difference(range_arrays)))) < 2:
            overlap_counter += 1
    return overlap_counter


print(solution1())


def get_start_sign_difference(range_arrays):
    return int(np.sign(np.diff(range_arrays, axis=0)[0, 0]))


def get_start_abs_difference(range_arrays):
    return int(np.abs(np.diff(range_arrays, axis=0)[0, 0]))


def solution2():
    file = open('data/4.in', 'r')
    overlap_counter = 0
    for pair in file:
        range_arrays = map_ranges_to_arrays(pair)
        if get_start_sign_difference(range_arrays) < 0:
            range_difference = np.diff(range_arrays)[1]
            start_diff = get_start_abs_difference(range_arrays)
            overlap_counter += sum(range_difference >= start_diff)
        elif get_start_sign_difference(range_arrays) > 0:
            range_difference = np.diff(range_arrays)[0]
            start_diff = get_start_abs_difference(range_arrays)
            overlap_counter += sum(range_difference >= start_diff)
        else:
            overlap_counter += 1
    return overlap_counter


print(solution2())
