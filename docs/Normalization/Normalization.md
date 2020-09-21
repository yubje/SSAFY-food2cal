# Normalization

 Data Normalization 은 데이터의 범위를 사용에 용이한 범위로 제한하는 것이다. 이미지 데이터의 경우 픽셀 값의 범위가 보통 0~255 사이의 값을 가지므로, 255로 나누어 0~1.0 사이의 값을 갖게 한다.

 아주 기본적이고 중요한 개념이며, 이를 간과하면 성능에 치명적인 영향을 미치게 된다. 정규화 및 표준화는 모두 머신러닝 알고리즘을 훈련시키는데 있어서 사용되는 특성(feature)들이 모두 비슷한 영향력을 행사하도록 값을 변환해주는 작업이다.

 특성 스케일링(feature scaling) 또는 데이터 스케일링(data scaling)이라고 부른다.



- 머신러닝 알고리즘은 데이터가 가진 feature(특성)들을 비교하여 데이터의 패턴을 찾는다
- 데이터가 가진 feature의 스케일이 **심하게** 차이가 나는 경우 문제 발생
- 모든 데이터 포인트가 동일한 정도의 스케일(중요도)로 반영되도록 해주는 게 정규화(Normalization)의 목표



 이를 수식으로 표현하면,

`(정규화하고자 하는 값 - 데이터 범위의 최소값) / (데이터 범위의 최대값 - 데이터 범위의 최소값)` 으로 표현할 수 있다.



 표준화를 수식으로 표현하면,

`(표준화하고자 하는 값 - 평균) / (표준편차)`

![image-20200908113357435](Normalization.assets/image-20200908113357435.png)



## Normalization을 하는 이유?

- 신경망의 학습을 더 빨리한다.

- Lacal Optimum에 빠지는 가능성을 줄이는 등 다양한 이유가 있다.

- Gradient descent algorithm에 대해 간략히 알아보자.

  ![image-20200908112733189](Normalization.assets/image-20200908112733189.png)

  - 위 그림과 같이 지협적인 최저점을 local optimum 인데, 우리의 목적은 global optimum을 빠르게 찾는 것(학습을 빨리 하는 것)이다.

  

  ![image-20200908112913387](Normalization.assets/image-20200908112913387.png)

  
  
  - 위 그림과 같이 하나의 최저점을 가지고 있는 모양을 선호하며 이와 같은 함수로 만들어야 한다는 것이 핵심이다.



![image-20200908114545639](Normalization.assets/image-20200908114545639.png)

왼쪽 이미지는 Unnormalized, 오른쪽 이미지는 Normalized를 나타낸다. Normalization을 적용하면 좀 더 spherical contour를 가지게 되고, 이렇게 하면 Gradient Descent Algorithm으로 쉽게, 빠르게 최적화 지점을 찾을 수 있게 된다.



## Normalization의 방법

### 1. Min-Max Normalization (최소-최대 정규화)

최소-최대 정규화는 데이터를 정규화하는 가장 일반적인 방법이다. 모든 feature에 대해 **0~1 사이의 값**으로 변환하는 방법이다.



식으로 표현하면,

`(정규화하고자 하는 값 - 데이터 범위의 최소값) / (데이터 범위의 최대값 - 데이터 범위의 최소값)` 으로 나타낼 수 있다.

실제로 코드로 나타내면,

```python
def min_max_normalize(lst):
    normalized = []
    
    for value in lst:
        normalized_num = (value - min(lst)) / (max(lst) - min(lst))
        normalized.append(normalized_num)
      
   	return normalized
```

로 표현할 수 있다.

참고로, 이미지의 경우 픽셀 값이 보통 0~255 사이의 값을 갖기 때문에 255로 나누어 처리하기도 한다.



그러나, 최소-최대 정규화는 **이상치(Outlier)**에 너무 많은 영향을 받는다는 치명적인 단점이 있다. 예를 들어, 100개의 값 중 99개는 0~40 사이의 값이고, 하나의 값만 100이라면 산포도로 나타내면 다음과 같다.

![image-20200908130725246](Normalization.assets/image-20200908130725246.png)

그래프로 보는 것과 같이 x축에서 문제가 있는 것으로 보인다. 이 상태로 데이터들을 비교한다면 y축의 영향이 지배적일 수밖에 없다.



이러한 단점을 **Z-점수 정규화**를 고려하여 보완한다.



### 2. Z-Score Normalization (Z-점수 정규화)

Z-점수 정규화는 이상치(outlier) 문제를 피하는 데이터 정규화 전략이다.



식으로 나타내면 다음과 같다.

`(표준화하고자 하는 값 - 평균) / (표준편차)`



코드로 나타내면,

```python
def z_score_normalization(lst):
    normalized = []
    
    for value in lst:
        normalized_num = (value - np.mean(lst)) / np.std(lst)
        normalized.append(normalized_num)
        
    retrun normalized
```



데이터 산포도를 확인하면,

![image-20200908131429485](Normalization.assets/image-20200908131429485.png)

위 그림과 같이 여전이 데이터가 찌그러져 보이지만 어느정도 비슷한 스케일로 나타냈음을 확인할 수 있다.



이 방법 또한 반대로 정확히 동일한 척도로 정규화된 데이터를 생성하지는 않는다는 단점이 있다.



## 추가

표준화(Z) = (X - 평균) / 표준편차

- 표준화한 Z값이 ±1.96 이내 (간단히는 ±2)에 있으면 95% 신뢰구간 내에 있는 것이므로, 그 데이터만 선택하게 되면 outlier를 제거하게 된다



- 파이썬 코드

  - 1. 새 칼럼 만들어서 Z값 넣기

    ```python
    from scipy import stats
    df['Z값 넣을 new 컬럼명'] = stats.zscore(df['Z값 구할 컬럼명'])
    ```

  - Z = ±2 인 것만 남기기

    ```python
    df = df[df['Z값 넣은 new 칼럼명'].between(-2, 2)]
    ```



- **SciPy** (다양한 통계관련 도구 제공)

  http://www.scipy.org/

  ```
  pip install scipy
  ```

  - scipy.stats: 표준 연속/이산 확률 분포(집적도 함수, 샘플러, 연속 분포 함수)와 다양한 통계 테스트, 그리고 좀 더 기술적인 통계 도구

    https://docs.scipy.org/doc/scipy/reference/stats.html

  

- 표준편차

  - 편차(데이터 값과 평균과의 차이)의 제곱을 평균내서 루트 씌운것으로 `평균에서 벌어진 정도`를 의미한다



## Reference

- [데이터 정규화 참조 문서1](https://bskyvision.com/849)

- [데이터 정규화 참조 문서2](https://go-hard.tistory.com/21)
- [데이터 정규화 참조 문서3](http://hleecaster.com/ml-normalization-concept/)
- [Gradient descent algorithm 참조 문서](https://daeson.tistory.com/167)