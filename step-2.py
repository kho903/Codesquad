cube_array = [
    ['R', 'R', 'W'],
    ['G', 'C', 'W'],
    ['G', 'B', 'B']
]


def u_temp(cube_array):
    temp1 = cube_array[0][0]
    temp2 = cube_array[0][1]
    temp3 = cube_array[0][2]
    return temp1, temp2, temp3


def r_temp(cube_array):
    temp1 = cube_array[0][2]
    temp2 = cube_array[1][2]
    temp3 = cube_array[2][2]
    return temp1, temp2, temp3


def l_temp(cube_array):
    temp1 = cube_array[0][0]
    temp2 = cube_array[1][0]
    temp3 = cube_array[2][0]
    return temp1, temp2, temp3


def b_temp(cube_array):
    temp1 = cube_array[2][0]
    temp2 = cube_array[2][1]
    temp3 = cube_array[2][2]
    return temp1, temp2, temp3


def solution(cube_array, input_value):
    if input_value == 'U':
        temp1, temp2, temp3 = u_temp(cube_array)
        cube_array[0][0], cube_array[0][1], cube_array[0][2] = temp2, temp3, temp1

    elif input_value == 'U\'':
        temp1, temp2, temp3 = u_temp(cube_array)
        cube_array[0][0], cube_array[0][1], cube_array[0][2] = temp3, temp1, temp2

    elif input_value == 'R':
        temp1, temp2, temp3 = r_temp(cube_array)
        cube_array[0][2], cube_array[1][2], cube_array[2][2] = temp2, temp3, temp1

    elif input_value == 'R\'':
        temp1, temp2, temp3 = r_temp(cube_array)
        cube_array[0][2], cube_array[1][2], cube_array[2][2] = temp3, temp1, temp2

    elif input_value == 'L':
        temp1, temp2, temp3 = l_temp(cube_array)
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp3, temp1, temp2

    elif input_value == 'L\'':
        temp1, temp2, temp3 = l_temp(cube_array)
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp2, temp3, temp1

    elif input_value == 'B':
        temp1, temp2, temp3 = b_temp(cube_array)
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp3, temp1, temp2

    elif input_value == 'B\'':
        temp1, temp2, temp3 = b_temp(cube_array)
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp2, temp3, temp1

    return cube_array


input_values = input('CUBE> ')

while input_values != 'Q':
    for i in range(len(input_values)):
        if (i != len(input_values) - 1) and (input_values[i + 1] == '\''):
            i += 1
            solution(cube_array, input_values[i] + '\'')
        else:
            solution(cube_array, input_values[i])
        print(input_values[i])
        for j in range(len(cube_array)):
            for k in range(len(cube_array)):
                print(cube_array[j][k], end='')
            print()
    input_values = input('> ')
    if input_values == 'Q':
        print("Bye~")
