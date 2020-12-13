B_array = [
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
]
W_array = [
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W']
]
O_array = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O']
]
G_array = [
    ['G', 'G', 'G'],
    ['G', 'G', 'G'],
    ['G', 'G', 'G']
]
Y_array = [
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y']
]
R_array = [
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
]

all_array = [B_array, W_array, O_array, G_array, Y_array, R_array]


# Front - W_array, Right - O_array, Left - Y_array, Back - G_array
# Up - B_array, Down - R_array


def traverse_self_front(all_array, i):
    all_array[i][0][0], all_array[i][0][1], all_array[i][0][2], all_array[i][1][0], all_array[i][1][2], \
    all_array[i][2][0], all_array[i][2][1], all_array[i][2][2] = all_array[i][0][2], all_array[i][1][2], \
                                                                 all_array[i][2][2], all_array[i][0][1], \
                                                                 all_array[i][2][1], all_array[i][0][0], \
                                                                 all_array[i][1][0], all_array[i][2][0]


def traverse_self_front_dash(all_array, i):
    all_array[i][0][0], all_array[i][0][1], all_array[i][0][2], all_array[i][1][0], all_array[i][1][2], \
    all_array[i][2][0], all_array[i][2][1], all_array[i][2][2] = all_array[i][2][0], all_array[i][1][0], \
                                                                 all_array[i][0][0], all_array[i][2][1], \
                                                                 all_array[i][0][1], all_array[i][2][2], \
                                                                 all_array[i][1][2], all_array[i][0][2]


