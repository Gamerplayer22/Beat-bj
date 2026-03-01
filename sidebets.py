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
    flag = 0
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
    
    return print(f'{t}: {max*100:.2f}% , total: {(probability[0]+probability[1]+probability[2]+probability[3])*100:.2f}%')

# straight
def straight(card_array, remaining_cards):

    probability = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(1,len(probability)-2):
        probability[i] = (card_array[i]/remaining_cards) * (card_array[i+1]/(remaining_cards-1)) * (card_array[i+2]/(remaining_cards-2))

    probability[0] = (card_array[12]/remaining_cards) * (card_array[0]/(remaining_cards-1)) * (card_array[1]/(remaining_cards-2))
    probability[10] = (card_array[9]/remaining_cards) * (card_array[10]/(remaining_cards-1)) * (card_array[11]/(remaining_cards-2))
    probability[11] = (card_array[10]/remaining_cards) * (card_array[11]/(remaining_cards-1)) * (card_array[12]/(remaining_cards-2))

    total = 0
    for i in range(len(probability)):
        total += probability[i]

    return print(f'straight total: {total*100:.2f}%')

# A,2,3
# 2,3,4
# 3,4,5
# 4,5,6
# 5,6,7
# 6,7,8
# 7,8,9
# 8,9,T
# 9,T,J
# T,J,Q
# J,Q,K
# Q,K,A

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

    return print(f'3 of a kind total: {total*100:.2f}%')

# straight flush
def s_f():
    return

# royal flush
def r_f():
    return