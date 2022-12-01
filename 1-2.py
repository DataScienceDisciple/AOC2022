with open('data/1.in', 'r') as f:
    lines = f.readlines()

one, two, three = 0, 0, 0
cur_results = 0
for el in lines:
    if el != '\n':
        cur_results += int(el)
    else:
        if cur_results > three:
            if cur_results < two:
                three = cur_results
            elif cur_results < one:
                two, three = cur_results, two
            else:
                one, two, three = cur_results, one, two
        cur_results = 0

print(sum([one, two, three]))
