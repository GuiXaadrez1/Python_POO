# Esse código visa explicar o comportamento do método construtor
# esse define parâmetros ou atributos essencias para a nossa classe
# ou seja, ele obriga que aquele atributo exista

class Pets():
    
    # criando o método contrutor
    # o self dentro do contrutor funciona como se fosse um this do java
    # Lembrando que é possível colocar lógica e valores padrão no método construtor

    def __init__(self,nome_pet,tipo_animal,pelagem = "Pelos Curtos"):    
        self.nome = nome_pet
        self.tipo_animal = tipo_animal
        self.pelagem = pelagem

    def exibir_informações (self):
        
        informacoes ={
            "Nome Pet": self.nome,
            "Tipo Animal": self.tipo_animal,
            "Pelagem Pet": self.pelagem
        }

        
        print("\nInformações do Pet: \n")

        for chave, valor in informacoes.items():
            print(f"{chave}: {valor}")

    # Método para exibir o som do pet
    def som_pet(self, som_pet: str):
        print(f"O pet faz o som: {som_pet}")


if __name__ == '__main__':
    '''
    # materializando a class Pets com o construtor
    pet1 = Pets('Tom','Gato','Pelos Longos')
    
    # materializando o atributo dora do contrutor para a função
    som_pet = 'Miau Miau'

    pet1.exibir_informações()
    
    # Exibindo o som do pet
    pet1.som_pet(som_pet=som_pet)

    # realizando a instanciação do objeto mais avançada

    nome = input("\nDigite o nome do Pet: ")
    tipo_animal = input("\nSeu pet é qual animal?\nExemplo: (Cachorro..)\nDigite aqui: ")
    pelagem_pet = input("\nQual é a Pelagem do seu Pet?\nDigite aqui: ")
    som_pet2 = input("Digite som que seu Pet faz: ")

    pet2 = Pets(nome,tipo_animal,pelagem_pet)
    pet2.exibir_informações()
    pet2.som_pet(som_pet2)
    '''
    # Usando a forma Padrão do atributo pelagem
 
    nome3 = input("\nDigite o nome do Pet: ")
    tipo_animal3 = input("\nSeu pet é qual animal?\nExemplo: (Cachorro..)\nDigite aqui: ")
    #pelagem_pet3 = input("\nQual é a Pelagem do seu Pet?\nDigite aqui: ")
    som_pet3 = input("Digite som que seu Pet faz: ")
    
    pet3 = Pets(nome3,tipo_animal3)
    pet3.exibir_informações()
    pet3.som_pet(som_pet3)