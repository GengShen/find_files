
import sys
import os


def list_files(path):
    fl = []
    if os.path.isfile(path):
        fl.append(path)
        return fl
    elif os.path.isdir(path):
        try:
            paths = [os.path.join(path, i) for i in os.listdir(path)]
            for i in paths:
                fl += list_files(i)
        except:
            pass
    return fl


def find(word):
    if len(sys.argv) == 3:
        path = sys.argv[2]
    else:
        path = raw_input("search path:")
        if not path:
            path = os.getcwd()
    f = list_files(path)
    result_num = 0
    for i in f:
        if word in i:
            print i
            result_num += 1
    print "result_num:" + str(result_num)
    return 1


if __name__ == "__main__":
    l = len(sys.argv)
    if l == 1:
        words = raw_input("search content:")
    else:
        word = sys.argv[1]
    find(words)
