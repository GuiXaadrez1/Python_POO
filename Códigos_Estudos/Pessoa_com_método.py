# Esse é o Primeiro código para Entender Python POO

# Criando a Classe
class Pessoa():
    
    #   Método construtor 
    def __init__(self,nome,idade,altura):
        self.nome = nome # atributos da classe com encapsulamento publico
        self.idade = idade # atributos da classe
        self.altura = altura # atributos da classe
    
    # método de exibir informações 
    def exibir_informações(self):
        # atributos públicos com sefl sem dois undescore(__.)
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura}m")

if __name__ == "__main__":
    # Materializando a classe Pessoa em um Objeto
    pessoa1 = Pessoa("Guilherme",21,1.72)
   
    # Toda vez que instânciamos um objeto ele vai estar em algum lugar diferente na memória
   
    '''
    # Exibindo Informações puxando uma característica da classe
    print("Exibindo informações:")
    print(f"Nome: {pessoa1.nome}")
    print(f"Idade: {pessoa1.idade}")
    print(f"Altura: {pessoa1.altura}")
    '''
    # Ação/método da classe de exibir informações que são os atributos de pessoa
    pessoa1.exibir_informações()
   
    '''
    print(type(1))
    print(type('Amor'))
    print(type(pessoa1))
    Basicamente tudo em python são objetos
    '''