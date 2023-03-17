class Caixa:
    def __init__(self,nota2 = 0 ,nota5 = 0 ,nota10 = 0 ,nota20 = 0 ,nota50 = 0 ,nota100 = 0, qtdnota2 = 0,qtdnota5 = 0,
                 qtdnota10 = 0 ,qtdnota20 = 0 ,qtdnota50 = 0 ,qtdnota100 = 0 , saldo = 0 , valorsaque = 0):
        self.__nota2 = nota2
        self.__nota5 = nota5
        self.__nota10 = nota10
        self.__nota20 = nota20
        self.__nota50 = nota50
        self.__nota100 = nota100
        self.__qtdnota2 = qtdnota2
        self.__qtdnota5 = qtdnota5
        self.__qtdnota10 = qtdnota10
        self.__qtdnota20 = qtdnota20
        self.__qtdnota50 = qtdnota50
        self.__qtdnota100 = qtdnota100
        self.__saldo = saldo
        self.__valorsaque = valorsaque 
        
        @property
        def nota2():
            return self.__nota2
        
        @property
        def nota5():
            return self.__nota5
        @property
        def nota10():
            return self.__nota10
        @property
        def nota20():
            return self.__nota20
        @property
        def nota50():
            return self.__nota50
        @property
        def nota100():
            return self.__nota100
        
        @property
        def qtdnota2():
            return self.__qtdnota2
        
        @property
        def qtdnota5():
            return self.__qtdnota5
        @property
        def qtdnota10():
            return self.__qtdnota10
        @property
        def qtdnota20():
            return self.__qtdnota20
        @property
        def qtdnota50():
            return self.__qtdnota50
        @property
        def qtdnota100():
            return self.__qtdnota100
        
        @property
        def saldo():
            return self.__saldo
        
        @property
        def valorsaque():
            return self.__valorsaque

    def set_nota2(self,nota2):
        self.__nota2 = nota2
    
    def set_nota5(self,nota5):
        self.__nota5 = nota5
        
    def set_nota10(self,nota10):
        self.__nota10 = nota10
    
    def set_nota20(self,nota20):
        self.__nota20 = nota20
    
    def set_nota50(self,nota50):
        self.__nota50 = nota50
    
    def set_nota100(self,nota100):
        self.__nota100 = nota100
    
    def set_valorsaque(self,valorsaque):
        self.__valorsaque = valorsaque
               
    def abastecerNotas2(self):
        self.__qtdnota2 += self.__nota2
        return self.__qtdnota2
     
    def abastecerNotas5(self):
        self.__qtdnota5 += self.__nota5
        return self.__qtdnota5
    
    def abastecerNotas10(self):
        self.__qtdnota10 += self.__nota10
        return self.__qtdnota10
        
    def abastecerNotas20(self):
        self.__qtdnota20 += self.__nota20
        return self.__qtdnota20
        
    def abastecerNotas50(self):
        self.__qtdnota50 += self.__nota50
        return self.__qtdnota50
    
    def abastecerNotas100(self):
        self.__qtdnota100 += self.__nota100
        return self.__qtdnota100
        
    def consultarSaldo(self):
        valorSaldo = ((self.__qtdnota2 * 2) + (self.__qtdnota5 * 5) + (self.__qtdnota10 * 10) + (self.__qtdnota20 * 20) + (self.__qtdnota50 * 50) + (self.__qtdnota100 * 100))
        return valorSaldo
        
    def consultarNotas(self):
         print(f"Notas de 100: {self.__qtdnota100}, Notas de 50: {self.__qtdnota50}, Notas de 20: {self.__qtdnota20}") 
         print(f"Notas de 10: {self.__qtdnota10}, Notas de 5: {self.__qtdnota5}, Notas de 2: {self.__qtdnota2}")
    
   
    def extrairCedulas(self,vSaque,valorNota,qtdNota):
            cNota = vSaque // valorNota
            if valorNota != 2:
                if cNota > qtdNota:
                    nota_utilizada = qtdNota
                else:
                    nota_utilizada = cNota
                return nota_utilizada
            else:
                if cNota > qtdNota:
                    #print("Não há caixa suficiente para esse valor!")
                    return 0
                else:
                    nota_utilizada = cNota
                    return nota_utilizada  

    def sacarValor(self):
        qtdNota100v = self.__qtdnota100
        qtdNota50v = self.__qtdnota50
        qtdNota20v = self.__qtdnota20
        qtdNota10v = self.__qtdnota10
        qtdNota5v = self.__qtdnota5
        qtdNota2v = self.__qtdnota2
        
        valorSaque = self.__valorsaque
        qtdNota100 = self.__qtdnota100
        qtdNota50 = self.__qtdnota50
        qtdNota20 = self.__qtdnota20
        qtdNota10 = self.__qtdnota10
        qtdNota5 = self.__qtdnota5
        qtdNota2 = self.__qtdnota2

        if self.consultarSaldo() >= self.__valorsaque:

            cem = self.extrairCedulas(valorSaque, 100 , qtdNota100)
            valorSaque = valorSaque - (cem *100)
            self.__qtdnota100 -= cem
          
            cinquenta = self.extrairCedulas(valorSaque, 50 , qtdNota50)
            valorSaque = valorSaque -(cinquenta *50)
            self.__qtdnota50 -= cinquenta

            vinte = self.extrairCedulas(valorSaque, 20 , qtdNota20)
            valorSaque = valorSaque -(vinte *20)
            self.__qtdnota20 -= vinte

            dez = self.extrairCedulas(valorSaque, 10 , qtdNota10)
            valorSaque =valorSaque -(dez *10)
            self.__qtdnota10 -= dez

            cinco = self.extrairCedulas(valorSaque, 5 , qtdNota5)
            valorSaque = valorSaque -(cinco *5)
            self.__qtdnota5 -= cinco

            dois = self.extrairCedulas(valorSaque, 2 , qtdNota2)
            valorSaque = valorSaque -(dois *2)
            self.__qtdnota2 -= dois
                
            if valorSaque != 0:
                print("Não Há Notas Suficientes em Caixa!")
                self.__qtdnota100 = qtdNota100v
                self.__qtdnota50 = qtdNota50v
                self.__qtdnota20 = qtdNota20v
                self.__qtdnota10 = qtdNota10v
                self.__qtdnota5 = qtdNota5v
                self.__qtdnota2 = qtdNota2v
            else:
                print(f"Você Sacou R${self.__valorsaque:.2f}")
                print(f"Notas de 100: {cem}, Notas de 50: {cinquenta}, Notas de 20: {vinte}") 
                print(f"Notas de 10: {dez}, Notas de 5: {cinco}, Notas de 2: {dois}")
        else:
            print("Saldo Insuficiente")