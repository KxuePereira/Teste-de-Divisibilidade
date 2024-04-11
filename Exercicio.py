# //Escrever um algoritmo/programa que  receba  dois  valores  inteiros  positivos (xe y) e informarse x é divisívelpor y. Vamos focar no problema quando yé 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15 ou25.//
# Aluno: Kauê Vitor Pereira Santos


import math

def imprimirObjetivoLab():
    print("Programa TESTE DE DIVISIBILIDADE\n")
    print("O programa tem por objetivo informar se um determinado número é ou não divisível por outro.\n")
    print("Os testes de divisibilidade são válidos para os seguintes divisores: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15 e 25.\n")

def testarDivisibilidade(dividendo, divisor):
    if divisor == 2:
        return divisibilidade2(dividendo)
    elif divisor == 3:
        return divisibilidade3(dividendo)
    elif divisor == 4:
        return divisibilidade4(dividendo)
    elif divisor == 5:
        return divisibilidade5(dividendo)
    elif divisor == 6:
        return divisibilidade6(dividendo)
    elif divisor == 7:
        return divisibilidade7(dividendo)
    elif divisor == 8:
        return divisibilidade8(dividendo)
    elif divisor == 9:
        return divisibilidade9(dividendo)
    elif divisor == 10:
        return divisibilidade10(dividendo)
    elif divisor == 11:
        return divisibilidade11(dividendo)
    elif divisor == 12:
        return divisibilidade12(dividendo)
    elif divisor == 15:
        return divisibilidade15(dividendo)
    elif divisor == 25:
        return divisibilidade25(dividendo)
    else:
        return False

def divisibilidade2(num):
    if num % 2 == 0:
        return True
    else:
        return False

def divisibilidade3(num):
    soma_digitos = sum(int(digito) for digito in str(num))
    while soma_digitos > 9:
        soma_digitos = sum(int(digito) for digito in str(soma_digitos))
    if soma_digitos in [3, 6, 9]:
        return True
    else:
        return False

# Implemente as outras funções de divisibilidade da mesma maneira.

def divisibilidade4(num):
    if num % 4 == 0:
        return True
    else:
        return False

def divisibilidade5(num):
    if num % 5 == 0:
        return True
    else:
        return False

def divisibilidade6(num):
    if num % 6 == 0:
        return True
    else:
        return False

def divisibilidade7(num):
    numero = num
    while numero > 70:
        ultimo_algarismo = numero % 10
        numero = math.fabs(numero - 2 * ultimo_algarismo)
    if numero in [0, 7, 14, 21, 28, 35, 42, 49, 54, 63, 70]:
        return True
    else:
        return False

def divisibilidade8(num):
    if num % 8 == 0:
        return True
    else:
        return False

def divisibilidade9(num):
    if num % 9 == 0:
        return True
    else:
        return False

def divisibilidade10(num):
    if num % 10 == 0:
        return True
    else:
        return False

def divisibilidade11(num):
    num_str = str(num)
    pares = [int(num_str[i]) for i in range(1, len(num_str), 2)]
    impares = [int(num_str[i]) for i in range(0, len(num_str), 2)]
    diferenca = abs(sum(pares) - sum(impares))
    while diferenca > 9:
        diferenca = abs(diferenca - 9)
    if diferenca == 0:
        return True
    else:
        return False

def divisibilidade12(num):
    if num % 3 == 0 and num % 4 == 0:
        return True
    else:
        return False

def divisibilidade15(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False

def divisibilidade25(num):
    if num % 5 == 0 and (num // 5) % 5 == 0:
        return True
    else:
        return False

def main():
    imprimirObjetivoLab()
    while True:
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
        if divisor in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 25]:
            if testarDivisibilidade(dividendo, divisor):
                print(f"{dividendo} é divisível por {divisor}.")
            else:
                print(f"{dividendo} NÃO é divisível por {divisor}.")
            resposta = input("Deseja realizar novo teste (s/n)? ").lower()
            while resposta not in ['s', 'n']:
                resposta = input("Opção inválida! Deseja realizar novo teste (s/n)? ").lower()
            if resposta == 'n':
                break
        else:
            print("Divisor inválido! Favor informar novos valores.")

if __name__ == '__main__':
    main()