def solution(all_array, input_value):
    if input_value == 'F':
        temp = all_array[0][2]  # Up
        all_array[0][2][0], all_array[0][2][1], all_array[0][2][2] = all_array[4][0][2], all_array[4][1][2], \
                                                                     all_array[4][2][2]  # Up
        all_array[4][0][2], all_array[4][1][2], all_array[4][2][2] = all_array[5][0][0], all_array[5][0][1], \
                                                                     all_array[5][0][2]  # LEft
        all_array[5][0][0], all_array[5][0][1], all_array[5][0][2] = all_array[2][0][0], all_array[2][1][0], \
                                                                     all_array[2][2][0]  # Down
        traverse_self_front(all_array, 1)  # front
        all_array[2][0][0], all_array[2][1][0], all_array[2][2][0] = temp  # Right

    elif input_value == 'F\'':
        temp = all_array[0][2]  # Up
        all_array[0][2][0], all_array[0][2][1], all_array[0][2][2] = all_array[2][0][0], all_array[2][1][0], \
                                                                     all_array[2][2][0]
        all_array[2][0][0], all_array[2][1][0], all_array[2][2][0] = all_array[5][0][0], all_array[5][0][1], \
                                                                     all_array[5][0][2]
        all_array[5][0][0], all_array[5][0][1], all_array[5][0][2] = all_array[4][0][2], all_array[4][1][2], \
                                                                     all_array[4][2][2]
        traverse_self_front_dash(all_array, 1)
        all_array[4][0][2], all_array[4][1][2], all_array[4][2][2] = temp  # Left

    elif input_value == 'R':
        temp = all_array[0][0][2], all_array[0][1][2], all_array[0][2][2]
        all_array[0][0][2], all_array[0][1][2], all_array[0][2][2] = all_array[1][0][2], all_array[1][1][2], \
                                                                     all_array[1][2][2]
        all_array[1][0][2], all_array[1][1][2], all_array[1][2][2] = all_array[5][0][2], all_array[5][1][2], \
                                                                     all_array[5][2][2]
        all_array[5][0][2], all_array[5][1][2], all_array[5][2][2] = all_array[3][0][0], all_array[3][1][0], \
                                                                     all_array[3][2][0]
        all_array[3][0][0], all_array[3][1][0], all_array[3][2][0] = temp[-1], temp[-2], temp[-3]
        traverse_self_front(all_array, 2)


    elif input_value == 'R\'':
        temp = all_array[0][0][2], all_array[0][1][2], all_array[0][2][2]
        all_array[0][0][2], all_array[0][1][2], all_array[0][2][2] = all_array[3][2][0], all_array[3][1][0], \
                                                                     all_array[3][0][0]
        all_array[3][0][0], all_array[3][1][0], all_array[3][2][0] = all_array[5][2][2], all_array[5][1][2], \
                                                                     all_array[5][0][2]
        all_array[5][0][2], all_array[5][1][2], all_array[5][2][2] = all_array[1][0][2], all_array[1][1][2], \
                                                                     all_array[1][2][2]
        all_array[1][0][2], all_array[1][1][2], all_array[1][2][2] = temp
        traverse_self_front_dash(all_array, 2)

    elif input_value == 'B':
        temp = all_array[0][0][0], all_array[0][0][1], all_array[0][0][2]
        all_array[0][0][0], all_array[0][0][1], all_array[0][0][2] = all_array[2][0][2], all_array[2][1][2], \
                                                                     all_array[2][2][2]
        all_array[2][0][2], all_array[2][1][2], all_array[2][2][2] = all_array[5][2][2], all_array[5][2][1], \
                                                                     all_array[5][2][0]
        all_array[5][2][0], all_array[5][2][1], all_array[5][2][2] = all_array[4][0][0], all_array[4][1][0], \
                                                                     all_array[4][2][0]
        all_array[4][0][0], all_array[4][1][0], all_array[4][2][0] = temp[-1], temp[-2], temp[-3]
        traverse_self_front(all_array, 3)


    elif input_value == 'B\'':
        temp = all_array[0][0][0], all_array[0][0][1], all_array[0][0][2]
        all_array[0][0][0], all_array[0][0][1], all_array[0][0][2] = all_array[4][0][0], all_array[4][1][0], \
                                                                     all_array[4][2][0]
        all_array[4][0][0], all_array[4][1][0], all_array[4][2][0] = all_array[5][2][2], all_array[5][2][1], \
                                                                     all_array[5][2][0]
        all_array[5][2][2], all_array[5][2][1], all_array[5][2][0] = all_array[2][2][2], all_array[2][1][2], \
                                                                     all_array[2][0][2]
        all_array[2][2][2], all_array[2][1][2], all_array[2][0][2] = temp
        traverse_self_front_dash(all_array, 3)


    elif input_value == 'D':
        temp = all_array[1][2][0], all_array[1][2][1], all_array[1][2][2]
        all_array[1][2][0], all_array[1][2][1], all_array[1][2][2] = all_array[4][2][0], all_array[4][2][1], \
                                                                     all_array[4][2][2]
        all_array[4][2][0], all_array[4][2][1], all_array[4][2][2] = all_array[3][2][0], all_array[3][2][1], \
                                                                     all_array[3][2][2]
        all_array[3][2][0], all_array[3][2][1], all_array[3][2][2] = all_array[2][2][0], all_array[2][2][1], \
                                                                     all_array[2][2][2]
        traverse_self_front(all_array, 5)


    elif input_value == 'D\'':
        temp = all_array[1][2][0], all_array[1][2][1], all_array[1][2][2]
        all_array[1][2][0], all_array[1][2][1], all_array[1][2][2] = all_array[2][2][0], all_array[2][2][1], \
                                                                     all_array[2][2][2]
        all_array[2][2][0], all_array[2][2][1], all_array[2][2][2] = all_array[3][2][0], all_array[3][2][1], \
                                                                     all_array[3][2][2]
        all_array[3][2][0], all_array[3][2][1], all_array[3][2][2] = all_array[4][2][0], all_array[4][2][1], \
                                                                     all_array[4][2][2]
        traverse_self_front_dash(all_array, 5)



    elif input_value == 'U':
        temp = all_array[1][0][0], all_array[1][0][1], all_array[1][0][2]
        all_array[1][0][0], all_array[1][0][1], all_array[1][0][2] = all_array[2][0][0], all_array[2][0][1], \
                                                                     all_array[2][0][2]
        all_array[2][0][0], all_array[2][0][1], all_array[2][0][2] = all_array[3][0][0], all_array[3][0][1], \
                                                                     all_array[3][0][2]
        all_array[3][0][0], all_array[3][0][1], all_array[3][0][2] = all_array[4][0][0], all_array[4][0][1], \
                                                                     all_array[4][0][2]
        traverse_self_front(all_array, 0)


    elif input_value == 'U\'':
        temp = all_array[1][0][0], all_array[1][0][1], all_array[1][0][2]
        all_array[1][0][0], all_array[1][0][1], all_array[1][0][2] = all_array[4][0][0], all_array[4][0][1], \
                                                                     all_array[4][0][2]
        all_array[4][0][0], all_array[4][0][1], all_array[4][0][2] = all_array[3][0][0], all_array[3][0][1], \
                                                                     all_array[3][0][2]
        all_array[3][0][0], all_array[3][0][1], all_array[3][0][2] = all_array[2][0][0], all_array[2][0][1], \
                                                                     all_array[2][0][2]
        traverse_self_front_dash(all_array, 0)

    return all_array


input_values = input("CUBE> ")
while input_values != 'Q':
    for i in range(len(input_values)):
        if (i != len(input_values) - 1) and (input_values[i + 1] == '\''):
            i += 1
            solution(all_array, input_values[i] + '\'')
        else:
            solution(all_array, input_values[i])

    input_value = input("CUBE> ")
