# Esse código visa explicar o comportamento do método construtor
# esse define parâmetros ou atributos essencias para a nossa classe
# ou seja, ele obriga que aquele atributo exista
# Vamos pegar o mesmo código de Pets_contrutor.py 
# Colocar Docstring nele, pois quanto mais humanizado o código, melhor para realizar
# possíveis manutenções e revições, porém a manutenção do docstring pode ser um problema
# pois, a cada manutenção realizada deve ser registrada no Docstring
# para utilizar Docstring basta colocar dentro do médoto """ descrição do método"""

class Pets():
    
    # criando o método contrutor
    # o self dentro do contrutor funciona como se fosse um this do java
    # Lembrando que é possível colocar lógica e valores padrão no método construtor


    # Criando DocString, por recomendação faça docstring em métodos
    """
    Essa classe é uma planta do objeto Pets Podemos criar um pet recebendo como parâmetro obrigatório
    param nome_pet : Nome do Pet
    param tipo_animel : Especificar qual é o animel. Ex(Cachorro)
    param pelagem : Se possui pelos longos ou curto, por padrão a classe coloca pelos curtos
    return : o próprio pet
    """
    def __init__(self,nome_pet,tipo_animal,pelagem = "Pelos Curtos"):    
        self.nome = nome_pet
        self.tipo_animal = tipo_animal
        self.pelagem = pelagem
        

    def exibir_informações (self):
        # Criando Docstring
        """
        Esse método exibe informações sobre o pet e recebe como parâmetro o próprio objeto instânciado        
        return : dict()
        """
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
        """
            Mostra a ação do som que o animal faz
            param som_pet : str
        """
        print(f"O pet faz o som: {som_pet}")


if __name__ == '__main__':
    
    # materializando e instânciando em um objeto a classe Pets()

    pets = Pets("Albert","Cachorro","Tosado")
    print(dir(pets))
    pets.exibir_informações()
    pets.som_pet('Au Au Auuuuuuuuu!')