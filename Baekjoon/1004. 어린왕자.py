# url = 'https://www.acmicpc.net/problem/1004'

def inCircle(planet, x, y):
    c1, c2, r = planet
    d = ((c1-x)**2 + (c2-y)**2)**0.5
    if d < r:
        return True
    return False

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    planets = []
    for __ in range(N):
        planets.append(tuple(map(int, input().split())))

    cnt = 0
    for planet in planets:
        if inCircle(planet, x1, y1) and inCircle(planet, x2, y2):
            continue
        elif inCircle(planet, x1, y1) or inCircle(planet, x2, y2):
            cnt += 1
        else:
            continue
    
    print(cnt)
