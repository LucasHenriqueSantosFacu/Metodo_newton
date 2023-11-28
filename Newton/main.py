from sympy import symbols, lambdify
import numpy as np


def substituir_sen(expressao):
    # Substitui 'sen' por 'sin' na expressão
    return expressao.replace("sen", "sin")


def metodo_newton(expressao_funcao, expressao_derivada, ponto_inicial, precisao, max_iteracoes):
    # Símbolo de variável
    x = symbols('x')

    # Converte a expressão da função para uma função numérica
    funcao_numerica = lambdify(x, expressao_funcao, 'numpy')
    # Converte a expressão da derivada para uma função numérica
    derivada_numerica = lambdify(x, expressao_derivada, 'numpy')

    for i in range(1, max_iteracoes + 1):
        # Calcula o valor da função no ponto atual
        valor_funcao = funcao_numerica(ponto_inicial)
        # Calcula o valor da derivada no ponto atual
        derivada_funcao = derivada_numerica(ponto_inicial)

        if derivada_funcao == 0:
            # Se a derivada é zero, o método não converge
            print("A derivada é zero. O método não converge.")
            return

        # Calcula o próximo ponto usando o método de Newton
        ponto_proximo = ponto_inicial - valor_funcao / derivada_funcao
        # Calcula o erro relativo
        erro = np.abs((ponto_proximo - ponto_inicial) / ponto_proximo)

        # Exibe informações sobre a iteração atual
        print(
            f"Iteração {i} - Ponto Inicial: {ponto_inicial:.6f}, Ponto Encontrado: {ponto_proximo:.6f}, Erro: {erro:.6f}")

        if erro < precisao:
            # Se o erro é menor que a precisão desejada, a convergência é alcançada
            print("Convergência alcançada.")
            return

        # Atualiza o ponto inicial para o próximo ponto
        ponto_inicial = ponto_proximo

    # Se o número máximo de iterações for atingido sem convergência, exibe uma mensagem
    print("Número máximo de iterações alcançado. A solução pode não ter convergido.")


if __name__ == "__main__":
    # Solicita as expressões da função e da derivada ao usuário
    expressao_funcao = substituir_sen(input(
        "Digite a expressão da função (use 'x' como variável, ^ substitua por **, escreva completo as multiplicações,segue um exemplo para uso: 4x ficaria 4*x.): "))
    expressao_derivada = substituir_sen(input(
        "Digite a expressão da derivada (use 'x' como variável, ^ substitua por **, escreva completo as multiplicações, segue um exemplo para uso: 4x ficaria 4*x.): "))

    # Solicita os parâmetros iniciais ao usuário
    ponto_inicial = float(input("Digite o ponto inicial: "))
    precisao = float(input("Digite a precisão: ").replace(',', '.'))  # Substituir ',' por '.' no valor de precisão
    max_iteracoes = int(input("Digite a quantidade máxima de iterações: "))

    # Chama a função do método de Newton com os parâmetros fornecidos
    metodo_newton(expressao_funcao, expressao_derivada, ponto_inicial, precisao, max_iteracoes)
