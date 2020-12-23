import time
with open('input22.txt') as f:
    inputs = f.read()


def build_deck(decks):
    players = {1: decks[0].strip().split('\n'),
               2: decks[1].strip().split('\n')}
    for player in players.keys():
        name = players[player].pop(0)
        assert(name == f'Player {player}:')
        deck = players[player]
        players[player] = [int(card) for card in deck]
    return players


def play_game(players):
    while players[1] and players[2]:
        cards = [players[i].pop(0) for i in [1, 2]]
        if cards[0] > cards[1]:
            players[1].extend(cards)
        else:
            players[2].extend([cards[1], cards[0]])


def score_game(players):
    total = 0
    name = 0
    for player, deck in players.items():
        if not deck:
            continue
        name = player
        i = len(deck)
        for value in deck:
            total += value * i
            i -= 1
    return total, name


decks = inputs.split('\n\n')
state = build_deck(decks)
play_game(state)
total, name = score_game(state)
print(f'Player {name} wins with score: {total}')


def play_recursive_game(players):
    previous_states = {(tuple(players[1]), tuple(players[2])): 0}
    while players[1] and players[2]:
        cards = [players[i].pop(0) for i in [1, 2]]
        if len(players[1]) >= cards[0] and len(players[2]) >= cards[1]:
            winner = play_recursive_game({1: players[1][:cards[0]], 2: players[2][:cards[1]]})
        elif cards[0] > cards[1]:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            players[1].extend(cards)
        else:
            players[2].extend([cards[1], cards[0]])
        if (tuple(players[1]), tuple(players[2])) in previous_states.keys():
            players[2] = []
            return 1
        previous_states[(tuple(players[1]), tuple(players[2]))] = 0
    if players[1]:
        return 1
    else:
        return 2


start = time.time()
decks = inputs.split('\n\n')
state = build_deck(decks)
play_recursive_game(state)
total = score_game(state)
print(f'Player {name} wins with score: {total}, {time.time() - start}')
