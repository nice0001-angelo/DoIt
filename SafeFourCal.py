from MoreFourCal import *

class SafeFourCal(MoreFourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result


if __name__ ==  '__main__':
    a=SafeFourCal(10,6)
    print("SafeFourCal의 add", a.add())