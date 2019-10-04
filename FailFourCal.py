from SafeFourCal import *

class FailFourCal(SafeFourCal):
    def mul(self):
        if self.first == 0 or self.second == 0:
            print("Fail 입니다 두수 중 하나는 0 입니다")
        else:
            result = self.first*self.second
            return result

if __name__ ==  '__main__':
    a = FailFourCal(4,0)
    print("FailFourCal의 add",a.add())
    print("FailFourCal의 sub",a.sub())
    print("FailFourCal의 mul",a.mul())
    print("FailFourCal의 div",a.div())