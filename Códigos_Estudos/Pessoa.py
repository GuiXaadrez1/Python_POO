# Esse é o Primeiro código para Entender Python POO

# Criando a Classe
class Pessoa():
    
    #   Método construtor 
    def __init__(self,nome,idade,altura):
        self.nome = nome # atributos da classe
        self.idade = idade # atributos da classe
        self.altura = altura # atributos da classe

if __name__ == "__main__":
    # Materializando a classe Pessoa em um Objeto
    pessoa1 = Pessoa("Guilherme",21,1.72)
    # Exibindo Informações:
    print("Exibindo informações:")
    print(f"Nome: {pessoa1.nome}")
    print(f"Idade: {pessoa1.idade}")
    print(f"Altura: {pessoa1.altura}")