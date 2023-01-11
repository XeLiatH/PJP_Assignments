def with_klasicky_priklad():
    with open('pokus.txt', 'r') as myf:
        print(myf.read())
    

        
def klasicky_zapis():
    try:
        myf = open('pokus.txt', 'r')
        myf.read()
    finally:
        myf.close()    
            

if __name__ == '__main__':
    with_klasicky_priklad()