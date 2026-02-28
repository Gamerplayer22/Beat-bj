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
    
    return print(f'{t}: {max*100}% , total: {(probability[0]+probability[1]+probability[2]+probability[3])*100}%')

# straight
def straight():
    return

# 3 of a kind
def trips(card_array, remaining_cards):
                  # 2    3    4    5    6    7    8    9    T    J    Q    K    A   
    probability = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(probability)):
        probability[i] = (card_array[i]/remaining_cards) * ((card_array[i]-1)/(remaining_cards-1)) * ((card_array[i]-2)/(remaining_cards-2))
    
    max = probability[0]
    total = 0
    for i in range(len(probability)):
        if probability[i] > max:
            max = probability[i]
        total += probability[i]

    return print(f'total: {total*100}%')

# straight flush
def s_f():
    return

# royal flush
def r_f():
    return