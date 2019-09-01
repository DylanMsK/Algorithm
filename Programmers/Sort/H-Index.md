# H-Index


### 문제 출처
[H-Index](https://programmers.co.kr/learn/courses/30/lessons/42747)



### 풀이
```python
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

```