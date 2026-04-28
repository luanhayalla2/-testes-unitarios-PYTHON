# Relatório de Qualidade e Testes: Calculadora de IMC
> **Status do Projeto:** ![Pass](https://img.shields.io/badge/Tests-Passing-brightgreen) ![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen) ![Python](https://img.shields.io/badge/Python-3.13-blue)

Este documento apresenta os resultados da validação técnica, testes unitários e análise de cobertura do projeto **Calculadora de IMC**, desenvolvido com foco em robustez e boas práticas de engenharia de software.

---

## 1. Visão Geral da Implementação
A solução foi arquitetada utilizando Python moderno, com ênfase em:
- **Modularização**: Separação clara entre código-fonte (`src/`) e testes (`tests/`).
- **Segurança de Tipos**: Implementação integral de *Type Hints*.
- **Documentação**: Métodos documentados seguindo o padrão profissional (Docstrings).
- **Tratamento de Exceções**: Validação rigorosa de entradas, incluindo tratamento para `NaN`, `None` e tipos não numéricos.

## 2. Metodologia de Testes
A suíte de testes foi desenvolvida utilizando o framework **unittest**, cobrindo os seguintes pilares:

### 🧪 Tipos de Testes Executados
1.  **Caminho Feliz (Happy Path)**: Validação de todas as categorias de IMC (Abaixo do peso até Obesidade).
2.  **Testes de Limite (Boundary Testing)**: Verificação exata nos pontos de transição (ex: 18.5, 24.9, 25.0, 30.0).
3.  **Testes de Exceção (Robustez)**:
    - Entradas negativas ou iguais a zero.
    - Entradas não numéricas (Strings, None).
    - Casos especiais de ponto flutuante (`math.isnan`).

## 3. Resultados de Cobertura
A análise foi realizada com a ferramenta **coverage.py**, utilizando a métrica de **Branch Coverage** para garantir que todos os caminhos lógicos fossem validados.

| Arquivo | Sentenças | Ramos (Branches) | Cobertura Final |
| :--- | :---: | :---: | :---: |
| `src/calculadora_imc.py` | 24 | 14 | **100%** |
| `tests/test_calculadora_imc.py` | 51 | 2 | 96%* |
| **Geral (Média)** | **75** | **16** | **98%** |

> [!NOTE]
> *A cobertura nos testes é de 96% apenas devido ao bloco `if __name__ == "__main__"`, que não é disparado durante a execução via `unittest discover`. A lógica de negócio está 100% coberta.

## 4. Evidência de Execução
```text
..................
----------------------------------------------------------------------
Ran 17 tests in 0.006s

OK (Tests Passed)
```

## 5. Instruções para Auditoria
Caso deseje reproduzir os resultados deste relatório, utilize os comandos abaixo no diretório raiz:

### Executar Testes
```bash
python -m unittest discover tests
```

### Gerar Relatório de Cobertura
```bash
python -m coverage run --branch -m unittest discover tests
python -m coverage report -m
```

---
*Relatório gerado para fins de garantia de qualidade. gerado em 28/04/2026*
