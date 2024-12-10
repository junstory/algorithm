def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def generate_extreme_points(x1, y1, x2, y2):
    # 선분의 시작점과 끝점을 제외한 가장 양끝 점만 반환
    dx, dy = x2 - x1, y2 - y1
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    return [(x1 + dx, y1 + dy), (x2 - dx, y2 - dy)]

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

def solve_triangle():
    data = list(map(int, input().split()))
    x1, y1, x2, y2, x3, y3 = data

    # 각 변에서 가장 멀리 떨어진 점 계산
    ab_points = generate_extreme_points(x1, y1, x2, y2)
    bc_points = generate_extreme_points(x2, y2, x3, y3)
    ca_points = generate_extreme_points(x3, y3, x1, y1)

    max_area = 0
    min_area = float('inf')
    found = False
    print(len(ab_points), len(bc_points), len(ca_points))
    # 최대 8개의 조합만 확인
    for px1, py1 in ab_points:
        for px2, py2 in bc_points:
            for px3, py3 in ca_points:
                area = triangle_area(px1, py1, px2, py2, px3, py3)
                if area > 0:  # 유효한 삼각형
                    found = True
                    max_area = max(max_area, area)
                    min_area = min(min_area, area)

    if not found:
        print(-1)
    else:
        print(max_area, min_area)

print("풀이 시작")
solve_triangle()