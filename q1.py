from math import pi, cos, sin, tan, sqrt, acos
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.x2, self.x3 = x1, x2, x3
        self.y1, self.y2, self.y3 = y1, y2, y3

    def edges(self):
        e1 = sqrt((self.x2-self.x3)**2+(self.y2-self.y3)**2)
        e2 = sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
        e3 = sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2)
        return (e1, e2, e3)
    
    def perimeter(self):
        (a,b,c) = self.edges()
        return a + b + c
    
    def area(self):
        (a,b,c) = self.edges()
        s = (a + b + c) / 2
        triangleArea = sqrt(s * (s - a) * (s - b) * (s - c))
        return triangleArea
    
    def angles(self):
        (a,b,c) = self.edges()
        cosA = (b**2 + c**2 - a**2) / (2 * b * c)
        cosB = (a**2 + c**2 - b**2) / (2 * a * c)
        cosC = (a**2 + b**2 - c**2) / (2 * a * b)
        anglesA = acos(cosA) / pi * 180
        anglesB = acos(cosB) / pi * 180
        anglesC = acos(cosC) / pi * 180
        return (anglesA, anglesB, anglesC)

if (__name__ == '__main__'):
    tr1 = Triangle(0, 0, 0, 3, 4, 0)
    tr2 = Triangle(0, 0, 1, 0, 0, 1)
    # ---------- 1st triangle ---------- #
    print("3 edges of the 1st triangle is: ", tr1.edges())
    print("perimeter of the 1st triangle is: ", tr1.perimeter())
    print("area of the 1st triangle is: ", tr1.area())
    print("3 angles of the 1st triangle is: ", tr1.angles())
    print("")
    # ---------- 2st triangle ---------- #
    print("3 edges of the 2st triangle is: ", tr2.edges())
    print("perimeter of the 2st triangle is: ", tr2.perimeter())
    print("area of the 2st triangle is: ", tr2.area())
    print("3 angles of the 2st triangle is: ", tr2.angles())