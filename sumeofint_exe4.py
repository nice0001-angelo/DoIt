def solution(a, b):
    answer = 0
    if a >= b:
        answer = b
        while b < a:
            b += 1
            answer += b
    else:
        answer = a
        while a < b:
            a += 1
            answer += a
    return answer

if __name__ == "__main__":
    print(solution(5,3))
