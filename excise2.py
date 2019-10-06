import sys

class Calculator:
    def __init__(self):
        self.value =  0

    def add(self,val):
        self.value +=val

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -=val


class MaxLimitCalculator(UpgradeCalculator):
    def add(self,val):
        self.value += val
        if self.value <= 100:
            self.value
        else:
            self.value = 100
            print("not allowed")

if __name__ == "__main__":
    cal = MaxLimitCalculator()
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    cal.add(a)
    cal.add(b)

    print(cal.value)
