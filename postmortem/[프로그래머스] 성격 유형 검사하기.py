def solution(survey, choices):
    answer = 'RCJA'
    choices = [i-4 for i in choices]
    mbti = {'R':0,'C':0,'J':0,'A':0,
            'T':0,'F':0,'M':0,'N':0}

    for idx, p in enumerate(choices):
        if p>0: mbti[survey[idx][1]] += p
        else : mbti[survey[idx][0]] += abs(p)

    if mbti['R'] < mbti['T'] : answer = answer.replace('R','T')
    if mbti['C'] < mbti['F'] : answer = answer.replace('C','F')
    if mbti['J'] < mbti['M'] : answer = answer.replace('J','M')
    if mbti['A'] < mbti['N'] : answer = answer.replace('A','N')

    return answer