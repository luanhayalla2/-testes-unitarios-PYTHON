import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Instancia a calculadora antes de cada teste."""
        self.calc = Calculadora()

    # Testes de Adição
    def test_adicao_positivos(self):
        self.assertEqual(self.calc.adicao(2, 3), 5)
    
    def test_adicao_negativos(self):
        self.assertEqual(self.calc.adicao(-2, -3), -5)

    # Testes de Subtração
    def test_subtracao_comum(self):
        self.assertEqual(self.calc.subtracao(10, 4), 6)
    
    def test_subtracao_resultado_negativo(self):
        self.assertEqual(self.calc.subtracao(5, 10), -5)

    # Testes de Multiplicação
    def test_multiplicacao_comum(self):
        self.assertEqual(self.calc.multiplicacao(4, 3), 12)
    
    def test_multiplicacao_por_zero(self):
        self.assertEqual(self.calc.multiplicacao(5, 0), 0)

    # Testes de Divisão
    def test_divisao_exata(self):
        self.assertEqual(self.calc.divisao(10, 2), 5)
    
    def test_divisao_decimal(self):
        self.assertEqual(self.calc.divisao(5, 2), 2.5)

    def test_divisao_por_zero(self):
        """Verifica se lança ValueError ao dividir por zero."""
        with self.assertRaises(ValueError) as context:
            self.calc.divisao(10, 0)
        self.assertEqual(str(context.exception), "Divisão por zero não é permitida")

if __name__ == '__main__':
    unittest.main()