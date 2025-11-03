#biblioteca
import os
import math


# limpa console
def limpar():
    os.system("cls")

# funções de calculo
def quadrado(l):
    return l**2

def retangulo(b, h):
    return b*h

def triangulo(b, h):
    return (b*h)/2


def hipotenusa(c1, c2):
    return math.sqrt(c1 ** 2 + c2 **2)
    
    

# TODO: Atividade: crie uma nova função para calcular a hipotenusa do triangulo-reta
# NOTE: para calcular raiz quadrada, importe a biblioteca "math" e use função "sqrt()".




# algoritmo principal 
limpar()

while True:
   
   print("1 - calcular quadrado")
   print("2 - calcular retangulo")
   print("3 - calcule triângulo")
   print("4 - Calcular hipotenusa do triângulo retângulo")
   print("5 - sair do programa")
   opção = input("Opção desejada").strip()
   limpar()
   match opção:
       case "1":
            float(input("informe o lado do quadrado:").strip().replace(",","."))
            resultado = quadrado(1)
            limpar()
            print(f"Area do quadrado: {resultado}")
            continue
       case "2":
           b = float(input("informe a base do retangulo: ").strip().replace(",","."))
           h = float(input("informe a altura: ").strip().replace(",","."))
           resultado = retangulo(b, h)
           limpar
           print(f"Area do retangulo: {resultado}")
           continue
       case "3":
           b = float(input("informe a base do triângulo:").strip().replace(",","."))
           h = float(input("informe a altura do triãngulo:").strip().replace(",","."))
           resultado = triangulo(b, h)
           limpar()
           print(f"Área do triangulo: {resultado}")
           continue
       case "4":
            c1 = float(input("Informe o primeiro cateto: ").strip().replace(",", "."))
            c2 = float(input("Informe o segundo cateto: ").strip().replace(",", "."))
            resultado = hipotenusa(c1, c2)
            limpar()
            print(f"Hipotenusa do triângulo retângulo: {resultado}")
            continue
       case "5":
           break
       case _:
           print("opção inválida")
           continue