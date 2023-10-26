## 2. Pandas 기본
![image](https://github.com/d982h8st7/DataAnalysis/assets/50827253/eaaedd82-fec8-4015-8bef-1ea396bf164b)

Series는 라벨이 있는 1차원 배열 구조이다. 그리고 축의 이름은 **index** 이라고 명명한다.
```py
s = pd.Series(data, index=None)
```
```
0    1
1    3
2    5
3    7
4    9
dtype: int64
```
Series가 출력된 문자열을 살펴보면, 왼쪽이 index, 오른쪽이 해당 인덱스가 갖는 값이다.

![image](https://github.com/d982h8st7/DataAnalysis/assets/50827253/bb519647-6701-4bb0-be28-eff36e4d7d45)

만약 data가 ndarray(multidimensional container of items of the same type and size)라면,
index도 무조건 data랑 같은 길이가 되어야 한다. <br>
기입된 index가 없을때, [0 ... ,len(data) -1] 만큼의 값이 생성된다.

- 파이썬의 딕셔너리로 Series를 생성할수있다. 

```py
data = {
    '서울':70000,
    '부산':52000,
    '대전':35000,
    '광주':40000,
    '제주도':28000
}
s = pd.Series(data=data)
print(s)
```
```
서울     70000
부산     52000
대전     35000
광주     40000
제주도    28000
dtype: int64
```

또한, 인덱스의 순서를 지정하고 싶으면 원하는 인덱스를 리스트로 만들어 변수로 전달하면된다.
```py
data = {
    '서울':70000,
    '부산':52000,
    '대전':35000,
    '광주':40000,
    '제주도':28000
}
i = ['광주','서울','부산','대전','경기도']
s = pd.Series(data=data,index=i)
print(s)
```
```
광주     40000.0
서울     70000.0
부산     52000.0
대전     35000.0
경기도        NaN
dtype: float64
```
하지만, 예시에서 나온것과 같이 정의한 인덱스가 기존에 있던 인덱스에 존재하지않기때문에,
해당 값이 NaN으로 출력된다. <br>
이러한 값을 결측값,손실값, Null 값 등으로 부르지만 결측값이라고 통일한다.

