import sys
import numpy

def get_filename():
    script = sys.argv[0]
    filename = sys.argv[1]
    return filename

def print_mean(filename):
    data = numpy.loadtxt(filename, delimiter=',')
    for m in numpy.mean(data, axis=1):
        print(m)

if __name__ == '__main__':
    filename = get_filename()
    print_mean(filename)
