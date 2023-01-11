import random
import time

names = ['Karel', 'Pepa', 'Nick', 'John', 'Kuchio', 'Tom']
sports = ['fotbal', 'ragby', 'tenis', 'cyklistika', 'judo', 'lyzovani']

def person_list(num_persons):
    result = [{'id': i, 'jmeno': random.choice(names), 'sport': random.choice(sports)} for i in range(num_persons)]
    return result

def person_generator(num_persons):
    result = ({'id': i, 'jmeno': random.choice(names), 'sport': random.choice(sports)} for i in range(num_persons))
    return result    

if __name__ == '__main__':
    T1 = time.clock()
    PERSONS = person_list(1000000)
    #PERSONS = person_generator(1000000)
    T2 = time.clock()
    [print(person['id']) for person in PERSONS if person['jmeno'] == 'Pepa' and person['sport'] == 'lyzovani']
    
    print("trvalo to {} sec.".format(T2-T1))
    