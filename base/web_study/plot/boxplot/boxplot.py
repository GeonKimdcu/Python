"""
이상값 탐지를 위한 시각화 방법
- 히스토그램 (한 변수의 이상값 분석, 정규 분포의 양극단)
- 박스 플롯 (한 변수의 이상값 분석, 정규 분포의 양극단)
- 산점도 (두 변수의 이상값 분석)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
df_train = pd.DataFrame([
    ['A01', 2, 1, 60, 139, 'country', 0, 'fail'],
    ['A02', 3, 2, 80, 148, 'country', 0, 'fail'],
    ['A03', 3, 4, 50, 149, 'country', 0, 'fail'],
    ['A04', 5, 5, 40, 151, 'country', 0, 'pass'],
    ['A05', 7, 5, 35, 154, 'city', 0, 'pass'],
    ['A06', 2, 5, 45, 149, 'country', 0, 'fail'],
    ['A07', 8, 9, 40, 155, 'city', 1, 'pass'],
    ['A08', 9, 10, 70, 155, 'city', 3, 'pass'],
    ['A13', 90, 100, 71, 154, 'city', 2, 'pass'],  # 이상값 추가
    ['A14', 91, 101, 72, 155, 'city', 3, 'pass'],  # 이상값 추가
    ['A09', 6, 12, 55, 154, 'city', 0, 'pass']
], columns=['ID', 'hour', 'attendance', 'weight', 'iq', 'region', 'library', 'pass'])

# 데이터 분석
sns.boxplot(df_train['hour'])
plt.show()

sns.boxplot(x='hour', data = df_train)
plt.show()

sns.boxplot(y = 'hour', data = df_train)
plt.show()

sns.boxplot(data = df_train)
plt.show()

sns.boxplot(x='region', y= 'hour', data = df_train)
plt.show()

sns.boxplot(x = 'region', y = 'hour', data = df_train, hue = 'pass')
plt.show()

sns.boxplot(x = 'hour', data=df_train, hue = 'pass')
plt.show()
'''
sns.boxplot(data = df_train, hue = 'pass') #ValueError : Cannot use 'hue' without 'x'or 'y'
plt.show()
'''