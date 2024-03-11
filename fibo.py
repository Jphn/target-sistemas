from math import sqrt

def isPerfectSquare(x: int) -> bool:
    root: int = int(sqrt(x))
    
    return root * root == x
    
def isFibo(x: int) -> bool:
    return isPerfectSquare(5 * x * x + 4) or isPerfectSquare(5 * x * x - 4)

n = int(input('Digite o nº: '))
print('Pertence!' if isFibo(n) else 'Não pertence!')
