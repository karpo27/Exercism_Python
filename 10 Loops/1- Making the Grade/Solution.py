def round_scores(student_scores):
    for i in range(0, len(student_scores)):
        student_scores[i] = round(student_scores[i])

    return student_scores

def count_failed_students(student_scores):
    c = 0
    for i in student_scores:
        if i <= 40:
            c += 1

    return c
    
def above_threshold(student_scores, threshold): 
    s = []
    for i in student_scores:
        if i >= threshold:
            s.append(i)

    return s
    
def letter_grades(highest):
    value = (highest - 40) / 4
    return [41, int(41 + value), int(41 + 2 * value), int(41 + 3 * value)]
    
def student_ranking(student_scores, student_names):
    ranking = []
    counter = 1
    for i, j in zip(student_scores, student_names):
        ranking.append(f'{counter}. {j}: {i}')
        counter += 1

    return ranking
    
def perfect_score(student_info):
    for i in range(0, len(student_info)):
        if student_info[i][1] == 100:
            return student_info[i]

    return []
            
