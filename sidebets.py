# calculating the probabilities of 3 card poker combinations
# (flush, straight, 3 of a kind, straight flush, royal flush)

# flush
def flush(matrix):
    probability = 0.0
    for i in range(len(1,5)):
        suit = matrix[i][0]
        total = matrix[0][0]
        probability += ((suit/total) + ((suit-1)/(total-1)) + ((suit-2)/(total-2)))
    return probability

# straight
def straight(matrix):
    probability = 0.0
    for i in range(len(1,11)):
        card = matrix[0][i]
        total = matrix[0][0]
        #probability += 

    return

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
def trips(matrix, remaining_cards):
                  # 2    3    4    5    6    7    8    9    T    J    Q    K    A   
    probability = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    return

# straight flush
def s_f(matrix, remaining_cards):
    probability = [0.0, 0.0, 0.0, 0.0]  # H, D, C, S
    return

# royal flush
def r_f(matrix, remaining_cards):
    return

