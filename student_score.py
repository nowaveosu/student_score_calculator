import pandas as pd

#본 파이썬파일이 csv파일들과 같은 폴더안에 있어야합니다

#정답파일명을 기입하세요
df1 = pd.read_csv('정답.csv',header=None)

#학생결과표 파일명을 기입하세요
df2 = pd.read_csv('노호준.csv',header=None)

#점수계산
n = len(df1.compare(df2))
acc = 100-(n*100/360)

#결과
print('틀린갯수: ' + str(n))
print('정확도: ' + str(round(acc,3)))

#틀린 번호 확인
#print(df1.compare(df2))
