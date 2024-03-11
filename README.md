# Target Sistemas

Resolução dos problemas apresentados no teste para vaga da Target Sistemas.

## Problemas

### 1 - Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?

**Resolução:** O valor será 91 (1 + 2 + ... + 12 + 13). Pois o K é incrementado e logo em seguida o valor é adicionado à variável soma. [Código implementado em _Python_](./sum.py).

### 2 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

> **IMPORTANTE:** Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

**Resolução:** Por meio da expressão _5 × n² + 4_ ou _5 × n² - 4_, é possível determinar se um número pertence ou não à sequência de Fibonacci. [Implementação da resolução em _Python_](./fibo.py).

```py
from math import sqrt

def isPerfectSquare(x: int) -> bool:
    root: int = int(sqrt(x))
    
    return root * root == x
    
def isFibo(x: int) -> bool:
    return isPerfectSquare(5 * x * x + 4) or isPerfectSquare(5 * x * x - 4)

n = int(input('Digite o nº: '))
print('Pertence!' if isFibo(n) else 'Não pertence!')
```

### 3 - Descubra a lógica e complete o próximo elemento:

a. 1, 3, 5, 7, \_\_\_
b. 2, 4, 8, 16, 32, 64, \_\_\_\_
c. 0, 1, 4, 9, 16, 25, 36, \_\_\_\_
d. 4, 16, 36, 64, \_\_\_\_
e. 1, 1, 2, 3, 5, 8, \_\_\_\_
f. 2,10, 12, 16, 17, 18, 19, \_\_\_\_

**Resolução:**

a. 1, 3, 5, 7, 9 (Sequência dos ímpares)
b. 2, 4, 8, 16, 32, 64, 128 (Número anterior vezes 2)
c. 0, 1, 4, 9, 16, 25, 36, 49 (Número anterior somado com o anterior enésimo número ímpar)
d. 4, 16, 36, 64, 100 (Quadrado dos múltiplos de 2)
e. 1, 1, 2, 3, 5, 8, 13 (Fibonacci)
f. 2, 10, 12, 16, 17, 18, 19, 200 (Números que iniciam com a letra D)


### 4 - Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

**Resolução:**

Passos (assumindo que as posições dos interruptores têm a mesma ação para cada um):

1. Inicialmente, eu iria colocar todos no mesmo estado (desligados)
2. Ligaria o interruptor A
3. Aguardaria alguns minutos
4. Desligaria o A
5. Ligaria o B

Assumindo que todas estariam desligadas após o passo 1, eu iria me basear nas seguintes condições, se a lâmpada estivesse acessa significa que o interruptor B a controla, se estivesse desligada eu iria verificar sua temperatura, se estivesse quente significa que a lâmpada é controlada pelo interruptor A, e se estiver fria é controlada pelo interruptor C. Com estas 3 condições é capaz de descobrir qual controla qual com apenas duas idas.

### 5 - Escreva um programa que inverta os caracteres de um string.

> **IMPORTANTE:** a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; b) Evite usar funções prontas, como, por exemplo, reverse;

> NÃO SE ESQUEÇA DE INSERIR O LINK DO SEU REPOSITÓRIO NO GITHUB COM O CÓDIGO FONTE QUE VOCÊ DESENVOLVEU .

**Resolução:** Percorrendo o vetor de caracteres da string de trás para frente é possível reescrevê-lo ao contrário. [Implementação em _Python_](./reverse.py).

```py
text = input('Seu texto: ')
reversedText = ''

for l in range(len(text), 0, -1):
    reversedText += text[l - 1]
    
print(reversedText)
```
