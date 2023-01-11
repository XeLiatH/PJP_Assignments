import math

class Vector:

    def __init__(self, *args):
        self._vals = list(args)

    
    def __getitem__(self, index):
        return self._vals[index]

    def __str__(self):
        return "to je tajne"    

    def __setitem__(self, index, value):
        self._vals[index] = value    
    
    def __add__(self, other):
        itera = zip(self._vals, other._vals)
        ns = tuple([x[0] + x[1] for x in itera])
        return Vector(*ns)


if __name__ == "__main__":
    x = Vector(10, 20, 30)
    y = Vector(50, 20, 5)

    x[1] = 20
    print(x[2])
    print(x)
    
    for a in x:
        print(a)

    c = x + y    
    print(c)    

    
    #x[1] = 300

    #print(x[1])    
