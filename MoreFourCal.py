from FourCal import *

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


if __name__ ==  '__main__':
     a = MoreFourCal(4,3)
     print("MoreFourCal의 add",a.add())
     print("MoreFourCal의 div",a.div())