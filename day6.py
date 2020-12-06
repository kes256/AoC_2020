with open('input6.txt') as f:
    inputs = f.read()

inputs = inputs.split('\n\n')
count = 0
for line in inputs:
    answers = set(line.strip()) - {' ', '\n'}
    count += len(answers)
print(count)