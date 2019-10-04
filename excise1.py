class calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result


if __name__ == '__main__':
    cal1=calculator()
    cal2=calculator()

    print(cal1.add(3))
    print(cal1.add(4))
    print(cal2.add(5))
    print(cal2.add(6))


