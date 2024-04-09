'''
Uniguairacá Centro Universitário
Curso: Análise e Desenvolvimento de Sistemas
Desenvolvido por: Maikon Schafranski e Marlon Schafranski

Tema: O Problema das N-Rainhas
O problema das N-rainhas consiste em encontrar todas as combinações 
possíveis de N rainhas num tabuleiro de dimensão N por N tal que nenhuma
das rainhas ataque qualquer outra
'''

from collections import deque


def posicao_segura(tabuleiro, linha, coluna):
    # Verifica se é seguro colocar uma rainha nesta posição
    for i in range(linha):
        if tabuleiro[i] == coluna or abs(tabuleiro[i] - coluna) == linha - i:
            return False
    return True


def resolver_n_rainhas(n):
    # Inicializa a fila de estados com o estado inicial vazio
    fila = deque([[]])
    # Inicializa a solução como uma lista de N-None
    solucao = [None] * n

    while fila:
        # Retira o primeiro estado da fila
        estado_atual = fila.popleft()
        # Se o estado atual é um estado completo, armazena-o como a solução
        if len(estado_atual) == n:
            solucao = estado_atual
            break
        # Gera os possíveis estados sucessores e os adiciona à fila
        for coluna in range(n):
            if posicao_segura(estado_atual, len(estado_atual), coluna):
                fila.append(estado_atual + [coluna])

    return solucao if len(solucao) == n else None


def imprimir_solucao(tabuleiro):
    if tabuleiro is None:
        print("Não há solução")
    else:
        for coluna in tabuleiro:
            linha = ['-'] * len(tabuleiro)
            linha[coluna] = 'R'
            print(' '.join(linha))


def main():
    n = int(input("Digite o tamanho do tabuleiro (N): "))
    solucao = resolver_n_rainhas(n)
    print("\nSolução encontrada:")
    imprimir_solucao(solucao)


if __name__ == "__main__":
    main()
