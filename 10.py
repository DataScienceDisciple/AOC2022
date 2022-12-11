command_list = open('data/10.in', 'r').readlines()


def solution1(commands):
    cycle_values = [1]

    for command in commands:
        if command.startswith("a"):
            for i in range(2):
                if i == 0:
                    cycle_values.append(cycle_values[-1])
                if i == 1:
                    cycle_values.append(cycle_values[-1] + int(command.split()[1]))
        elif command.startswith("n"):
            cycle_values.append(cycle_values[-1])

    score = sum([i * cycle_values[i - 1] for i in range(20, 240, 40)])
    return cycle_values, score


sprite, ans1 = solution1(command_list)
print(ans1)


def solution2(sprite_values):
    output = ""
    for i, value in enumerate(sprite_values):
        if sprite_values[i] in range((i % 40) - 1, (i % 40) + 2):
            output += "#"
        else:
            output += "."
        if (i + 1) % 40 == 0:
            output += "\n"
    return output


ans2 = solution2(sprite)
print(ans2)
