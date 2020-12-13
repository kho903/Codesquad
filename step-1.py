def reverse_direction(direction):
    if direction.lower() == 'r':
        direction = 'l'
    elif direction.lower() == 'l':
        direction = 'r'
    return direction


def solution(word, int_value, direction):
    int_value = int(int_value)

    if int_value < 0:
        direction = reverse_direction(direction)
        int_value = abs(int_value)
    int_value %= len(word)
    if direction.lower() == 'l':
        return word[int_value:] + word[:int_value]

    elif direction.lower() == 'r':
        return word[-int_value:] + word[:int_value]


input_value = input("> ")
word, int_value, direction = input_value.split(" ")
answer = solution(word, int_value, direction)
print(answer)
