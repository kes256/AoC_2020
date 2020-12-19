with open('input18.txt') as f:
    inputs = f.readlines()


def value(piece):
    total, remainder = piece.split(' ', 1)
    total = int(total)
    remainder = remainder + ' '
    while remainder:
        operation, next, remainder = remainder.split(' ', 2)
        if operation == '+':
            total += int(next)
        elif operation == '*':
            total *= int(next)
        else:
            print(f'Unknown operator: {operation}')
            return '-1'
    return str(total)


def pieces(puzzle):
    while '(' in puzzle:
        start = puzzle.find('(')
        next_close = puzzle.find(')', start + 1)
        opens = puzzle.count('(', start + 1, next_close)
        closes = puzzle.count(')', start + 1, next_close)
        while opens != closes:
            next_close = puzzle.find(')', next_close + 1)
            closes += 1
            opens = puzzle.count('(', start + 1, next_close)
        sub = pieces(puzzle[start + 1:next_close])
        puzzle = puzzle[:start] + sub + puzzle[next_close + 1:]
        puzzle = puzzle.replace('  ', ' ')

    return value(puzzle)


expressions = ['1 + (2 * 3) + (4 * (5 + 6))\n',
               '2 * 3 + (4 * 5)',
               '5 + (8 * 3 + 9 + 3 * 4 * 3)',
               '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
               '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
answers = [51, 26, 437, 12240, 13632]

for expression, answer in zip(expressions, answers):
    assert(int(pieces(expression)) == answer)

total = 0
for expression in inputs:
    total += int(pieces(expression))
print(total)


def value(piece):
    sums = piece.split(' * ')
    multiplicands = [sum([int(summand) for summand in x.split(' + ')]) for x in sums]
    prod = 1
    for mult in multiplicands:
        prod *= mult
    return str(prod)


answers = [51, 46, 1445, 669060, 23340]

for expression, answer in zip(expressions, answers):
    assert(int(pieces(expression)) == answer)

total = 0
for expression in inputs:
    total += int(pieces(expression))
print(total)
