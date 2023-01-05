from dist_lev import lev
import sys


def loss_metric(str_one, str_two):
    return lev(str_one, str_two) / len(str_two)


if __name__ == '__main__':
    read, write = sys.argv[1:]
    files_path = open(read).read().split()
    i = 0
    lev_size = ''
    while i < len(files_path):
        lev_size += str(loss_metric(list(open(files_path[i], encoding='UTF-8').read()),
                                     list(open(files_path[i + 1], encoding='UTF-8').read()))) + '\n'
        i += 2

    file_write = open(write, 'w')
    file_write.write(lev_size)
    file_write.close()

