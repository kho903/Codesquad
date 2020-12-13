cube_array = [
    ['R', 'R', 'W'],
    ['G', 'C', 'W'],
    ['G', 'B', 'B']
]


def solution(cube_array, input_value):
    if input_value == 'U':
        temp1 = cube_array[0][0]
        temp2 = cube_array[0][1]
        temp3 = cube_array[0][2]
        cube_array[0][0], cube_array[0][1], cube_array[0][2] = temp2, temp3, temp1
    elif input_value == 'U\'':
        temp1 = cube_array[0][0]
        temp2 = cube_array[0][1]
        temp3 = cube_array[0][2]
        cube_array[0][0], cube_array[0][1], cube_array[0][2] = temp3, temp1, temp2
    elif input_value == 'R':
        temp1 = cube_array[0][2]
        temp2 = cube_array[1][2]
        temp3 = cube_array[2][2]
        cube_array[0][2], cube_array[1][2], cube_array[2][2] = temp2, temp3, temp1
    elif input_value == 'R\'':
        temp1 = cube_array[0][2]
        temp2 = cube_array[1][2]
        temp3 = cube_array[2][2]
        cube_array[0][2], cube_array[1][2], cube_array[2][2] = temp3, temp1, temp2
    elif input_value == 'L':
        temp1 = cube_array[0][0]
        temp2 = cube_array[1][0]
        temp3 = cube_array[2][0]
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp3, temp1, temp2
    elif input_value == 'L\'':
        temp1 = cube_array[0][0]
        temp2 = cube_array[1][0]
        temp3 = cube_array[2][0]
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp2, temp3, temp1
    elif input_value == 'B':
        temp1 = cube_array[2][0]
        temp2 = cube_array[2][1]
        temp3 = cube_array[2][2]
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp3, temp1, temp2
    elif input_value == 'B\'':
        temp1 = cube_array[2][0]
        temp2 = cube_array[2][1]
        temp3 = cube_array[2][2]
        cube_array[0][0], cube_array[1][0], cube_array[2][0] = temp2, temp3, temp1
    return cube_array


input_values = input('CUBE> ')

while input_values != 'Q':
    for value in input_values:
        solution(cube_array, value)
        print(value)
        for j in range(len(cube_array)):
            for k in range(len(cube_array)):
                print(cube_array[j][k], end='')
            print()
    input_values = input('> ')
    if input_values == 'Q':
        print("BYE~")
