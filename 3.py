def letter_to_priority(letter: str):
    """Function used to map letters to their priorities.
    As per description of the task:
        - lower case letters have priorities from 1 to 26 (a to z)
        - upper case letters have priorities from 27 to 52 (A to Z)
    """
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def get_compartments(line: str) -> list[set]:
    """Function used to get compartments for the first task.
    """
    return [set(line[:len(line) // 2]), set(line[len(line) // 2:])]


def get_compartment_intersection(compartments: list[set]) -> str:
    """Function used to get compartments intersection of compartments.
    Works for both tasks.
    """
    return list(set.intersection(*compartments))[0]


def solution1() -> int:
    file = open('data/3.in', 'r')
    return sum(
        [letter_to_priority(
            get_compartment_intersection(
                get_compartments(line)
            )
        )
            for line in file
        ]
    )


print(solution1())


def solution2() -> int:
    lines = open('data/3.in', 'r').readlines()
    score = 0
    for i in range(0, len(lines), 3):
        current_group = [set(el.strip('\n')) for el in lines[i:i + 3]]
        score += letter_to_priority(get_compartment_intersection(current_group))
    return score


print(solution2())
