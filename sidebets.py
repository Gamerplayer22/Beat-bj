# calculating the probabilities of 3 card poker combinations
# (flush, straight, 3 of a kind, straight flush, royal flush)

# flush
def flush(h, d, s, c, remaining_cards):
    probability = [0.0, 0.0, 0.0, 0.0] # H, D, S, C
    probability[0] = (h/remaining_cards) * ((h-1)/(remaining_cards-1)) * ((h-2)/(remaining_cards-2))
    probability[1] = (d/remaining_cards) * ((d-1)/(remaining_cards-1)) * ((d-2)/(remaining_cards-2))
    probability[2] = (s/remaining_cards) * ((s-1)/(remaining_cards-1)) * ((s-2)/(remaining_cards-2))
    probability[3] = (c/remaining_cards) * ((c-1)/(remaining_cards-1)) * ((c-2)/(remaining_cards-2))

    max = probability[0]
    for i in range(len(probability)):
        if probability[i] > max:
            max = probability[i]
            flag = i
    
    if flag == 0:
        t = 'hearts'
    elif flag == 1:
        t = 'diamonds'
    elif flag == 2:
        t = 'spades'
    else:
        t = 'clubs'
    
    return print(f'{t}: {max*100}%')