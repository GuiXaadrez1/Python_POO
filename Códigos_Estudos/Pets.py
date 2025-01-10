# Esse código visa explicar melhor os conceitos de:
# atributos, métodos e encapsulaemnto de uma class em Python POO

class Pets():

    # atributos = características 
    # Atributos da classe pet sem usar self    
    nome_pet = 'Tom'
    tipo_animal = 'Gato'
    patas = 4
    som =  'Mia'

    # usando essa parte para entender self
    move = "Gato Corre"
    
    # usando self para passar parâmetros na função/método, ele representa a classe
    #  instânciada
    def movimento(self):
        acao = {'Movimento_Pet':self.move}
        for chave, valor in acao.items():
            return f"{chave}: {valor}"

if __name__ == '__main__':
    
    # exibit informações do pet
    informacoes ={
        "Nome Pet": Pets.nome_pet,
        "Tipo Animal": Pets.tipo_animal,
        "Quantidade Patas": Pets.patas,
        "Som do Pet": Pets.som
    }

    print("\nInformações do Pet: \n")

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")
    
    # Chamando diretamente pela classe
    print(Pets.movimento(Pets))
    # veja que colocamos a classe pets para intanciar a classe com o método
    # não é a forma ideal

    # Forma ideal
    # Tranformar a nossa classe em um objeto e puxar a função diretamente dela
    pet1 = Pets()
    print(pet1.movimento())