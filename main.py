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
    # keeping track of the suits of the cards
    Hearts = num_decks * 13
    Diamonds = num_decks * 13
    Spades = num_decks * 13
    Clubs = num_decks * 13
    # keeping track of the count of value cards
    array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A
    card_array = [(x + 4)*num_decks for x in array]

    # build dictionary for the shoe
    for i in range(len(deck.deck)):
        d.update({deck.deck[i] : num_decks})


    while(1):
        card = input('Card: ')
        if d[card] != 0:
            d[card] -= 1
            remaining_shoe_count -= 1
            # updating the suit count
            if card[0] == 'H':
                Hearts -= 1
            elif card[0] == 'D':
                Diamonds -= 1
            elif card[0] == 'S':
                Spades -= 1
            else:
                Clubs -= 1
            # updating running count
            if card[1] in ['A', 'K', 'Q', 'J', 'T']:
                running_count -= 1
            elif card[1] in ['2', '3', '4', '5', '6']:
                running_count += 1
            # updating value counts
            if card[1] in ['2', '3', '4', '5', '6', '7', '8' , '9']:
                card_array[int(card[1])+1] -= 1
            elif card[1] == 'T':
                card_array[8] -= 1
            elif card[1] == 'J':
                card_array[9] -= 1
            elif card[1] == 'Q':
                card_array[10] -= 1
            elif card[1] == 'K':
                card_array[11] -= 1
            elif card[1] == 'A':
                card_array[12] -= 1
        print('count: ',true_count(running_count,remaining_shoe_count))
        print(sidebets.flush(Hearts,Diamonds,Spades,Clubs,remaining_shoe_count))
        print(sidebets.trips(card_array,remaining_shoe_count))