# TASK 1
# A - ROCK, B - PAPER, C - SCISSORS
# X - ROCK, Y - PAPER, Z - SCISSORS
# X - 1, Y - 2, Z - 3

SHAPE_SCORE_TASK_1 = {"X": 1,
                      "Y": 2,
                      "Z": 3}

DUEL_SCORE_TASK_1 = {"A X": 3,
                     "A Y": 6,
                     "A Z": 0,
                     "B X": 0,
                     "B Y": 3,
                     "B Z": 6,
                     "C X": 6,
                     "C Y": 0,
                     "C Z": 3
                     }

# TASK 2
# A - ROCK, B - PAPER, C - SCISSORS
# X - LOSE, Y - DRAW, Z - WIN
# X - 0, Y - 2, Z - 3

DUEL_SCORE_TASK_2 = {"X": 0,
                     "Y": 3,
                     "Z": 6}

SHAPE_SCORE_TASK_2 = {"A X": 3,
                      "A Y": 1,
                      "A Z": 2,
                      "B X": 1,
                      "B Y": 2,
                      "B Z": 3,
                      "C X": 2,
                      "C Y": 3,
                      "C Z": 1
                      }


def evaluate_function_task_1(input_line, shape_score, duel_score):
    return shape_score[input_line[2]] + duel_score[input_line[:3]]


def evaluate_function_task_2(input_line, shape_score, duel_score):
    return shape_score[input_line[:3]] + duel_score[input_line[2]]


def solution(evaluate_function, shape_score, duel_score):
    file = open("data/2.in", "r")
    return sum([evaluate_function(line, shape_score, duel_score) for line in file if line != ''])


print(solution(evaluate_function_task_1, SHAPE_SCORE_TASK_1, DUEL_SCORE_TASK_1))
print(solution(evaluate_function_task_2, SHAPE_SCORE_TASK_2, DUEL_SCORE_TASK_2))
