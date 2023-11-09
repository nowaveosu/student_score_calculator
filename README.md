## 학생 과제 채점 프로그램 제작


![스크린샷 2023-11-09 오후 7 12 11](https://github.com/nowaveosu/student_score_calculator/assets/82007474/1eb5eba7-091d-4daa-9dd0-cd73b69cb2d5)

#### 교수님께서 갖고계신 모션인식 데이터를 학생들이 과제로 해 온 AI모델로 적용시킨 csv파일을 정답이 적혀있는 csv파일과 비교하는 코드가 필요했다.
#### 교수님께서 요청하신 Python으로 csv파일을 비교하는 코드를 최대한 간결하고 투명하게 작성하였다.

```python
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
```
