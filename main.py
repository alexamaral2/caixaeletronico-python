from caixa import Caixa
c = Caixa()

def menu():
    try:
        print("\n-------Caixa-Eletrônico-----")
        print("----Selecione uma Opção-----")
        print("1- Depositar")
        print("2- Sacar")
        print("3- Consultar Saldo")
        print("4- Sobre")
        print("5- Sair")
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Opção Inválida!")
        main()
    return opcao    
       
def submenu(opcao):
    nota02 = -1
    nota05 = -1
    nota10 = -1
    nota20 = -1
    nota50 = -1
    nota100 = -1
    valorSaque = -1
    
    if opcao == 1:
        try:
            while nota02 < 0:  
                nota02 = int(input("Insira a quantidade das Notas de 2: "))
            c.set_nota2(nota02)
            c.abastecerNotas2()
            
            while nota05 < 0: 
                nota05 = int(input("Insira a quantidade das Notas de 5: "))
            c.set_nota5(nota05)
            c.abastecerNotas5()
            
            while nota10 < 0: 
                nota10 = int(input("Insira a quantidade das Notas de 10: "))
            c.set_nota10(nota10)
            c.abastecerNotas10()
            
            while nota20 < 0: 
                nota20 = int(input("Insira a quantidade das Notas de 20: "))
            c.set_nota20(nota20)
            c.abastecerNotas20()
            
            while nota50 < 0: 
                nota50 = int(input("Insira a quantidade das Notas de 50: "))
            c.set_nota50(nota50)
            c.abastecerNotas50()
            
            while nota100 < 0: 
                nota100 = int(input("Insira a quantidade das Notas de 100: "))
            c.set_nota100(nota100)
            c.abastecerNotas100()
            
            main()
        except ValueError:
            print("Valor Inválido, Tente Novamente!")
            submenu(opcao)
        
    if opcao == 2:
        while valorSaque < 0:
            try:
                valorSaque = int(input("Informe o valor do Saque: "))
            except ValueError:
                print("Valor Inválido, Tente Novamente!")
        c.set_valorsaque(valorSaque)
        c.sacarValor()
        main()
    
    if opcao == 3:
        print(f"Valor Saldo: R${c.consultarSaldo():.2f}")
        c.consultarNotas()
        main()
        
    if opcao == 4:
        print("==> Desenvolvido por Alex Jr <==")
        main()
    
    if opcao == 5:
        print("Saindo do Caixa...")
        print("Programa Encerrado!")
        exit()
    else:
        print("Opção Inválida!")
        main()   

def main():
   retornaOpcao = menu() 
   retornaSubmenu = submenu(retornaOpcao)
   return retornaSubmenu
    
if __name__ == "__main__":
    main()