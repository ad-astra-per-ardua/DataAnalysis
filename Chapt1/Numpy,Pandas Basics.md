## 1. 넘파이 기본.
1.1 기본 배열 생성 : array()

파이선의 리스트처럼 순차형 객체를 넘겨받고 넘겨받은 데이터를 포함한 새로운 넘파이 배열을 생성한다.
```py
data1 = [5,9,2.5,3,1]
array1 = np.array(data1)
print(array1)
```
```
[5.  9.  2.5 3.  1. ]
```
```py
print(array1.dtype)
float64
```
* 2.5때문에 float형이므로 전체가 float형으로 출력.<br><br>

같은 길이의 리스트를 포함한 순차 데이터는 리스트 수와 동일한 다차원의 배열로 변환한다.

```py
data1 = [[1,3,5,7,9],[2,4,6,8,10]]
array1 = np.array(data1)
print(array1)
print(array1.dtype)
```
```
[[ 1  3  5  7  9]
 [ 2  4  6  8 10]]
int32
```
*마찬가지로 array안의 요소들이 전부 Integer이기 때문에 자료형은 int32이다.

array를 만들때 사용했던 data에 담긴 리스트 수를 추론하여 2차원 형태로 생성되었음.

```py
data1 = [[1,3,5,7,9],[2,4,6,8,10]]
array1 = np.array(data1)
print(array1.ndim)
print(array1.shape)
```
```
2
(2, 5)
```
- object.ndim = 객체가 몇 차원인지 return <br>
- object.shape = 객체가 (몇행, 몇열) 인지 return

```py
array1 = np.zeros(shape=10,dtype=numpy.int64,order='c')
print(array1)
```
```
[0 0 0 0 0 0 0 0 0 0]
```
내용이 0으로 채워진 여러가지 모양이나 형식으로 정의된 배열.
- zeros(shape, dtype, order, like=None)
  - shape = 행과 열 정의 수 하나만 입력시 1행 N열로 정의.
  (X,Y) 입력시 X행 Y열로 정의. + (Z ,X, Y) 입력시 (X,Y)모양의 0으로 채운 행렬을 Z개의 면 생성 이라는 의미가 되므로 3차원의 배열을 생성.
```py
array1 = np.zeros(shape=(2,5,10),dtype=np.int64,order='c')
print(array1)

[[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]

[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]]
```
  - dtype = Data Type 정의. 기본값은 float64 바꾸고싶다면, dtype = numpy.int64 이런식으로 정의 해주면됨.
  - order = 다차원 배열의 데이터가 메모리에 어떻게 저장될 것인지를 지정. C는 C언어 style로 행 기반 순서로 같은 행끼리 메모리에 저장.
  F는 Fortran style로 열 기반 순서로 같은 열끼리 메모리에 저장.

numpy.arange는 list comprehension for loop range랑 똑같다.

### 통계 관련 함수
- len() : 데이터의 총 개수 반환(행의 개수)
- mean() : 데이터 표본의 평균을 계산. array.mean과 같은 형식으로 입력해도 동일하다.
- median() : 데이터를 정렬했을 때 가운데에 위치한 수 , 즉 중앙값을 구한다.
  데이터 수가 짝수면 가운데 있는 2개 수의 평균값을 사용한다.
- var() : 데이터와 표본평균 간의 거리의 제곱의 평균값인 **표본분산**을 구한다. 분모의 기본값은 N이다
- std() : abs(sqrt(var())) 즉 표본분산의 양의 제곱근 값인 표준편차를 구한다. 분모의 기본값은 N이다.
- min() : 최솟값.
- max() : 최댓값.
- sum() : 배열전체 혹은 특정 조건을 기준으로 한 모든 원소의 합을 계산하는 함수.
- cumsum() : 원소의 누적합의 배열을 반환.
- cumprod() : 원소의 누적곱의 배열을 반환. 일정기준이상으로 커지면 Overflow로 0을 반환
- percentile(param=array_like, param=array_like of float(0~100) , axis= int, tuple of int ... )
  : 

