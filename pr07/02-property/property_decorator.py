class Foo:
    '''
    Ukazka validace dat pri vytvareni objektu
    
    Jestlize  'hodnota' neni kladna vyvola value error  

    viz: https://docs.python.org/3/library/functions.html#property
    '''
    
    def __init__(self,  value):
        '''
        'hodnota' musi byt vetsi nez nula
        '''
        
        self._hodnota = None
        self.hodnota = value
        
    @property
    def hodnota(self):
        '''getter pomoci dekoratoru'''
        
        return self._hodnota

    @hodnota.setter
    def hodnota(self, value):
        '''setter pomoci dekoratoru'''
        
        if not (value > 0): 
            raise ValueError("hodnota musi byt vetsi nez nula")
        
        self._hodnota = value

if __name__ == '__main__':

    T = Foo(4)
    print(T.hodnota)
    T.hodnota = 6
    print(T.hodnota)
    