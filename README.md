# ➗ Teste de Divisibilidade (Python)

Um script matemático interativo desenvolvido em Python para testar se um número (dividendo) é divisível por outro (divisor). Este projeto foca especificamente na implementação das **regras de divisibilidade matemáticas clássicas** para uma lista de divisores.

## 🚀 Divisores Suportados
O programa consegue analisar as regras de divisibilidade exatas para os seguintes divisores:
`2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `15` e `25`.

## 🧠 Destaque Algorítmico

Em vez de simplesmente usar o operador de módulo (`num % divisor == 0`) para todos os casos, este script implementa os **algoritmos matemáticos reais e teóricos** para alguns números desafiadores, como por exemplo:
- **Divisibilidade por 7:** Extrai-se o último algarismo, dobra-se o seu valor e subtrai do restante do número (excluindo a casa das unidades). O processo é repetido em loop até que reste um número fácil de verificar se é múltiplo de 7 (como 14, 21, etc).
- **Divisibilidade por 11:** Soma-se os algarismos de ordem ímpar e de ordem par separadamente. Em seguida, verifica se a diferença entre essas somas é um múltiplo de 11 (ou 0).
- **Divisibilidade por 3:** Soma contínua de todos os algarismos do número até que reste apenas uma casa decimal, verificando se o resultado é igual a 3, 6 ou 9.

## 💻 Como executar o script

Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.

1. Faça o clone do repositório:
   ```bash
   git clone https://github.com/KxuePereira/Teste-de-Divisibilidade.git
   ```
2. Abra o terminal na pasta baixada.
3. Execute o comando:
   ```bash
   python teste_divisibilidade.py
   ```
4. O programa pedirá um **Dividendo** (o número que será testado) e um **Divisor** (por quem você quer dividir, de acordo com a lista suportada). 
5. O console exibirá se a divisão é exata ou não e perguntará se você deseja fazer outro teste!

## 👨‍💻 Autor
- **Kauê Vitor Pereira Santos** 
- Exercício de lógica de programação e modelagem de algoritmos matemáticos em Python.
