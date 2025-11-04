# operador terrario
#funçao principal
def main():

#entrada de dados
    nome = input("informe seu nome: ").strip().title()
    idade = int(input("informe sua idade: ").strip())


    # operador ternário
    resultado  = " é maior de idade." if idade >= 18 else "é menor de idade"

# saída de dados
    print(f"{nome} {resultado}")

# PROTEGE Algoritimo principal 

if __name__ == "_main_":
    main()
