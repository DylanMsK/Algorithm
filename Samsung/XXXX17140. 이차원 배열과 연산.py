# url = 'https://www.acmicpc.net/problem/17140'

def custom_sort(lst):
    # print(lst)
    set_lst = list(set(lst))
    set_lst.sort(key=lambda x: lst.count(x))
    result = []
    for i in set_lst:
        if i:
            if i > 100 or lst.count(i) > 100:
                # print(set_lst)
                return None
            result.append(i)
            result.append(lst.count(i))
    return result[:100]


def c_cal():
    global arr
    brr = []
    max_ = 0
    for x in range(len(arr[0])):
        nums = []
        for y in range(len(arr)):
            nums.append(arr[y][x])
        result = custom_sort(nums)
        if not result:
            # print('????')
            return None
        if len(result) > max_:
            max_ = len(result)
        brr.append(result)
    crr = [[0]*len(brr) for _ in range(max_)]
    for y in range(len(brr)):
        for x in range(len(brr[y])):
            crr[x][y] = brr[y][x]
    return crr


def r_cal():
    global arr
    max_ = 0
    brr = []
    for row in arr:
        result = custom_sort(row)
        if not result:
            return None
        if len(result) > max_:
            max_ = len(result)
        brr.append(result)
    for row in range(len(brr)):
        if len(brr[row]) < max_:
            lack = max_ - len(brr[row])
            brr[row] += [0] * lack
    return brr


def check(arr):
    if arr[r][c] == k:
        return True
    return False


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
time = 0
while 1:
    # print(f'{time}초')
    # for i in arr:
    #     print(i)
    if len(arr) >= len(arr[0]):
        arr = r_cal()
        if not arr:
            time = -1
            break
        if check(arr):
            break
    else:
        arr = c_cal()
        if not arr:
            time = -1
            break
        if check(arr):
            break
    time += 1
print(time)


# for i in arr:
#     print(i)
# print()
# arr = c_cal()
# for i in arr:
#     print(i)
