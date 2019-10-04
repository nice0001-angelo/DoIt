class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def set_data(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first+self.second
        return result

    def sub(self):
        result = self.first-self.second
        return result

    def mul(self):
        result = self.first*self.second
        return result

    def div(self):
        result = self.first/self.second
        return result

if __name__ ==  '__main__':
    a=FourCal(20,14)
    print("FourCal의 add",a.add())
    print("FourCal의 sub",a.sub())




