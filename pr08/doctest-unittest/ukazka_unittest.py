'''
Created on 30.10.2012

@author: Jiri Vrany

UnitTest pro modul reseni.py ze cviceni2
'''
import unittest
import reseni_gen as reseni


class Test(unittest.TestCase):

    '''
    Testy pro druhy ukol z PJP pomoci unittest
    '''

    def test_vzor(self):
        '''
        zakladni test / vzorove reseni
        '''
        bod_a = (1, 1)
        bod_b = (3, 1)
        bod_c = (2, 2)
        bod_d = (2, 3)
        vzor = sorted((bod_a, bod_b, bod_d))
        vysledek = sorted(reseni.get_triangle(bod_a, bod_b, bod_c, bod_d))
        self.assertListEqual(
            vzor, vysledek, "vzorovy test : vzor %s vysledek %s" % (vzor, vysledek))

    def test_prekryv(self):
        '''
        Test kdy se dva body prekryvaji
        '''
        bod_a = (-2, 2)
        bod_b = (-2, 2)
        bod_c = (2, 2)
        bod_d = (0, -2)
        vzor = sorted((bod_a, bod_c, bod_d))
        vysledek = sorted(reseni.get_triangle(bod_a, bod_b, bod_c, bod_d))
        self.assertListEqual(
            vzor, vysledek, "test prekryvajicich se bodu: vzor %s vysledek %s" % (vzor, vysledek))

    def test_zapornych(self):
        ''''
        Test bodu tvoricich ctverec
        '''
        bod_a = (-2, 2)
        bod_b = (0, -2)
        bod_c = (2, 2)
        bod_d = (1, -1)
        vzor = sorted((bod_a, bod_b, bod_c))
        vysledek = sorted(reseni.get_triangle(bod_a, bod_b, bod_c, bod_d))
        self.assertListEqual(
            vzor, vysledek, "test bodu ve ctverci : vzor %s vysledek %s" % (vzor, vysledek))

    def test_hrana(self):
        '''
        Test bodu leziciho na hrane nejvetsiho trojuhelnika
        '''
        bod_a = (0, 0)
        bod_b = (1, 0)
        bod_c = (10, 0)
        bod_d = (2, 2)
        vzor = sorted((bod_a, bod_d, bod_c))
        vysledek = sorted(reseni.get_triangle(bod_a, bod_b, bod_c, bod_d))
        self.assertListEqual(
            vzor, vysledek, "test bodu na hrane : vzor %s vysledek %s" % (vzor, vysledek))

    def test_neni_trojuhelnik(self):
        '''
        prekryvaji li se vice nez dva body, trojuhelnik neexistuje
        '''
        bod_a = (0, 0)
        bod_b = (1, 1)
        bod_c = (0, 0)
        bod_d = (1, 1)
        vysledek = reseni.get_triangle(bod_a, bod_b, bod_c, bod_d)
        self.assertFalse(
            vysledek, "trojuhelnik neexistuje, fce vraci {}".format(vysledek))

if __name__ == '__main__':
    unittest.main()
