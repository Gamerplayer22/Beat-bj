import sidebets

# gives the true count
def true_count(running_count,remaining_shoe_count):
    return running_count/(remaining_shoe_count/52)  

def position(card):
    pos = [0, 0]

    if card[1] == 'H':
        pos[0] = 1
    elif card[1] == 'D':
        pos[0] = 2
    elif card[1] == 'C':
        pos[0] = 3
    else:
        pos[0] = 4

    if card[0] == '2':
        pos[1] = 1
    elif card[0] == '3':
        pos[1] = 2
    elif card[0] == '4':
        pos[1] = 3
    elif card[0] == '5':
        pos[1] = 4
    elif card[0] == '6':
        pos[1] = 5
    elif card[0] == '7':
        pos[1] = 6
    elif card[0] == '8':
        pos[1] = 7
    elif card[0] == '9':
        pos[1] = 8
    elif card[0] == 'T':
        pos[1] = 9
    elif card[0] == 'J':
        pos[1] = 10
    elif card[0] == 'Q':
        pos[1] = 11
    elif card[0] == 'K':
        pos[1] = 12
    else:
        pos[1] = 13

    return pos      

if __name__=='__main__':
    # how many decks are in the shoe
    num_decks = int(input('Number of decks used: '))

    running_count = 0

    #       total 2 3 4 5 6 7 8 9 T J Q K A
    # total
    # H    
    # D
    # C
    # S      

    matrix = [[num_decks for _ in range(14)] for _ in range(5)]
    print(matrix)

    for i in range(1,5):
        matrix[i][0] = num_decks * 13

    for i in range(1,14):
        matrix[0][i] = num_decks * 4

    matrix[0][0] = num_decks * 52
    print(matrix)

    while(1):
        card = input('Card: ')
        matrix[0][0] -= 1
        x = position(card)[0]
        y = position(card)[1]
        print(x, y)
        matrix[x][y] -= 1
        matrix[0][y] -= 1
        matrix[x][0] -= 1

            
        print(matrix)