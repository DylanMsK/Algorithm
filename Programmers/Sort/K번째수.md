# K번째수


### 문제 출처
[K번째수](https://programmers.co.kr/learn/courses/30/lessons/42748)


### 풀이
```python
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]

```
