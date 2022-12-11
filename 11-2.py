from tqdm import tqdm


class Item:
    def __init__(self,
                 initial_value: int):
        self.value = initial_value
        self.divisible_by = {i: self.value % i for i in [2, 3, 5, 7, 11, 13, 17, 19, 23]}

    def update_divisible_by_on_add(self, add_value):
        for key, value in self.divisible_by.items():
            self.divisible_by[key] = (self.divisible_by[key] + add_value) % key

    def update_divisible_by_on_multiply(self, multiply_value):
        for key, value in self.divisible_by.items():
            self.divisible_by[key] = (self.divisible_by[key] * multiply_value) % key

    def update_divisible_by_on_square(self):
        for key, value in self.divisible_by.items():
            self.divisible_by[key] = (self.divisible_by[key] * self.divisible_by[key]) % key

    def __str__(self):
        return f"Item(value={self.value}, divisible_by={self.divisible_by})"

    def __repr__(self):
        return f"Item(value={self.value}, divisible_by={self.divisible_by})"


class Monkey:
    def __init__(self,
                 index: int,
                 starting_items: list[Item],
                 operation: str,
                 division_test: int,
                 send_indices: list[int]):
        self.index = index
        self.items = starting_items
        self.operation = operation
        self.division_test = division_test
        self.send_indices = send_indices
        self.total_items_checked = 0

    def __str__(self):
        return f"Monkey(index={self.index}, items={self.items}, operation={self.operation}, division_test={self.division_test}, send_indices={self.send_indices})"

    def __repr__(self):
        return f"Monkey(index={self.index}, items={self.items}, operation={self.operation}, division_test={self.division_test}, send_indices={self.send_indices})"

    def update_items(self):
        if "+" in self.operation:
            for item in self.items:
                item.update_divisible_by_on_add(int(self.operation.split()[-1]))
        elif self.operation == "old * old":
            for item in self.items:
                item.update_divisible_by_on_square()
        else:
            for item in self.items:
                item.update_divisible_by_on_multiply(int(self.operation.split()[-1]))

        self.total_items_checked += len(self.items)

    def get_monkeys_to_send(self):
        send_on_true_list = [item for item in self.items if item.divisible_by[self.division_test] == 0]
        send_on_false_list = [item for item in self.items if item.divisible_by[self.division_test] != 0]
        self.items = []
        return {self.send_indices[0]: send_on_true_list,
                self.send_indices[1]: send_on_false_list}

    def receive_items(self, items_to_receive: list[Item]):
        self.items.extend(items_to_receive)


def parse_monkeys(inputs: list[str]) -> list[Monkey]:
    indices, items, operations, division_tests, send_indices = [], [], [], [], []
    for line in inputs:
        if line.startswith("Monkey"):
            indices.append(int(line.strip()[-2]))
        elif line.strip().startswith("Starting items:"):
            items.append(
                [Item(initial_value=int(el)) for el in line.strip().replace("Starting items: ", "").split(',')])
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


def simulate_cycle(monkey_list: list[Monkey]):
    for monkey in monkey_list:
        monkey.update_items()
        dict_to_send = monkey.get_monkeys_to_send()
        for key in dict_to_send.keys():
            monkey_list[key].receive_items(dict_to_send[key])
    return monkey_list


def solution2(monkey_list, nrounds):
    for _ in tqdm(range(nrounds)):
        monkey_list = simulate_cycle(monkey_list)
    items_checked_top2 = sorted([monkey.total_items_checked for monkey in monkey_list])[-2:]
    return items_checked_top2[0] * items_checked_top2[1]


input_lines = open('data/11.in', 'r').readlines()
monkeys = parse_monkeys(input_lines)
print(monkeys)
print(solution2(monkeys, 10000))
