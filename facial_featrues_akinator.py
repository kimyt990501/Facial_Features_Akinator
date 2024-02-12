#%%
import random
import numpy as np
import pandas as pd

questions = {
    1: '이 사람의 키가 큰 편인가요?',
    2: '이 사람의 눈 사이 간격이 넓은 편인가요?',
    3: '이 사람의 눈이 가로로 큰 편인가요?',
    4: '이 사람의 눈이 세로로 큰 편인가요?',
    5: '이 사람의 코가 넓은 편인가요?',
    6: '이 사람의 입이 큰 편인가요?',
    7: '이 사람의 입술이 두꺼운 편인가요?',
    8: '이 사람의 포지션이 포수인가요?',
    9: '이 사람의 포지션이 투수인가요?',
    10: '이 사람의 포지션이 외야수인가요?',
    11: '이 사람의 포지션이 내야수인가요?',
}

df = pd.read_csv('C:\\Users\\user\\Desktop\\github_repo\\Facial_Features_Akinator\\data\\samsung_facialfeatures.csv', encoding='euc-kr')

# 빈 리스트를 만들어 결과를 저장할 준비
persons = []

# 각 속성마다 기준 값을 정해 각각 1 0.75 0.5 0.25 0 의 값을 할당
def set_data(part, val, sorted):
    if val > sorted[part * 4]:
        return 1
    elif val > sorted[part * 3]:
        return 0.75
    elif val > sorted[part * 2]:
        return 0.5
    elif val > sorted[part]:
        return 0.25
    else:
        return 0

# 데이터 프레임을 5구간으로 나누기 위한 변수
part = int(len(df) / 5)

# 각 행을 순회하면서 딕셔너리로 변환 후 리스트에 추가
for index, row in df.iterrows():
    person = {'name': row['name'], 'answers': {}}
    for i in range(2, 13):
        if i < 9:
            person['answers'][i - 1] = set_data(part, row[i], sorted(df[df.columns[i]]))
        else:
            person['answers'][i - 1] = row[i]
    persons.append(person)

#print(persons)

# 베이즈 정리 적용

questions_so_far = []
answers_so_far = []


def calculate_person_probability(person, questions_so_far, answers_so_far):
    
    # 사전 확률 (Prior)
    P_person = 1 / len(persons)

    # 가능도 (Likelihood)
    P_answers_given_person = 1
    P_answers_given_not_person = 1
    for question, answer in zip(questions_so_far, answers_so_far):
        P_answers_given_person *= max(
            1 - abs(answer - person_answer(person, question)), 0.01)

        P_answer_not_person = np.mean([1 - abs(answer - person_answer(not_person, question))
                                          for not_person in persons
                                          if not_person['name'] != person['name']])
        P_answers_given_not_person *= max(P_answer_not_person, 0.01)

    # 증거 (Evidence)
    P_answers = P_person * P_answers_given_person + \
        (1 - P_person) * P_answers_given_not_person

    # 베이즈 정리 (Bayes Theorem)
    P_person_given_answers = (
        P_answers_given_person * P_person) / P_answers

    return P_person_given_answers


def person_answer(person, question):
    if question in person['answers']:
        return person['answers'][question]
    return 0.5

def calculate_probabilites(questions_so_far, answers_so_far):
    probabilities = []
    for person in persons:
        probabilities.append({
            'name': person['name'],
            'probability': calculate_person_probability(person, questions_so_far, answers_so_far)
        })

    return probabilities

def main():
    global questions_so_far, answers_so_far

    while True:
        questions_left = list(set(questions.keys()) - set(questions_so_far))
        if len(questions_left) == 0:
            result = sorted(
                calculate_probabilites(questions_so_far, answers_so_far),
                key=lambda p: p['probability'], reverse=True
            )[0]
            print(f'당신이 보고있는 인물은 {result["name"]}입니다!')
            break
        else:
            next_question = random.choice(questions_left)
            print(questions[next_question])
            #print('당신의 답을 입력하세요:')
            choice = int(input('1. 예 2. 아니오 3. 모르겠어요 4. 그럴겁니다 5. 아닐겁니다 : '))
            if choice == 1:
                answer = 1
            elif choice == 2:
                answer = 0
            elif choice == 3:
                answer = 0.5
            elif choice == 4:
                answer = 0.75
            elif choice == 5:
                answer = 0.25
            questions_so_far.append(next_question)
            answers_so_far.append(answer)


if __name__ == '__main__':
    main()
# %%
