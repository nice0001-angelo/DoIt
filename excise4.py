# excise4.py

# 프로그래머스 체육복 문제 정답
'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''

import sys

def solution(n, lost, reserve):
    i = 0
    result = []
    while i < n:
        i = i+1
        result.append(i)
    for x in lost:
        #result.remove(x)
    #print(result)

n = int(sys.argv[1])
lost = (sys.argv[2])
reserve = (sys.argv[3])

print(lost)
print(reserve)
solution(n,lost,reserve)
