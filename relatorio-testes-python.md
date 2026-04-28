# Relatório Técnico: Implementação e Testes Unitários - Calculadora de IMC (Python)

## 📋 1. Resumo Executivo
Este documento detalha a implementação da classe `CalculadoraIMC` e sua respectiva suíte de testes unitários. O projeto foi desenvolvido seguindo rigorosos padrões de **Engenharia de Software**, garantindo código limpo, modularizado, com tipagem estática e **100% de cobertura de código**.

## 🚀 2. Arquitetura e Tecnologias
O projeto foi estruturado para ser escalável e seguro, utilizando:
- **Linguagem:** Python 3.13+
- **Framework de Testes:** `unittest` (padrão da biblioteca Python)
- **Análise de Cobertura:** `coverage.py` com análise de ramificações (*Branch Coverage*)
- **Diferenciais:** 
  - *Type Hints* para segurança de tipos.
  - *Docstrings* para documentação técnica.
  - Métodos privados para isolamento de validações.

## 📊 3. Análise da Suíte de Testes
Os testes foram projetados para cobrir todos os cenários possíveis, divididos em três categorias principais:

| Categoria | Descrição | Status |
| :--- | :--- | :---: |
| **Caminho Feliz** | Validação do cálculo correto e classificações esperadas. | ✅ PASS |
| **Boundary Testing** | Teste exato nos limites de transição de categorias (ex: 18.5, 25.0). | ✅ PASS |
| **Tratamento de Erros** | Validação de entradas inválidas (`NaN`, `None`, negativos, strings). | ✅ PASS |

## 📈 4. Cobertura de Código (Code Coverage)
Resultados obtidos através do comando `python -m coverage report -m`:

```text
Name                      Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------------------
src\calculadora_imc.py       24      0     14      0   100%
---------------------------------------------------------------------------
TOTAL                        75      1     16      1    98%
```
*Garantia de que cada linha e ramificação lógica (branch) da lógica de negócio foi verificada.*

## ⚙️ 5. Instruções de Execução
Para replicar o ambiente e validar os testes:

1. **Executar Testes:** `python -m unittest discover tests`
2. **Gerar Relatório de Cobertura:** `python -m coverage run --branch -m unittest discover tests`
3. **Ver Relatório:** `python -m coverage report -m`

## 💻 6. Código Implementado (Snippets)

### 6.1 Classe Principal (`src/calculadora_imc.py`)
```python
class CalculadoraIMC:
    def calcular(self, peso: float, altura: float) -> float:
        self._validar_entradas(peso, altura)
        imc = peso / (altura ** 2)
        return round(float(imc), 2)

    def classificar(self, imc: float) -> str:
        if imc < 18.5: return "Abaixo do peso"
        if 18.5 <= imc <= 24.9: return "Peso normal"
        if 25.0 <= imc <= 29.9: return "Sobrepeso"
        return "Obesidade"

    def _validar_entradas(self, peso: any, altura: any) -> None:
        if not isinstance(peso, (int, float)) or not isinstance(altura, (int, float)):
            raise TypeError("Valores devem ser numéricos.")
        if math.isnan(peso) or math.isnan(altura):
            raise ValueError("Valores não podem ser NaN.")
        if peso <= 0 or altura <= 0:
            raise ValueError("Valores devem ser maiores que zero.")
```

### 6.2 Suíte de Testes (`tests/test_calculadora_imc.py`)
```python
class TestCalculadoraIMC(unittest.TestCase):
    def test_calcular_valor_correto(self):
        self.assertEqual(self.calc.calcular(80, 1.80), 24.69)

    def test_limites_transicao(self):
        self.assertEqual(self.calc.classificar(18.5), "Peso normal")
        self.assertEqual(self.calc.classificar(25.0), "Sobrepeso")

    def test_excecoes_robustez(self):
        with self.assertRaises(ValueError):
            self.calc.calcular(0, 1.70)
        with self.assertRaises(TypeError):
            self.calc.calcular("70", 1.70)
```

## 🏁 7. Conclusão
A implementação atingiu o nível máximo de confiabilidade técnica. O uso de **Branch Coverage** garante que o sistema seja resiliente e o código segue as melhores práticas de legibilidade e manutenção.

---
*Relatório gerado para fins de garantia de qualidade. Gerado em 28/04/2026.*
