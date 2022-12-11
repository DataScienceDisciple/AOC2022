# count items inspected by monkeys after 20 round
# 1 round = every monkey inspected its elements
from tqdm import tqdm


class Monkey:
    def __init__(self,
                 index: int,
                 starting_items: list[int],
                 operation: str,
                 division_test: int,
                 send_indices: list[int]):
        self.index = index
        self.items = starting_items
        self.operation = operation
        self.division_test = division_test
        self.send_indices = send_indices
        self.total_items_checked = 0

    def __repr__(self):
        return f"Monkey(index={self.index}, items={self.items}, operation={self.operation}, division_test={self.division_test}, send_indices={self.send_indices})"

    def update_items(self):
        self.items = [eval(self.operation) // 3 for old in self.items]
        self.total_items_checked += len(self.items)

    def get_monkeys_to_send(self):
        send_on_true_list = [item for item in self.items if item % self.division_test == 0]
        send_on_false_list = [item for item in self.items if item % self.division_test != 0]
        self.items = []
        return {self.send_indices[0]: send_on_true_list,
                self.send_indices[1]: send_on_false_list}

    def receive_items(self, items_to_receive: list[int]):
        self.items.extend(items_to_receive)


input_lines = open('data/11.in', 'r').readlines()
print(input_lines)


def parse_monkeys(inputs: list[str]) -> list[Monkey]:
    indices, items, operations, division_tests, send_indices = [], [], [], [], []
    for line in inputs:
        if line.startswith("Monkey"):
            indices.append(int(line.strip()[-2]))
        elif line.strip().startswith("Starting items:"):
            items.append([int(el) for el in line.strip().replace("Starting items: ", "").split(',')])
        elif line.strip().startswith("Operation"):
            operations.append(line.strip().replace("Operation: new = ", ""))
        elif line.strip().startswith("Test:"):
            division_tests.append(int(line.strip().replace("Test: divisible by ", "")))
        elif line.strip().startswith("If true:"):
            current_send_indices = [int(line.strip().replace("If true: throw to monkey ", ""))]
        elif line.strip().startswith("If false:"):
            current_send_indices.append(int(line.strip().replace("If false: throw to monkey ", "")))
            send_indices.append(current_send_indices)
    return [Monkey(*args) for args in zip(indices, items, operations, division_tests, send_indices)]


monkeys = parse_monkeys(input_lines)


def simulate_cycle(monkey_list: list[Monkey]):
    for monkey in monkey_list:
        monkey.update_items()
        dict_to_send = monkey.get_monkeys_to_send()
        for key in dict_to_send.keys():
            monkey_list[key].receive_items(dict_to_send[key])
    return monkey_list


def solution1(monkey_list, nrounds):
    for _ in tqdm(range(nrounds)):
        monkey_list = simulate_cycle(monkey_list)
        print(monkey_list)
    items_checked_top2 = sorted([monkey.total_items_checked for monkey in monkey_list])[-2:]
    return items_checked_top2[0] * items_checked_top2[1]


print(solution1(monkeys, 20))

