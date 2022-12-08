import os
import numpy as np
import matplotlib.pyplot as plt


def save_forest_to_png(array):
    plt.imshow(array)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(os.path.join('images', '8-forest.png'))


def solution1():
    input_list = open('data/8.in', 'r').readlines()
    input_lists = np.array([[int(el) for el in current_list.strip()] for current_list in input_list])
    border_visible = 2 * ((input_lists.shape[0] - 1) + (input_lists.shape[1] - 1))
    save_forest_to_png(input_lists)

    # going from top
    visible_trees = []
    for row in range(1, input_lists.shape[0] - 1):
        current_row = input_lists[row, 1:-1]
        max_heights = np.max(input_lists[:row, 1:-1], axis=0)
        visible_trees.extend([(row, el + 1) for el in np.where(current_row > max_heights)[0]])

    # from down
    for row in range(input_lists.shape[0] - 1, 1, -1):
        current_row = input_lists[row - 1, 1:-1]
        max_heights = np.max(input_lists[row:, 1:-1], axis=0)
        visible_trees.extend([(row - 1, el + 1) for el in np.where(current_row > max_heights)[0]])

    # from left
    for column in range(1, input_lists.shape[1] - 1):
        current_column = input_lists[1:-1, column]
        max_heights = np.max(input_lists[1:-1, :column], axis=1)
        visible_trees.extend([(el + 1, column) for el in np.where(current_column > max_heights)[0]])

    # from right
    for column in range(input_lists.shape[1] - 1, 1, -1):
        current_column = input_lists[1:-1, column - 1]
        max_heights = np.max(input_lists[1:-1, column:], axis=1)
        visible_trees.extend([(el + 1, column - 1) for el in np.where(current_column > max_heights)[0]])

    return len(set(visible_trees)) + border_visible


def get_score(tree_array, tree_index):
    top_array = tree_array[:tree_index[0], tree_index[1]][::-1]
    bottom_array = tree_array[tree_index[0] + 1:, tree_index[1]]
    left_array = tree_array[tree_index[0], :tree_index[1]][::-1]
    right_array = tree_array[tree_index[0], tree_index[1] + 1:]

    top_where = np.where(top_array >= tree_array[tree_index[0], tree_index[1]])[0]
    bottom_where = np.where(bottom_array >= tree_array[tree_index[0], tree_index[1]])[0]
    left_where = np.where(left_array >= tree_array[tree_index[0], tree_index[1]])[0]
    right_where = np.where(right_array >= tree_array[tree_index[0], tree_index[1]])[0]

    top_score = 1 + top_where[0] if top_where.shape[0] != 0 else tree_index[0]
    bottom_score = 1 + bottom_where[0] if bottom_where.shape[0] != 0 else tree_array.shape[0] - tree_index[0] - 1
    left_score = 1 + left_where[0] if left_where.shape[0] != 0 else tree_index[1]
    right_score = 1 + right_where[0] if right_where.shape[0] != 0 else tree_array.shape[1] - tree_index[1] - 1

    return top_score * bottom_score * right_score * left_score


def solution2():
    input_list = open('data/8.in', 'r').readlines()
    input_lists = np.array([[int(el) for el in current_list.strip()] for current_list in input_list])

    biggest_score = 0
    biggest_index = None
    for i in range(1, input_lists.shape[0] - 1):
        for j in range(1, input_lists.shape[1] - 1):
            cur_index = (i, j)
            cur_score = get_score(input_lists, cur_index)
            if cur_score > biggest_score:
                biggest_score = cur_score
                biggest_index = cur_index
    return biggest_score, biggest_index


print(solution1())
print(solution2())
