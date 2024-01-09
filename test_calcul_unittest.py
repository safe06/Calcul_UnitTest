import unittest

# import la classe calcul
from calcul import Calcul

#classe de tests héritant de unittest.TestCase
class TestCalcul(unittest.TestCase) :

    #méthode de configuration exécutée avant chaque test
    def setUp(self) :
        #initialisation des ressources nécessaires pour les tests
        self.calc = Calcul()

    #test addition
    def test_additionner(self):
        resultat = self.calc.additionner(3, 5)
        #verifier si le resultat est égal à 8
        self.assertEqual(resultat, 8)
        
    #test de soustraction 
    def test_soustraire(self):
        resultat = self.calc.soustraire(8, 5)
        self.assertEqual(resultat, 3)

    #test de multiplication 
    def test_multiplier(self):
        resultat = self.calc.multiplier(6, 4)
        self.assertEqual(resultat, 24)

    #test de division
    def test_divisier(self):
        resultat = self.calc.diviser(35, 7)
        self.assertEqual(resultat, 5)
    
    #test division par zéro
    def test_diviserParZero(self):
        resultat = self.calc.diviser(54, 0)
        self.assertEqual(resultat, "Division par zéro impossible")

    # # version 2 de division par 0
    # # Test de division par zéro
    # def test_diviser_par_zero(self):
    #     with self.assertRaises(ZeroDivisionError, msg="Division par zéro impossible"):
    #                 self.calc.diviser(5, 0)


#exécuter les tests si le script est exécuté directement
if __name__ == '__main__' :
    unittest.main()
        