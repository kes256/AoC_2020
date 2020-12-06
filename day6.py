with open('input6.txt') as f:
    inputs = f.read()

inputs = inputs.split('\n\n')
count = 0
for line in inputs:
    answers = set(line.strip()) - {' ', '\n'}
    count += len(answers)
print(count)

count = 0
for line in inputs:
    answers = [set(x.strip()) for x in line.split()]
    all_ans = answers[0]
    for ans in answers:
        if not all_ans:
            break
        all_ans = all_ans.intersection(ans)
    count += len(all_ans)
print(count)