# 判断点是否在三角形中
import math

def area(point1,point2,point3):
    a = math.sqrt(math.pow(point2[0]-point1[0],2)+math.pow(point2[1]-point1[1],2))
    b = math.sqrt(math.pow(point3[0]-point2[0],2)+math.pow(point3[1]-point2[1],2))
    c = math.sqrt(math.pow(point1[0]-point3[0],2)+math.pow(point1[1]-point3[1],2))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

def in_triangle(point1,point2,point3,point):
    area1 = area(point1,point2,point)
    area2 = area(point2,point3,point)
    area3 = area(point3,point1,point)
    ori_area = area(point1,point2,point3)
    return math.isclose(area1+area2+area3,ori_area)

if __name__ == '__main__':
    print(in_triangle([0,0],[10,0],[5,20],[5,19]))
    print(in_triangle([0, 0], [10, 0], [5, 20], [4, 16]))
    print(in_triangle([0, 0], [10, 0], [5, 20], [4, 16.1]))
    print(in_triangle([0, 0], [10, 0], [5, 20], [4, 19]))
    print(in_triangle([0, 0], [10, 0], [5, 20], [4, 20]))