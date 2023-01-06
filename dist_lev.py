def large_length(func):
    def wrapper(word_one, word_two):
        size_one, size_two = len(word_one), len(word_two)
        if size_one == 0 or size_two == 0:
            return size_one if size_one >= size_two else size_two
        else:
            return func(word_one, word_two) if size_one >= size_two \
                else func(word_two, word_one)

    return wrapper


def update_matrix(number_character, size_word=None, array=None):
    d_matrix = []
    if array is None:
        d_matrix.append([i for i in range(size_word + 1)])
    else:
        d_matrix.append(array)
        size_word = len(array) - 1
    d_matrix.append([0] * (size_word + 1))
    d_matrix[1][0] += number_character
    return d_matrix, number_character + 1


@large_length
def lev(word_one, word_two):
    i = 1
    matrix, i = update_matrix(number_character=i, size_word=len(word_two))
    for l in range(len(word_one)):
        for j in range(len(word_two)):
            if word_one[l] != word_two[j]:
                matrix[1][j + 1] = min([matrix[0][j + 1] + 1, matrix[1][j] + 1, matrix[0][j] + 1])
            else:
                matrix[1][j + 1] = min([matrix[0][j + 1] + 1, matrix[1][j] + 1, matrix[0][j]])
        matrix, i = update_matrix(number_character=i, array=matrix[1])
    return matrix[0][-1]


if __name__ == '__main__':
    # проверяем алгоритм Левенштейна
    print(lev('проверка расстояния Леванштейна', 'проверка системы Леванштейна'))
