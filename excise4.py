# excise4.py

# 프로그래머스 체육복 문제 정답
# 리스트 내장 : <표현식> for <아이템> in <시퀀스타입객체> if <조건식>
''''''
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
''''''


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        a = r+1
        b = r-1
        if a in _lost:
            _lost.remove(a)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)