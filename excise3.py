import sys

def gugu(argv):
    i = 0
    result = 0
    print("%s단입니다\n" % argv)
    for i in range(1,9):
        result = argv*i
        print("%d * %d = %d\n" % (argv,i,result))

argv = int(sys.argv[1])
gugu(argv)
