'''
def solution(answers):
    student = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0] * len(student)

    for answers_k, answers_v in enumerate(answers):
        for student_k, student_v in enumerate(student):
            if answers_v == student_v[answers_k % len(student_v)]:
                score[student_k] += 1
    return [student_k + 1 for student_k, student_v in enumerate(score) if student_v == max(score)]

if __name__ == "__main__":
    print(solution([4,5,4,3,2,1]))
'''

def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []

    for a_k, a_v in enumerate(answers):
        if a_v == student1[a_k%len(student1)]:
            score[0] +=1
        if a_v == student2[a_k%len(student2)]:
            score[1] +=1
        if a_v == student3[a_k%len(student3)]:
            score[2] +=1

    for s_k, s_v in enumerate(score):
        if s_v == max(score):
            result.append(s_k+1)
    return result

if __name__ == "__main__":
    print(solution([4,5,4,3,2,1]))
