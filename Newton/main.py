# Defina a função h(x)
def h(x):
    return x**3 - 2*x**2 + 4

# Defina a derivada de h(x), indicada como dh(x)
def dh(x):
    return 3*x**2 - 4*x

# Implementação do método de Newton
def metodo_newton_customizado_v2(funcao, derivada, palpite_inicial, precisao=1e-3, max_iteracoes=100):
    # Inicializa o contador de iterações
    iteracao = 0

    # Inicializa a estimativa atual para a raiz
    x_atual = palpite_inicial

    # Inicializa o erro anterior com infinito positivo
    erro_anterior = float('inf')

    # Loop iterativo para o método de Newton
    while iteracao < max_iteracoes:
        # Calcula a próxima estimativa para a raiz
        x_proximo = x_atual - funcao(x_atual) / derivada(x_atual)

        # Calcula o erro entre as estimativas atual e próxima
        erro = abs(x_proximo - x_atual)

        # Imprime informações sobre a iteração atual
        print("Numero Da Iteração {}: Raiz Aproximada = {:.6f}, Valor do erro = {:.6f}".format(iteracao, x_proximo, erro))

        # Verifica se o erro está abaixo da precisão especificada
        if erro < precisao:
            return x_proximo  # Retorna a raiz aproximada

        # Atualiza a estimativa atual com a próxima estimativa
        x_atual = x_proximo

        # Incrementa o contador de iterações
        iteracao += 1

        # Verifica a não convergência comparando erros de iterações consecutivas
        if erro_anterior < erro:
            print("O método de Newton não converge para uma raiz.")
            return None

        # Atualiza o erro anterior para a próxima iteração
        erro_anterior = erro

    # Se o método não convergir dentro do número máximo de iterações, imprime uma mensagem
    print("O método de Newton não convergiu após {} iterações.".format(max_iteracoes))
    return None  # Retorna None se o método não convergir

# Palpite inicial para a raiz
palpite_inicial_v2 = 1.0

# Chama o método de Newton com a função fornecida, sua derivada e o palpite inicial
raiz_v2 = metodo_newton_customizado_v2(h, dh, palpite_inicial_v2)

# Imprime o resultado se uma raiz for encontrada
if raiz_v2 is not None:
    print("A raiz é aproximadamente:", raiz_v2)
