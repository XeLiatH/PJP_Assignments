class Foo:
    '''
    Ukazka validace dat pri vytvareni objektu
    Jestlize  'hodnota' neni kladna vyvola value error
    https://docs.python.org/3/library/functions.html#property  
    '''
    
    def __init__(self, given_value):
        '''
        given_value musi byt vetsi nez nula
        '''
        self.hodnota = None
        self.set_hodnota(given_value)

    def get_hodnota(self):
        '''
        getter pro hodnotu - vraci hodnotu
        '''
        
        return self.hodnota

    def set_hodnota(self, value):
        '''
        setter pro hodnotu - provadi validaci
        '''
        
        if (value <= 0): 
            raise ValueError("hodnota musi byt vetsi nez nula")
        
        self.hodnota = value
    
    
if __name__ == '__main__':

    T = Foo(5)
    print(T.hodnota)
    T.hodnota = -50
    print(T.hodnota)
