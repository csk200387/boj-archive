from typing import List, Tuple

def polygon_area(vertices: List[Tuple[int, int]]) -> float:
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return round(area, 2)

vertices = []
for i in range(int(input())) :
    vertices.append(tuple(map(int, input().split())))
print(polygon_area(vertices))