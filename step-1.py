def solution(word, int_value, direction):
    int_value = int(int_value)
    if direction.lower() == 'l':
        if int_value >= 0:
            int_value %= len(word)
            result = word[int_value:] + word[:int_value]
        elif int_value < 0:
            while len(word) < int_value:
                int_value += len(word)
            result = word

    elif direction.lower() == 'r':
        if int_value >= 0:
            result = word[int_value:] + word[:int_value]
        elif int_value < 0:
            while len(word) < int_value:
                int_value += len(word)
            result = word[int_value:] + word[:int_value]
    return result


input_value = input("> ")
word, int_value, direction = input_value.split(" ")
answer = solution(word, int_value, direction)
print(answer)
