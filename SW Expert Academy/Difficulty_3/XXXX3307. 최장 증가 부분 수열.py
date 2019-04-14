# url = 'https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBOKg-a6l0DFAWr&categoryId=AWBOKg-a6l0DFAWr&categoryType=CODE'

def dfs(idx, nums):
    global max_, visited
    visited[idx] = 0
    for j in range(idx+1, N):
        if lst[j] >= nums[-1]:
            nums.append(lst[j])
            dfs(j, nums)
            nums.pop()
    else:
        if len(nums) > max_:
            max_ = len(nums)
        return


for tc in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    max_ = 0
    visited = [1] * N
    for i in range(N-1):
        if visited[i]:
            nums = [[i]]
            while nums:
                num = nums.pop()
                for j in range(num[-1]+1, N):
                    if lst[j] >= lst[num[-1]]:
                        visited[j] = 0
                        nums.append(num + [j])
                else:
                    if len(num) > max_:
                        max_ = len(num)
    print(f'#{tc+1} {max_}')