"""
Ukazka argumenty a super() pro volani rodicovsko tridy
"""
class Foo:
    """
    Foo Class
    """
    
    def __init__(self, value1, value2):
        # do something with the values
        print(value1, value2)

class MyFoo(Foo):
    """
    Derived from Foo
    """
    
    def __init__(self, *args, **kwargs):
        # do something else, don't care about the args
        print('do something usefull')
        super(MyFoo, self).__init__(*args, **kwargs) 
        
if __name__ == '__main__':
    F = MyFoo(10, 20)
    
    