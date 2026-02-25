import deck, sidebets

# gives the true count
def true_count(running_count,remaining_shoe_count):
    return running_count/(remaining_shoe_count/52)
        

if __name__=='__main__':
    # how many decks are in the shoe
    num_decks = int(input('Number of decks used: '))

    d ={}
    running_count = 0
    # how many cards are left in the shoe
    remaining_shoe_count = num_decks * 52
    Hearts = num_decks * 13
    Diamonds = num_decks * 13
    Spades = num_decks * 13
    Clubs = num_decks * 13

    print(Hearts)

    for i in range(len(deck.deck)):
        d.update({deck.deck[i] : num_decks})


    while(1):
        card = input('Card: ')
        if d[card] != 0:
            d[card] -= 1
            remaining_shoe_count -= 1
            if card[0] == 'H':
                Hearts -= 1
            elif card[0] == 'D':
                Diamonds -= 1
            elif card[0] == 'S':
                Spades -= 1
            else:
                Clubs -= 1
            if card[1] in ['A', 'K', 'Q', 'J', 'T']:
                running_count -= 1
            elif card[1] in ['2', '3', '4', '5', '6']:
                running_count += 1
        print('count: ',true_count(running_count,remaining_shoe_count))
        print(Hearts)
        print(sidebets.flush(Hearts,Diamonds,Spades,Clubs,remaining_shoe_count))