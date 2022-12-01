with open('data/1.in', 'r') as f:
    lines = f.readlines()

max_result = 0
cur_results = 0
for el in lines:
    if el != '\n':
        cur_results += int(el)
    else:
        if cur_results > max_result:
            max_result = cur_results

        cur_results = 0

print(max_result)
