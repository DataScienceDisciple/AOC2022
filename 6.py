def solution1():
    f = open('data/6.in')
    input_message = f.readline().strip()
    for i in range(len(input_message)):
        if len(set(input_message[i:i + 4])) == 4:
            return i + 4


print(solution1())


def solution2():
    f = open('data/6.in')
    input_message = f.readline().strip()
    for i in range(len(input_message)):
        if len(set(input_message[i:i + 14])) == 14:
            return i + 14


print(solution2())
