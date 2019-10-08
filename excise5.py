def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    _a = a*int(10000/len(a))
    _b = b*int(10000/len(b))
    _c = c*int(10000/len(c))
    ___a = _a[0:len(answer)]
    ___b = _b[0:len(answer)]
    ___c = _c[0:len(answer)]
    __a = [x for x in ___a if x not in answers]
    __b = [y for y in ___b if y not in answers]
    __c = [z for z in ___c if z not in answers]
    if len(__a) > len(__b):
        if len(__a) > len(__c):
            answer = [1]
        elif len(__a) == len(__c):
            answer = [1,3]
        else:
            answer = [3]
    elif len(__a) == len(__b):
        if len(__a) == len(__c):
            answer = [1,2,3]
        elif len(__a) > len(__c):
            answer = [1,2]
    else:
        answer = [2]
    return answer

if __name__ == "__main__":
    print(solution([1,3,2,4,2]))