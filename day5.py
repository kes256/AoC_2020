with open('input5.txt') as f:
    inputs = f.read()

inputs = inputs.replace('B', '1')
inputs = inputs.replace('F', '0')
inputs = inputs.replace('R', '1')
inputs = inputs.replace('L', '0')

boarding_passes = inputs.split()
boarding_pass = max(boarding_passes)
print(int(boarding_pass, 2))

boarding_ids = [int(x, 2) for x in boarding_passes]
seats = set(range(min(boarding_ids), max(boarding_ids)))
empty_seats = seats - set(boarding_ids)
print(empty_seats)

if len(empty_seats) > 1:
    print(f"Choose the seat that does not share a row with {min(boarding_ids)} or {max(boarding_ids)}!")