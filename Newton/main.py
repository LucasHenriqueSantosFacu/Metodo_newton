from sympy import symbols, lambdify
import numpy as np

def substituir_sen(expressao):
    return expressao.replace("sen", "sin")

def metodo_newton(expressao_funcao, expressao_derivada, ponto_inicial, precisao, max_iteracoes):
    x = symbols('x')
    funcao_expr = lambdify(x, expressao_funcao, 'numpy')
    derivada_expr = lambdify(x, expressao_derivada, 'numpy')

    for i in range(1, max_iteracoes + 1):
        # faz o primeiro cálculo
        valor_funcao = funcao_expr(ponto_inicial)
        # faz o segundo cálculo
        derivada_funcao = derivada_expr(ponto_inicial)

        if derivada_funcao == 0:
            print("A derivada é zero. O método não converge.")
            return

        ponto_proximo = ponto_inicial - valor_funcao / derivada_funcao
        erro = np.abs((ponto_proximo - ponto_inicial) / ponto_proximo)

        print(f"Iteração {i} - Ponto Inicial: {ponto_inicial:.6f}, Ponto Encontrado: {ponto_proximo:.6f}, Erro: {erro:.6f}")

        if erro < precisao:
            print("Convergência alcançada.")
            return

        ponto_inicial = ponto_proximo

    print("Número máximo de iterações alcançado. A solução pode não ter convergido.")

if __name__ == "__main__":
    expressao_funcao = substituir_sen(input("Digite a expressão da função (use 'x' como variável, ^ substitua por **, escreva completo as multiplicações,segue um exemplo para uso: 4x ficaria 4*x.): "))
    expressao_derivada = substituir_sen(input("Digite a expressão da derivada (use 'x' como variável, ^ substitua por **, escreva completo as multiplicações, segue um exemplo para uso: 4x ficaria 4*x.): "))
    ponto_inicial = float(input("Digite o ponto inicial: "))
    precisao = float(input("Digite a precisão: ").replace(',', '.'))  # Substituir ',' por '.' no valor de precisão
    max_iteracoes = int(input("Digite a quantidade máxima de iterações: "))

    metodo_newton(expressao_funcao, expressao_derivada, ponto_inicial, precisao, max_iteracoes)

