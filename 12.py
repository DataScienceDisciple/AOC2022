import numpy as np
from itertools import product

S = -14
E = -28


def iterate_dijkstra(heights, cur_node_coord, distance_dict, visited_list, task):
    next_coord_down = (cur_node_coord[0] + 1, cur_node_coord[1])
    next_coord_up = (cur_node_coord[0] - 1, cur_node_coord[1])
    next_coord_right = (cur_node_coord[0], cur_node_coord[1] + 1)
    next_coord_left = (cur_node_coord[0], cur_node_coord[1] - 1)

    # check down step
    if (cur_node_coord[0] < heights.shape[0] - 1) and (
            check_if_step_possible(heights, cur_node_coord, next_coord_down, task)) and (
            next_coord_down not in visited_list):
        distance_dict = update_distance(distance_dict, cur_node_coord, next_coord_down)

    # check up step
    if (cur_node_coord[0] > 0) and (
            check_if_step_possible(heights, cur_node_coord, next_coord_up, task)) and (
            next_coord_up not in visited_list):
        distance_dict = update_distance(distance_dict, cur_node_coord, next_coord_up)

    # check right step
    if (cur_node_coord[1] < heights.shape[1] - 1) and (
            check_if_step_possible(heights, cur_node_coord, next_coord_right, task)) and (
            next_coord_right not in visited_list):
        distance_dict = update_distance(distance_dict, cur_node_coord, next_coord_right)

    # check left step
    if (cur_node_coord[1] > 0) and (
            check_if_step_possible(heights, cur_node_coord, next_coord_left, task)) and (
            next_coord_left not in visited_list):
        distance_dict = update_distance(distance_dict, cur_node_coord, next_coord_left)
    visited_list.append(cur_node_coord)

    return distance_dict, visited_list


def check_if_step_possible(heights, cur_node_coord, next_node_coord, task):
    if task == 1:
        return True if heights[next_node_coord[0], next_node_coord[1]] - 1 <= heights[  # TASK 1
            cur_node_coord[0], cur_node_coord[1]] else False
    elif task == 2:
        return True if heights[next_node_coord[0], next_node_coord[1]] + 1 >= heights[  # TASK 2
            cur_node_coord[0], cur_node_coord[1]] else False


def update_distance(distance_dict, cur_node_coord, next_node_coord):
    if distance_dict[next_node_coord] == np.inf:
        distance_dict[next_node_coord] = distance_dict[cur_node_coord] + 1
        return distance_dict
    elif distance_dict[next_node_coord] > distance_dict[cur_node_coord]:
        distance_dict[next_node_coord] = distance_dict[cur_node_coord] + 1
        return distance_dict
    else:
        return distance_dict


def solution2(array_height):
    s_coord = np.where(array_height == S)[0][0], np.where(array_height == S)[1][0]
    e_coord = np.where(array_height == E)[0][0], np.where(array_height == E)[1][0]
    distances = {key: np.inf for key in list(product(range(array_height.shape[0]), range(array_height.shape[1])))}
    distances[e_coord] = 0

    array_height[s_coord[0], s_coord[1]] = ord("a") - 97
    array_height[e_coord[0], e_coord[1]] = ord("z") - 97

    visited_places = []
    current_coord = e_coord
    unvisited_coords = list(distances.keys())
    a_squares = list(zip(np.where(array_height == 0)[0], np.where(array_height == 0)[1]))

    while visited_places != a_squares:
        distances, visited_places = iterate_dijkstra(array_height, current_coord, distances, visited_places, task=2)
        unvisited_coords.remove(current_coord)
        unvisited_dict = {key: distance for key, distance in distances.items() if key in unvisited_coords}
        if unvisited_dict:
            current_coord = min(unvisited_dict, key=unvisited_dict.get)
        else:
            return min([value for key, value in distances.items() if key in a_squares])


def solution1(array_height):
    s_coord = np.where(array_height == S)[0][0], np.where(array_height == S)[1][0]
    e_coord = np.where(array_height == E)[0][0], np.where(array_height == E)[1][0]
    distances = {key: np.inf for key in list(zip(np.where(array_height != S)[0], np.where(array_height != S)[1]))}
    distances[s_coord] = 0

    array_height[s_coord[0], s_coord[1]] = ord("a") - 97
    array_height[e_coord[0], e_coord[1]] = ord("z") - 97

    visited_places = []
    current_coord = s_coord
    unvisited_coords = list(distances.keys())

    while e_coord not in visited_places:
        distances, visited_places = iterate_dijkstra(array_height, current_coord, distances, visited_places, task=1)
        unvisited_coords.remove(current_coord)
        unvisited_dict = {key: distance for key, distance in distances.items() if key in unvisited_coords}
        current_coord = min(unvisited_dict, key=unvisited_dict.get)
    return distances[e_coord]


input_list = open('data/12.in', 'r').readlines()
heights = np.array([[ord(letter) - 97 for letter in line.strip()] for line in input_list])
print(solution1(heights))

input_list = open('data/12.in', 'r').readlines()
heights = np.array([[ord(letter) - 97 for letter in line.strip()] for line in input_list])
print(solution2(heights))
