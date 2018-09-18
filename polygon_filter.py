from configurations import *

def test_inside_polygon():
    pol = [(1,1),(2,1),(3,1),(3,2),(3,3),(2,3),(1,3)]

    inPoint = (2,2)
    outPoint0 = (5,5)
    outPoint1 = (2,5)

    print(inside_polygon(inPoint, pol) == True)
    print(inside_polygon(outPoint0, pol) == False)
    print(inside_polygon(outPoint1, pol) == False)

def inside_polygon(p, polygon):
    """
    Reference: http://www.ariel.com.au/a/python-point-int-poly.html
    """

    x = p[0]
    y = p[1]
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


test_inside_polygon()




