from dist_lev import lev
import sys


def lev_metric(str_one, str_two):
    return (len(str_one) - lev(str_one, str_two)) / len(str_one)


if __name__ == '__main__':
    read, write = sys.argv[1:]
    files_path = open(read).read().split()
    i = 0
    lev_size = ''
    for i in range(0, len(files_path), 2):
        string_one = ''.join(open(files_path[i], encoding='UTF-8').read().split())
        string_two = ''.join(open(files_path[i + 1], encoding='UTF-8').read().split())
        lev_size += str(lev_metric(string_one, string_two)) + '\n'

    file_write = open(write, 'w')
    file_write.write(lev_size)
    file_write.close()
