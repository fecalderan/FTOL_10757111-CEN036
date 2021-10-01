# a e b são inteiros menor que 1000!
#calcular o inteiro que corresponde o quadrado da hipotenusa do triangulo retangulo com catetos a e b

import sys

##funcao que verifica se é inteiro
def inteiro(v):
    n = int(v)
    m = v * 10
    s = n * 10
    if m == s:
      return 0 ##inteiro
    else:
      return 1 ## nao inteiro


a = float(sys.argv[1]) ##primeiro argumento  passado, cateto a
b = float(sys.argv[2]) ##segundo argumento passado, cateto b

## confere se a é inteiro
if inteiro(a) == 1:
    print("Primeiro argumento nao é inteiro")
elif inteiro(b) ==1: ## confere se b é inteiro
    print("Segundo argumento nao é inteiro")
elif (a or b) >= 1000: ## se os dois forem inteiro, calcula hipotenusa
    print("um dos argumentos maior que mil")
else:
  hip = a**2+b**2 ##calcula a hipotenusa
  print("O quadrado da hipotenusa para o triangulo retângulo com lados a = {} e b = {}, é {}" .format(a,b,hip))
