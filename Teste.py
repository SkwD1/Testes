import unittest
import Claro


class Teste(unittest.TestCase):
    def testVerificarPlano1(self):
        claro = Claro()
        claro.plano1(["50", "1024", "50"])

        self.assertTrue(Claro.plano1(["62", "1026", "51"]))
        self.assertEqual(claro.plano1(["50", "1024", "50"], "Você vai o valor padrão em R$: 50"))

        self.assertFalse(claro.plano1(["50", "1024"]))
        self.assertFalse(claro.plano1(["50", "-3"]))
        self.assertFalse(claro.plano1(["50"]))
        self.assertFalse(claro.plano1(["D", "-3"]))

    def testVerificarPlano2(self):
        claro = Claro()
        claro.plano1(["100", "2048", "100"])

        self.assertTrue(claro.plano1(["151", "2049", "102"]))
        self.assertEqual(claro.plano1(["100", "2048", "100"], "Você vai o valor padrão em R$: 80"))

        self.assertFalse(claro.plano1(["100", "2048"]))
        self.assertFalse(claro.plano1(["100", "-3"]))
        self.assertFalse(claro.plano1(["100"]))
        self.assertFalse(claro.plano1(["D", "-3"]))

    def testVerificarPlano3(self):
        claro = Claro()
        claro.plano1(["200", "4096", "200"])

        self.assertTrue(claro.plano1(["201", "4099", "267"]))
        self.assertEqual(claro.plano1(["200", "4096", "200"], "Você vai o valor padrão em R$: 120"))

        self.assertFalse(claro.plano1(["200", "4096"]))
        self.assertFalse(claro.plano1(["200", "-3"]))
        self.assertFalse(claro.plano1(["200"]))
        self.assertFalse(claro.plano1(["D", "-3"]))

if __name__ == '__main__':
    unittest.main()