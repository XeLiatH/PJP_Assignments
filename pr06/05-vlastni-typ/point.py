
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str((self.x, self.y))


if __name__ == '__main__':
    A = Point(1, 2)
    B = Point(2, 2)
    C = A + B
    print(C)
    mli = [A, B, C]

    s = Point(0, 0)
    for p in mli:
        s = s + p


    print(sum(mli, s))    


