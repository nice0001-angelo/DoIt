# random.py
import random
import sys

def random_pop(args):
    number = random.randint(0,len(args)-1) #randint를 이용해서 pop 하고자 하는 자릿수 랜덤 반환
    return args.pop(number)

if __name__ == "__main__":
    #args =[1,2,3,4,5]
    args = sys.argv[1:]
    while args:
        print(random_pop(args))

