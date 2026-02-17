import deck

if __name__=='__main__':
    num_players = 0
    num_decks = 0

    num_players = int(input('Number of players: '))
    num_decks = int(input('Number of decks used: '))

    card = []

    for j in range(2):
        for i in range(num_players):
            card.append(input('player ' + str(i+1) + ': '))
        card.append(input('dealer: '))

    